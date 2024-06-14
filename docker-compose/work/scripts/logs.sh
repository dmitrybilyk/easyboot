#!/bin/bash

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <pod_name> [<since_minutes>] [<to_follow>]"
    exit 1
fi

# Assign arguments to variables
POD_NAME=${1:-"automated"}
SINCE_MINUTES=${2:-5}
TO_FOLLOW=${3:-true}

# Execute the Python script with the provided arguments
python3 /home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/logs.py "$POD_NAME" "$SINCE_MINUTES" "$TO_FOLLOW"

