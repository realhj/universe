import fnmatch
import os
from jsonschema import validate


def main():
    SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
    UNIVERSE_DIR = os.path.dirname(SCRIPTS_DIR)
    SCHEMA_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'meta', 'schema')
    PKG_DIR=os.path.join(UNIVERSE_DIR, 'repo', 'packages')
    print "Validating package definitions..."

    # validate all command.json files
    _validate(PKG_DIR, "command.json",
              os.path.join(SCHEMA_DIR, 'command-schema.json'))

    # validate all config.json files
    _validate(PKG_DIR, "config.json",
              os.path.join(SCHEMA_DIR, 'config-schema.json'))

    # validate all package.json files
    _validate(PKG_DIR, "package.json",
              os.path.join(SCHEMA_DIR, 'config-schema.json'))
    print('OK')


def _validate(pkd_dir, query, schema):

    for root, dirnames, filenames in os.walk(pkd_dir):
        for filename in fnmatch.filter(filenames, query):
            validate(os.path.join(root, filename), schema)


if __name__ == "__main__":
    main()