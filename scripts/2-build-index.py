import fnmatch
import gzip
import os
from jsonschema import validate


def main():
    SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
    UNIVERSE_DIR = os.path.dirname(SCRIPTS_DIR)
    META_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'meta')
    INDEX_FILE_NAME="index.json"

    print "Building index..."
    build_index = os.path.join(SCRIPTS_DIR, "build-index.py")

    os.system('{} {}'.format(build_index, UNIVERSE_DIR))
    print('OK')

    print('Compressing index...')
    zip_file_name ='{}.gz'.format(INDEX_FILE_NAME)
    with open(os.path.join(META_DIR, 'INDEX_FILE_NAME'), 'rb') as zip_in:
        with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
            f_out.writelines(os.path.join(META_DIR, zip_file_name))

    print('OK')


if __name__ == "__main__":
    main()