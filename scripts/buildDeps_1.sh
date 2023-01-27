#!/bin/bash

sudo apt update
sudo apt upgrade 
sudo apt install build-essential

sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

sudo apt install libcups2-dev python3-pyaudio libcairo2-dev \
libcurl4-openssl-dev libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev \
gir1.2-gtk-3.0 libdbus-1-dev libdbus-glib-1-dev

sudo apt install libgirepository1.0-dev gcc libcairo2-dev gir1.2-gtk-3.0

sudo apt install espeak ffmpeg libespeak1

sudo apt install python3-pyaudio

sudo apt install smbclient libsmbclient libsmbclient-dev

sudo apt install python3-cupshelpers

exec $SHELL



