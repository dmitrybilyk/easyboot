#!/bin/bash

# Check if the user provided the vmSubIp parameter
if [ -z "$1" ]; then
    echo "Usage: $0 <vmSubIp>"
    exit 1
fi

# Store the vmSubIp parameter
vmSubIp=$1

# Run the Python script and pass the vmSubIp parameter
python3 /home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/copyVM.py "$vmSubIp"


