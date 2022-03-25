#!/bin/bash
echo "Starting bootstrap script..."

function init() {
  echo "Checking for python3..."
  PYTHON_VAL=$(which python3)

  if [[ ! -z $PYTHON_VAL ]]; then
    echo "Python3 exists, installing dependencies..."
    pip3 install --upgrade pip
    pip3 install paramiko getpass4 flask

  else
    echo "Python3 doesn't exist, installing Python3 and dependencies..."
    YUM_CMD=$(which yum)
    APT_GET_CMD=$(which apt-get)
    BREW_CMD=$(which brew)

    if [[ ! -z $YUM_CMD ]]; then
       yum install python3
    elif [[ ! -z $APT_GET_CMD ]]; then
      apt-get python3
    elif [[ ! -z $BREW_CMD ]]; then
      brew install python3
    else
      echo "Error: can't install Python3"
      exit 1;

    pip3 install --upgrade pip
    pip3 install paramiko getpass4 flask
    fi
  fi

}

function enable_cli() {
  echo "Making program into command line..."
  chmod +x $PWD/configdeploy
  mkdir bin
  cp -r src bin && cp configdeploy bin
  export PATH=$PATH":$PWD/bin"

}

init
enable_cli
exec "$SHELL"