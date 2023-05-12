#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python version 3, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi


python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py $1