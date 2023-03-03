.. _warning_messages:

Warning Messages
=====================

When the elevator makes an assumption during the conversion of some content, or is unable to convert the content, a warning message is output.


General
---------------

================================================================================================================== ====    =====
Message                                                                                                            Code    Level
================================================================================================================== ====    =====
Results produced by the stix2-elevator may generate warning messages which should be investigated                  201     info
Observable Expressions should not contain placeholders                                                             202     error
Placeholder *id* should be resolved                                                                                203     error
Found definition for *id*                                                                                          204     info
At least one PLACEHOLDER idref was not resolved in *id*                                                            205     error
At least one observable could not be converted in *id*                                                             206     error
Options not initialized                                                                                            207     error
EMPTY BUNDLE -- No objects created from 1.x input document!                                                        208     warn
Both console and output log have disabled messages.                                                                209     info
OSError *message*                                                                                                  210     error
silent option is not compatible with a policy                                                                      211     warn
Created Marking Structure for *id*                                                                                 212     info
custom_property_prefix is provided, but the missing policy is not 'use-custom-properies'.  It will be ignored.     213     warn
*type* option was not given, but it defaults to true for version 2.1"                                              214     info
Custom properties/objects/extensions are deprecated in version 2.1.  Suggest using 'use-extensions' instead        215     info
The missing policy option of 'use-extensions' cannot be used with version 2.0. 'use-custom-properies' is suggested 216     error
ACS data markings cannot be supported in version 2.0. --acs option is ignored.                                     217     warn
Only one of the options --enable and --disable can be used                                                         218     error
The STIX package header contained no extra information that needed to be generated in STIX 2.x                     219     info
*id* was created to store the extra STIX package header information                                                220     info
================================================================================================================== ====    =====


Handle STIX 1.x Content not supported in STIX 2.x
-------------------------------------------------

============================================================================================================================== ====    =====
Message                                                                                                                        Code    Level
============================================================================================================================== ====    =====
The ``Short_Description`` property is no longer supported in STIX. The text was appended to the description property of *id*   301     info
Appended *property_name* to description of *id*                                                                                302     warn
Title in *type* used for ``name``, appending ``exploit_target`` *id* title in description property                             303     info
Appended ``confidence`` property content to description of *id*                                                                304     warn
Appended ``Statement`` type content to description of *id*                                                                     305     warn
Appended ``Tool`` type content to description of *id*                                                                          306     warn
Missing property *property_name* of *id* is ignored                                                                            307     warn
Used custom property for *property_name* of *id*                                                                               308     warn
Missing property *property_name* of *id* is ignored, because there is no description property                                  309     warn
The Short_Description property in *id* is not supported in STIX 2.x.                                                           310     info
``Not in use``                                                                                                                 311     warn
No extension-definition was found for STIX 1 type *type* in *id*                                                               312     warn
Used an extension property for *property_name* of *id*                                                                         313     warn
Property *property_name* of *id* is ignored, because it can't be represented in an extension                                   314     warn
New extension-definition id *id* was generated for *type*. *id*                                                                315     warn
Custom Content *property_name* of *id* is ignored                                                                              316     warn
Used *object_path* for extension property for *property_name*                                                                  317     warn
Token in control set not recognized: *token*                                                                                   318     warn
Used extensions for ACS data markings. See *id*                                                                                319     warn
Any extra STIX package header properties are ignored                                                                           320     warn
============================================================================================================================== ====    =====


Content not supported in STIX 2.x
---------------------------------------------------

