from __future__ import print_function

# Standard Library
import io
import json
import os
import sys

# internal
from stix2elevator import elevate
from stix2elevator.options import (
    get_option_value, initialize_options, set_option_value
)
from stix2elevator.utils import (
    extension_definition_id_property, find_dir, get_environment_variable_value,
    id_property, iterpath
)

BEFORE_FILES = []
BEFORE_FILENAMES = []
MASTER_JSON_FILES = []

_ID_IGNORE_2_0 = (u"id", u"idref", u"created_by_ref", u"object_refs", u"target_ref", u"source_ref",
                  u"sighting_of_ref", u"observed_data_refs",
                  u"bcc_refs", u"cc_refs", u"child_refs", u"object_refs", u"opened_connection_refs", u"to_refs",
                  u"body_raw_ref", u"dst_ref", u"from_ref", u"parent_ref", u"parent_directory_ref", u"src_ref")

_IGNORE_2_x = (u"created", u"modified", u"first_seen", u"valid_from", u"valid_until", u"last_seen",
               u"first_observed", u"last_observed", u"published",
               u"external_references",
               u"created_by_ref", u"marking_ref", u"object_marking_refs", u"where_sighted_refs", u"source_ref", u"target_ref",
               # extensions
               u"x_elevator_contacts", u"contacts")


def idiom_elevator_mappings(before_file_path, stored_json, version, missing_policy, ignore):
    """Test fresh conversion from XML to JSON matches stored JSON samples."""
    print("Checking - " + before_file_path)
    print("With Master - " + stored_json["id"])
    validator_args = "--version " + version
    if missing_policy == "use-extensions":
        validator_args += " -s extension-definition-schemas"

    initialize_options(options={"spec_version": version,
                                "missing_policy": missing_policy,
                                "log_level": "WARN",
                                "incidents": True,
                                "validator_args": validator_args})
    if not get_option_value("policy") == "no_policy":
        print("'no_policy' is the default for testing")
    set_option_value("policy", "no_policy")
    if version == "2.1":
        set_option_value("acs", True)
    sys.setrecursionlimit(3000)
    converted_json = elevate(before_file_path)
    print(converted_json)
    converted_json = json.loads(converted_json)
    return idiom_mappings(converted_json, stored_json, ignore)


def idiom_mappings(converted_json, stored_json, ignored_properties):

    for good, to_check in zip(iterpath(stored_json), iterpath(converted_json)):

        good_path, good_value = good
        check_path, check_value = to_check
        # last_good_field = good_path[-1]

        if isinstance(good_value, (dict, list)):
            # Rule #1: No need to verify iterable types. Since we will deal
            # with individual values in the future.
            continue

        if (any(s in (u"object_marking_refs", u"granular_markings")
                for s in good_path)):
            # Exception to Rule #1: object_marking_refs and granular_markings
            # are not verifiable because they contain identifiers per rule #2.
            continue

        # make sure that the property names match
        if any(x in ignored_properties for x in good_path) and good_path[-1] == check_path[-1]:
            # Rule #2: Since fresh conversion may create dynamic values.
            # Some fields are omitted for verification. Currently
            # fields with: identifier and timestamp values.
            continue

        yield good, to_check


def setup_tests(before_idioms_dir, after_idioms_dir, before_suffix, after_suffix):
    print("Setting up tests from following directories...")
    print(before_idioms_dir)
    print(after_idioms_dir)

    for after_filename in sorted(os.listdir(after_idioms_dir)):
        if after_filename.endswith(after_suffix):
            path = os.path.join(after_idioms_dir, after_filename)

            with io.open(path, "r", encoding="utf-8") as f:
                loaded_json = json.load(f)

            MASTER_JSON_FILES.append(loaded_json)

    for before_filename in sorted(os.listdir(before_idioms_dir)):
        if before_filename.endswith(before_suffix):
            path = os.path.join(before_idioms_dir, before_filename)
            BEFORE_FILENAMES.append(before_filename.split(".")[0])
            BEFORE_FILES.append(path)


