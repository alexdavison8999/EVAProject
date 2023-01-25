#!/bin/bash

# If there's an error at the poetry --version, make sure that the pyenv installation was successfull and that
# the export text line got added to your bashrc file (nano ~/.bashrc to look)
poetry --version
# The above line should produce something like 'Poetry (X.X.X), currently 1.3.2 (Jan 24th, 2023)'

mkdir projects
cd projects

git clone https://github.com/KroegerP/EVAProject.git
cd EVAProject

poetry shell

alias startEnv="source $(poetry env info --path)/bin/activate"

echo "To start your poetry env, type 'startEnv'"

echo "Type 'deactivate' into the console to exit"

echo "You must be in the project directory for this to work"

# source $(poetry env info --path)/bin/activate