============================================================================================================================================== ====    =====
Message                                                                                                                                        Code    Level
============================================================================================================================================== ====    =====
``Information Source`` on *id* is not representable in STIX 2.x                                                                                401     warn
``Related_Packages`` type in *id* not supported in STIX 2.x                                                                                    402     warn
``Campaign/Activity`` type in *id* not supported in STIX 2.x                                                                                   403     warn
Structured COAs type in *id* are not supported in STIX 2.x                                                                                     404     warn
``ExploitTarget/Weaknesses`` type in *id* not supported in STIX 2.x                                                                            405     warn
``ExploitTarget/Configurations`` type in *id* not supported in STIX 2.x                                                                        406     warn
Indicator *id* has an observable or indicator composite expression which may not supported correctly in STIX 2.x - please check this pattern   407     warn
``TTP/Behavior/Exploits/Exploit`` in *id* not supported in STIX 2.x                                                                            408     warn
``Infrastructure`` in *id* not part of STIX 2.0                                                                                                409     warn
IOC indicator in *id* cannot be converted to a STIX pattern                                                                                    410     warn
Relationship *rel_name* in *id* for *id* is not explicitly supported in STIX 2.x. Expression *pattern* is ANDed                                411     warn
Relationship *rel_name* in *id* for *id* is not explicitly supported in STIX 2.x. %s will be ANDed if/when resolved                            412     warn
Kill Chains type in *id* not supported in STIX 2.x                                                                                             413     warn
Victim Target in *id* did not yield any STIX 2.x object                                                                                        414     warn
TTP *id* did not generate any STIX 2.x object                                                                                                  415     error
No STIX 2.x object generated from embedded object *id*                                                                                         416     warn
*object* did not yield any STIX 2.x object                                                                                                     417     warn
The *property* property of *STIX 1.x object type* is not part of STIX 2.x                                                                      418     warn
*id* is used as a characteristic in an infrastructure object, therefore it is not included as an observed_data instance                        419     warn
Windows Handles are not a part of STIX 2.x                                                                                                     420     warn
The address type address is not part of STIX 2.x                                                                                               421     warn
No pattern term was created from *id*                                                                                                          422     warn
*id* is used as a pattern, therefore it is not included as an observed_data instance                                                           423     warn
*xxx* content is not supported in STIX 2.x                                                                                                     424     warn
Could not resolve Marking Structure *id*                                                                                                       425     warn
MAEC content in *id* cannot be represented in STIX 2.x                                                                                         426     warn
The *relationship name* relationship involving *id* is not explicitly supported in STIX 2.x                                                    427     warn
``roles`` is not a property of a 2.0 identity (*id*).  Perhaps the roles are associated with a related Threat Actor                            428     warn
``HTTPServerResponse`` type is not supported in STIX 2.x                                                                                       429     warn
The confidence value *value* is not found on one of the confidence scales from the specification. No confidence can be inferred                430     warn
The confidence value *value* is not between 0 and 100, which is required for STIX 2.1. No confidence can be inferred                           431     warn
The confidence value *value* cannot be converted                                                                                               432     warn
Location with free text address in *id* not handled yet                                                                                        433     warn
Observed Data objects cannot refer to other external objects: *property name* in *type*"                                                       434     warn
CIQ Address information in *id* is not representable in 2.0                                                                                    435     warn
ACS data markings only supported when --acs option is used. See *id*                                                                           436     warn
Required property *property_name* is not populated on *id*                                                                                     437     warn
A placeholder was generated for required property *property_name* of *id*                                                                      438     warn
============================================================================================================================================== ====    =====

Multiple values are not supported in STIX 2.x
----------------------------------------------------

=========================================================================================================================================== ====    =====
Message                                                                                                                                     Code    Level
=========================================================================================================================================== ====    =====
Cannot convert range of *ip addr 1* to *ip addr 2* in *id* to a CIDR                                                                        501     warn
Only one person name allowed for *id* in STIX 2.x, used *name_1*, *name_2* becomes an alias                                                 502     warn
Only one organization name allowed for *id* in STIX 2.x, used *name_1*, *name_2* becomes an alias                                           503     warn
YARA/SNORT/IOC or other patterns are not supported in STIX 2.0. See *id*                                                                    504     warn
Only two pdfids are allowed for *id*, dropping *pidid*                                                                                      505     warn
Only one alternative test mechanism allowed for *id* in STIX 2.x - used *pattern_lang_1*, dropped *pattern_lang_2*                          506     warn
Only one valid time window allowed for *id* in STIX 2.x - used first one                                                                    507     warn
Only one name for malware is allowed for *id* in STIX 2.x - used *name_1*, dropped *name_2*                                                 508     warn
No STIX 1.x vocab value given for *property*, using 'unknown'                                                                               509     warn
Only one *property name* allowed in STIX 2.x - used *prop_value* in *id*                                                                    510     warn
File size 'window' not allowed in top level observable, using first value                                                                   511     warn
Only one ``HTTP_Request_Response`` used for ``http-request-ext``, using first value                                                         512     warn
=========================================================================================================================================== ====    =====

Possible issue in original STIX 1.x content
--------------------------------------------------

