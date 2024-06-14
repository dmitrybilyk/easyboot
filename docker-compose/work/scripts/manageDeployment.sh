#!/bin/bash

# Define your Python executable path (if needed)
PYTHON_EXECUTABLE=python3

# Define your Python script path
PYTHON_SCRIPT=/home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/manageDeployment.py

# Check if at least two arguments are passed
if [ $# -ge 2 ]; then
    $PYTHON_EXECUTABLE $PYTHON_SCRIPT $2 "$1"
else
    echo "Usage: $0 <command> <resource>"
    exit 1
fi

