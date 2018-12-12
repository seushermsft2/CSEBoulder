parentDir=$(dirname $(dirname $(readlink -f "$0")))

# Install the dependency required to build the project
pip3 install pylint
pip3 install pylint_runner
pip3 install pytest
pip3 install pytest-cov
pip3 install $parentDir/credscan --upgrade
find $parentDir -name "requirements.txt" | xargs -I {} pip install -r {}