=========================================================================================================================================== ====    =====
Message                                                                                                                                     Code    Level
=========================================================================================================================================== ====    =====
Dangling source reference *source* in *id*                                                                                                  601     error
Dangling target reference *target* in *id*                                                                                                  602     error
STIX 1.X ID: *id* was not mapped to STIX 2.x ID                                                                                             603     warn
Unable to determine the STIX 2.x type for *id*                                                                                              604     error
Malformed id *id*. Generated a new uuid                                                                                                     605     warn
Identity *id* has organization and person names                                                                                             606     error
Dangling kill chain phase id in indicator *id*                                                                                              607     error
``windows-registry-key`` is required to have a ``key`` property                                                                             608     error
*condition* was used, but two values were not provided.                                                                                     609     error
No object mapped to *old_id*                                                                                                                610     warn
Can not associate *old_id* with None                                                                                                        611     error
Identity *id* must have a name, using 'None'                                                                                                612     error
No *type* properties found in *object*                                                                                                      613     warn
Address direction in *id* is inconsistent, using 'src'"                                                                                     614     warn
No ``WinProcess`` properties found in *WinProcess*                                                                                          615     warn
No ``WinService`` properties found in *WinService*                                                                                          616     warn
The custom property name *name* does not adhere to the specification rules                                                                  617     warn
No ISO code for *value* in *identifying_info*                                                                                               618     warn
No *start/end* time for the first valid time interval is available in *id*, other time intervals might be more appropriate                  619     warn
Unable to create a pattern from a File object                                                                                               620     warn
*stix_1.x_property* contains no value                                                                                                       621     warn
No term was yielded for *id*                                                                                                                622     warn
Hive property, *hive_property_name*, is already a prefix of the key property, *key property name*                                           623     warn
The custom property name *name* contains whitespace, replacing it with underscores                                                          624     warn
Found duplicate marking structure *id*                                                                                                      625     info
*hash_string* is not a valid *hash_type* hash                                                                                               626     warn
*enum_value* in *id* is not a member of the *enum_type* enumeration                                                                         627     warn
Unknown condition given in *id* - marked as 'INVALID_CONDITION'                                                                             628     warn
Unable to determine the STIX 2.x type for *id*, which is malformed                                                                          629     error
'equals' allowed in *id* - should be 'Equals'                                                                                               630     warn
Multiple administrative areas with multiple countries in *id* is not handled                                                                631     warn
Unknown phase_id *phase_id* in *id*                                                                                                         632     warn
File path directory is empty *file_path*                                                                                                    633     warn
Any artifact additional artifact info on *id* is not recoverable                                                                            634     warn
*id* contains a observable composition, which implies it not an observation, but a pattern and needs to be contained within an indicator.   635     warn
Address direction in *id* is not provided, using 'src'                                                                                      636     warn
cisa-proprietary is only permitted when ais-consent is everyone, so it has been dropped. See *id*                                           637     warn
Indicator *id* does not contain the information necessary to generate a pattern                                                             638     warn
This observable *id* already is associated with cyber observables                                                                           639     warn
Unable to determine the hash type for *hash value*                                                                                          640     warn
Required property *property* is not provided for ACS data marking                                                                           641     warn
*id* was created without the xsi:type attribute.  Some content might be missing                                                             642     warn
ACS identifier *identifier* is not valid                                                                                                    643     warn
Observable object from pattern cannot be an observed_data_ref of a sighting. See *id*                                                       644     warn
Only one of the properties: Hostname and IP_Address  is allowed.  Dropping Hostname *name*                                                  645     warn
Exploit targets are part of STIX 1x TTP *id*.  Assuming they are related                                                                    646     warn
=========================================================================================================================================== ====    =====

STIX Elevator conversion based on assumptions
----------------------------------------------------

