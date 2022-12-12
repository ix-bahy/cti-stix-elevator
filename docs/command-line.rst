Command Line Interface
===========================

The elevator comes with a bundled script which you can use to elevate
STIX 1.x content to STIX 2.x content:

.. code-block:: text

    usage: stix2_elevator [-h]
              [--missing-policy {use-extensions,use-custom-properties,add-to-description,ignore}]
              [--header-object-type {report,grouping}]
              [--custom-property-prefix CUSTOM_PROPERTY_PREFIX]
              [--infrastructure]
              [--acs]
              [--incidents]
              [--package-created-by-id PACKAGE_CREATED_BY_ID]
              [--default-timestamp DEFAULT_TIMESTAMP]
              [--validator-args VALIDATOR_ARGS]
              [-e ENABLED]
              [-d DISABLED]
              [-s]
              [--message-log-directory MESSAGE_LOG_DIRECTORY]
              [--log-level {DEBUG,INFO,WARN,ERROR,CRITICAL}]
              [-m MARKINGS_ALLOWED]
              [-p {no_policy,strict_policy}]
              [-v {2.0,2.1}]
              [-r]
              file


stix2-elevator v4.1.7

positional arguments:

.. code-block:: text

  file          The input STIX 1.x document to be elevated.

optional arguments:

.. code-block:: text

  -h, --help
                Show this help message and exit

  --missing-policy {use-extensions,use-custom-properties,add-to-description,ignore}
                Policy for including STIX 1.x content that cannot be
                represented directly in STIX 2.x. The default is 'add-
                to-description'.

  --header-object-type {report,grouping}
                What STIX 2 type to use to store extra information
                from the STIX 1 package header.The default is
                'report'.

  --custom-property-prefix CUSTOM_PROPERTY_PREFIX
                Prefix to use for custom property names when missing
                policy is 'use-custom-properties'. The default is
                'elevator'.

  --infrastructure
                Infrastructure will be included in the conversion.
                Default for version 2.1 is true.

  --incidents
                Incidents will be included in the conversion.
                Default for version 2.1 is true.

  --acs
                Process ACS data markings
                Default is false.

  --package-created-by-id PACKAGE_CREATED_BY_ID
                Use provided identifier for "created_by_ref"
                properties.

                Example: --package-created-by-id "identity--1234abcd-1a12-42a3-0ab4-1234abcd5678"

  --default-timestamp DEFAULT_TIMESTAMP
                Use provided timestamp for properties that require a
                timestamp.

                Example: --default-timestamp "2016-11-15T13:10:35.053000Z"

  --validator-args VALIDATOR_ARGS
                Arguments to pass to stix2-validator.
                See https://stix2-validator.readthedocs.io/en/latest/options.html.

                Example: --validator-args="-v --strict-types -d 212"

  -e ENABLED, --enable ENABLED
                A comma-separated list of the stix2-elevator messages
                to enable. Not to be used with --disable.

                Example: --enable 250

  -d DISABLED, --disable DISABLED
                A comma-separated list of the stix2-elevator messages
                to disable. Not to be used with --enable.

                Example: --disable 212,220

  -s, --silent
                If this flag is set, all stix2-elevator messages will
                be disabled.

  --message-log-directory MESSAGE_LOG_DIRECTORY
                If this flag is set, all stix2-elevator messages will
                be saved to a file. The name of the file will be the
                input file with extension .log in the specified
                directory.

                Note, make sure the directory already exists.

                Example: --message-log-directory "../logs".

  --log-level {DEBUG,INFO,WARN,ERROR,CRITICAL}
                The logging output level.

  -m MARKINGS_ALLOWED, --markings-allowed MARKINGS_ALLOWED
                Avoid error exit, if these markings types
                (as specified via their python class names) are in the
                content, but not supported by the elevator. Specify as
                a comma-separated list.

                Example: --markings-allowed "ISAMarkingsAssertion,ISAMarkings"

  -p {no_policy,strict_policy},
  --error-policy {no_policy,strict_policy},
  --policy {no_policy,strict_policy}   #deprecated
               The policy to deal with errors. The default is 'no_policy'.

  -v {2.0,2.1}, --version {2.0,2.1}
               The version of stix 2 to be produced. The default is 2.1

  -r, --ignore-required-properties
                        Do not provide missing required properties


Refer to the :ref:`warning_messages` section for all stix2-elevator messages. Use the
associated code number to ``--enable`` or ``--disable`` a message. By default, the
stix2-elevator displays all messages.

The --enable and --disable arguments cannot be used at the same time.  When a message code is not specified in the --enable
option it will not be displayed.  When a message code is not specified in the --disable
option it will be displayed.  If the number of messages codes to be both enabled and disabled are both large, it is sufficient
to just specify the shorter one.

Note: disabling the message does not disable any functionality.
