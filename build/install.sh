current_file_path=$(readlink -f '$0')
this_file_directory=$(dirname "$current_file_path")
parentDir=$(dirname "$this_file_directory")

# Install the dependency required to build the project
pip3 install pylint
pip3 install pylint_runner
pip3 install pytest
pip3 install pytest-cov
pip3 install $parentDir/credscan --upgrade
find $parentDir -name "requirements.txt" | xargs -I {} pip install -r {}