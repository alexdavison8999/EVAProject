#!/bin/bash

# If there's an error at the pyenv --version, make sure that the pyenv installation was successfull and that
# those text lines got added to your bashrc file (nano ~/.bashrc to look)
pyenv --version

pyenv install 3.9.2
pyenv global 3.9.2

curl -sSL https://install.python-poetry.org | python3 -

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

exec $SHELL