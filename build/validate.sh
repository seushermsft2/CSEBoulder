parentDir=$(dirname $(dirname $(readlink -f "$0")))

# Run the linter on every file
pylint_runner $parentDir

# Run test coverage on the project
py.test --cov=$parentDir --cov-report=xml $parentDir