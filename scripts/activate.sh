#!/bin/bash

echo "Use this script to activate your poetry virtual environment"

echo "Type 'deactivate' into the console to exit"

echo "You must be in the project directory for this to work"

source $(poetry env info --path)/bin/activate