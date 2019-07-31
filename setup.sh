#!/bin/bash
BASEDIR=$(pwd)
pip install virtualenv
virtualenv -p python3 venv
$BASEDIR/venv/bin/pip install -r requirements.txt