import json
import os
from jsonschema import validate

SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
UNIVERSE_DIR = os.path.dirname(SCRIPTS_DIR)
SCHEMA_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'meta', 'schema')


def main():

    def load(json_file):
        with open(json_file) as f:
            return json.load(f)

    print('Validating version...')

    validate(load(os.path.join(UNIVERSE_DIR, 'repo', 'meta', 'index.json')),
             load(os.path.join(SCHEMA_DIR, 'index-schema.json')))

    print('OK')

if __name__ == "__main__":
    main()
