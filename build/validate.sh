current_file_path=$(readlink -f '$0')
this_file_directory=$(dirname "$current_file_path")
parentDir=$(dirname "$this_file_directory")


# Run the linter on every file
pylint_runner $parentDir

# Run test coverage on the project
py.test --cov=$parentDir --cov-report=xml $parentDir