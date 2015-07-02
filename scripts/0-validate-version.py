import os
from jsonschema import validate


def main():
    SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
    UNIVERSE_DIR = os.path.dirname(SCRIPTS_DIR)
    SCHEMA_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'meta', 'schema')
    print('Validating version...')
    validate(os.path.join(UNIVERSE_DIR, 'repo', 'meta', 'version.json'),
             os.path.join(SCHEMA_DIR, 'version-schema.json'))
    print('OK')

if __name__ == "__main__":
    main()