def setup_elevator_tests(version, missing_policy):
    directory = os.path.dirname(__file__)
    json_directory_suffix = ""
    if missing_policy == "use-custom-properties":
        json_directory_suffix = "-custom"
    elif missing_policy == "use-extensions":
        json_directory_suffix = "-extensions"
    elif missing_policy == "ignore":
        json_directory_suffix = "-ignore"
    xml_idioms_dir = find_dir(directory, "idioms-xml")
    json_idioms_dir = find_dir(directory, "idioms-json" + "-" + version + json_directory_suffix)
    setup_tests(xml_idioms_dir, json_idioms_dir, ".xml", ".json")


def ignorable_id_types(type):
    types = {
        "attack-pattern", "campaign", "course-of-action", "grouping", "identity", "indicator", "infrastructure",
        "intrusion-set", "location", "malware", "malware-analysis", "note", "observed-data", "opinion",
        "report", "threat-actor", "tool", "vulnerability", "relationship", "sighting", "bundle", "process"
    }
    return type in types


def ignore_this_id(uuid_of_good_id, uuid_of_check_id):
    parts_of_good = uuid_of_good_id.split("-")
    parts_of_check = uuid_of_check_id.split("-")
    # look at first digit of second group to see if what version of uuid it is
    return (parts_of_good[2].startswith("4") and parts_of_check[2].startswith("4"))


def id_2x(id):
    try:
        return id.find("--") != -1
    except AttributeError:
        return False


def name_property(path):
    return "name" == path[0][-1]


def test_elevator_idiom_mapping(test_file, stored_master, version, missing_policy, ignore):
    errors = []
    for good_path, check_path in idiom_elevator_mappings(test_file, stored_master, version, missing_policy, ignore):
        if extension_definition_id_property(check_path) and extension_definition_id_property(good_path):
            # use this hack to ignore differences in the extension-definition id
            dummy_extension = "extension-definition--xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            check_path[0][3] = good_path[0][3] = dummy_extension
        if id_property(check_path) and id_property(good_path):
            if id_2x(good_path[1]) and id_2x(check_path[1]):
                uuid_of_good_id = good_path[1].split("--")[1]
                uuid_of_check_id = check_path[1].split("--")[1]
                if ignore_this_id(uuid_of_good_id, uuid_of_check_id):
                    continue
        # handle placeholders for required fields
        if name_property(check_path) and name_property(good_path):
            if good_path[1].startswith("Placeholder for") and check_path[1].startswith("Placeholder for"):
                continue
        if good_path != check_path:
            find_index_of_difference(good_path, check_path)
            errors.append({"Expect": json.dumps(good_path), "Actual": json.dumps(check_path)})

    if errors:
        print("Number of errors: " + str(len(errors)))
        print(json.dumps(errors, indent=4), file=sys.stderr)
        raise AssertionError(errors)


def pytest_generate_tests(metafunc):
    version = get_environment_variable_value('VERSION', "2.1")
    if version == "2.1":
        ignore = _IGNORE_2_x
    else:
        ignore = _IGNORE_2_x + _ID_IGNORE_2_0
    missing_policy = get_environment_variable_value("MISSING_POLICY", "ignore")
    if missing_policy not in ["use-custom-properties", "add-to-description", "ignore", "use-extensions"]:
        raise RuntimeError("Missing policy " + missing_policy + " isn't one of the policy choices")
    setup_elevator_tests(version, missing_policy)
    argnames = ["test_file", "stored_master", "version", "missing_policy", "ignore"]
    argvalues = [(x, y, version, missing_policy, ignore) for x, y in zip(BEFORE_FILES, MASTER_JSON_FILES)]

    metafunc.parametrize(argnames=argnames, argvalues=argvalues, ids=BEFORE_FILENAMES, scope="function")


def find_index_of_difference(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        str1_len = len(str1[1])
        str2_len = len(str2[1])
        i = j = 0

        while True:
            if i < str1_len and j < str2_len:
                if str1[1][i] != str2[1][j]:
                    print("difference at " + str(i), file=sys.stderr)
                    break
            elif i == str1_len and j == str2_len:
                print("no difference", file=sys.stderr)
                break
            elif i == str1_len:
                print("str1 ended at " + str(i), file=sys.stderr)
                break
            elif j == str2_len:
                print("str2 ended at " + str(j), file=sys.stderr)
                break
            i = i + 1
            j = j + 1
