import fnmatch
import json
import os
from jsonschema import validate

SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
UNIVERSE_DIR = os.path.dirname(SCRIPTS_DIR)
SCHEMA_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'meta', 'schema')
PKG_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'packages')


def main():

    print "Validating package definitions..."

    # validate all command.json files
    _validate(PKG_DIR, "command.json",
              os.path.join(SCHEMA_DIR, 'command-schema.json'))

    # validate all config.json files
    _validate(PKG_DIR, "config.json",
              os.path.join(SCHEMA_DIR, 'config-schema.json'))

    # validate all package.json files
    _validate(PKG_DIR, "package.json",
              os.path.join(SCHEMA_DIR, 'package-schema.json'))
    print('OK')


def _validate(pkd_dir, query, schema):

    def load(json_file):
        with open(json_file) as f:
            return json.load(f)

    for root, dirnames, filenames in os.walk(pkd_dir):
        for filename in fnmatch.filter(filenames, query):
            validate(load(os.path.join(root, filename)), load(schema))


if __name__ == "__main__":
    main()
