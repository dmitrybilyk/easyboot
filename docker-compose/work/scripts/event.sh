#!/bin/bash

# Check if any parameters are provided
if [ "$#" -eq 0 ]; then
    echo "No parameters provided."
    exit 1
fi

# Execute Python script with parameters
$HOME/dev/projects/easyboot/venv/bin/python3 $HOME/dev/projects/easyboot/docker-compose/work/scripts/event.py "$@"
