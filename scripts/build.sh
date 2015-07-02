#!/bin/bash
set -o errexit -o nounset -o pipefail

SCRIPTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";

echo "Building the universe!";

python $SCRIPTS_DIR/"0-validate-version.py";
python $SCRIPTS_DIR/"1-validate-packages.py";
python $SCRIPTS_DIR/"2-build-index.py";
python $SCRIPTS_DIR/"3-validate-index.py";
python $SCRIPTS_DIR/"4-detect-dependency-cycles.py";

