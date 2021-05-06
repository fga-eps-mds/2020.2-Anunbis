#!/bin/sh 

black --version
if [[ "$?" != "0" ]]; then
    pip install black --quiet
fi
flake8 --version
if [[ "$?" != "0" ]]; then
    pip install flake8 --quiet
fi

black ./
flake8 --max-line-length=88

$SHELL