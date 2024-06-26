#!/bin/bash

# Check if a hostname argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <hostname>"
    exit 1
fi

# Assign the first argument to a variable
hostname="$1"

# Run the Python script with the provided hostname
$HOME/dev/projects/easyboot/venv/bin/python $HOME/dev/projects/easyboot/docker-compose/work/scripts/importCert.py "$hostname"