=========================================================================================================================================== ====    =====
Message                                                                                                                                     Code    Level
=========================================================================================================================================== ====    =====
Threat Actor identity *id* being used as basis of attributed-to relationship                                                                701     info
Found STIX 1.X ID: *old_id* replaced by *new_id*                                                                                            702     info
*old_id* is already associated other ids: *tuple_of_new_ids*                                                                                703     info
Including *id of relationship* in *id of report* and added the target_ref *target_ref* to the report                                        704     warn
Including *id of relationship* in *id of report* and added the source_ref *source_ref* to the report                                        705     warn
Including *id of relationship* in *id of report* although the target_ref is unknown                                                         706     warn
Including *id of relationship* in *id of report* although the source_ref is unknown                                                         707     warn
Not including *id of relationship* in *id of report* because there is no corresponding SDO for *target_ref*                                 708     warn
Not including *id of relationship* in *id of report* because there is no corresponding SDO for *source_ref*                                 709     warn
All associated *relationship name* relationships of *id* are assumed to not represent STIX 1.2 versioning                                   710     info
ciq name found in *id*, possibly overriding other name                                                                                      711     warn
Only one type pattern can be specified in *id* - using 'stix'                                                                               712     warn
*id* generated an identity associated with a victim                                                                                         713     info
No condition given for term in *current_observable* - assume '='                                                                            714     warn
Used MATCHES operator for *condition*                                                                                                       715     info
Based on CIQ information, *id* is assumed to be an organization                                                                             716     warn
Threat actor *id* title is used for name property                                                                                           717     info
Using *relationship_name* for the *property* of *id*                                                                                        718     warn
Using first Threat Actor motivation as ``primary_motivation`` value. If more, use ``secondary_motivation``                                  719     info
The ``published property`` is required for STIX 2.x Report *id*, using the created property                                                 720     info
``apply_condition`` assumed to be 'ANY' in *id*                                                                                             721     warn
``content_type`` for ``body_multipart`` of attachment *id* is assumed to be 'text/plain'                                                    722     info
The confidence value in *value* assumed to be a value on a scale between 0 and 100                                                          723     warn
The confidence value in *value* has been converted to an integer so it is valid in STIX 2.1                                                 724     warn
port number is assumed to be a destination port                                                                                             725     warn
"*stix1_id* already used, generated new id *stix2_id                                                                                        726     warn
Custom property name *property* has been converted to all lower case                                                                        727     warn
The is_family property of malware instance *id* is assumed to be true                                                                       728     info
Included parent markings for Relationship *id* and Location *id*                                                                            729     info
Number of sightings given is different than sightings_count in *id*                                                                         730     warn
=========================================================================================================================================== ====    =====

STIX elevator currently doesn't process this content
-----------------------------------------------------------

=========================================================================================================================================== ==== =====
Message                                                                                                                                     Code Level
=========================================================================================================================================== ==== =====
Could not resolve Marking Structure *id*                                                                                                    801  warn
STIX 1.x full file paths are not processed, yet                                                                                             802  warn
Location *id* may not contain all aspects of the STIX 1.x CIQAddress object                                                                 803  warn
Object reference *id* may not be handled correctly                                                                                          804  warn
CybOX object *object* not handled yet                                                                                                       805  warn
Email *property* not handled yet                                                                                                            806  warn
``file:extended_properties:windows_pebinary_ext:optional_header`` is not implemented yet                                                    807  warn
*object* found in *id* cannot be converted to a pattern, yet.                                                                               808  warn
``Not in use``                                                                                                                              809  warn
Negation of *id* is not handled yet                                                                                                         810  warn
Custom object with no name cannot be handled yet                                                                                            811  warn
Condition *condition* on a hive property not handled.                                                                                       812  warn
Cannot convert CybOX 2.x class name *name* to an object_path_root_name                                                                      813  error
``Not in use``                                                                                                                              814  warn
*property* in *id* are not handled, yet.                                                                                                    815  info
Ambiguous file path *path* was not processed                                                                                                816  warn
Pattern expression with STIX 1.x custom objects in *id* is ignored                                                                          817  warn
Pattern expression with STIX 1.x custom properties in *id* is ignored                                                                       818  warn
=========================================================================================================================================== ==== =====


Missing Required Timestamp
---------------------------------

=========================================================================================================================================== ====    =====
Message                                                                                                                                     Code    Level
=========================================================================================================================================== ====    =====
``first_observed`` and ``last_observed`` properties not available directly on *id* - using timestamp                                        901     info
Using parent object timestamp on *identifying_info*                                                                                         902     info
No valid time position information available in *id*, using parent timestamp                                                                903     warn
No ``first_seen`` property on *id* - using timestamp                                                                                        904     info
Timestamp not available for *entity*, using current time                                                                                    905     warn
=========================================================================================================================================== ====    =====
