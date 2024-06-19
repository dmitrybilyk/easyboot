#!/bin/bash

# Check if queue name argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <queue_name>"
    exit 1
fi

# Run the Python script with the provided queue name
$HOME/dev/projects/easyboot/venv/bin/python $HOME/dev/projects/easyboot/docker-compose/work/scripts/showLatestRabbitMessage.py "$1"

