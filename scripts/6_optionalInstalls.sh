#!/bin/bash

# Any other things that may need to be installed

# This script adds the EVA font to your local env to it works
DIRECTORY=~/.fonts/
FONT_FILE=EXPOFILES/assets/fonts/Inter-VariableFont_slnt,wght.ttf

if [ ! -d "$DIRECTORY" ]; then
    mkdir "$DIRECTORY"
    sudo cp "$FONT_FILE" "$DIRECTORY"
else
    echo "$DIRECTORY already exists, skipping directory creation"
fi
