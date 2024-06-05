#!/bin/bash

# Check if any parameters are provided
if [ "$#" -eq 0 ]; then
    echo "No parameters provided."
    exit 1
fi

# Execute Python script with parameters
/home/dmytro/dev/projects/easyboot/venv/bin/python /home/dmytro/dev/projects/easyboot/docker-compose/work/utils/calendar_event.py "$@"
