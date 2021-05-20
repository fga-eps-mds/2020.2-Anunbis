#!/bin/bash

black --version
if [[ "$?" != "0" ]]; then
    echo "Installing black from pip3... .. ."
    pip3 install black --quiet
fi
flake8 --version
if [[ "$?" != "0" ]]; then
    echo "Installing black from pip3... .. ."
    pip3 install flake8 --quiet
fi

black ./app ./tests 
flake8 --max-line-length=88 --exclude migrations

