import gzip
import os

SCRIPTS_DIR = os.path.dirname(os.path.realpath(__file__))
UNIVERSE_DIR = os.path.dirname(SCRIPTS_DIR)
META_DIR = os.path.join(UNIVERSE_DIR, 'repo', 'meta')
INDEX_FILE_NAME = "index.json"


def main():

    print "Building index..."
    build_index = os.path.join(SCRIPTS_DIR, "build-index.py")

    os.system('{} {}'.format(build_index, UNIVERSE_DIR))
    print('OK')

    print('Compressing index...')
    zip_file_name = '{}.gz'.format(INDEX_FILE_NAME)
    with open(os.path.join(META_DIR, INDEX_FILE_NAME), 'rb') as zip_in:
        with gzip.open(os.path.join(META_DIR, zip_file_name), 'wb') as f_out:
            f_out.writelines(zip_in)

    print('OK')


if __name__ == "__main__":
    main()