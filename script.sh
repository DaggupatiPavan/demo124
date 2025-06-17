#!/bin/bash

VERSION=$1
LOG_LEVEL=$2
API_URL=$3

python3 log_action.py $VERSION $LOG_LEVEL $API_URL
