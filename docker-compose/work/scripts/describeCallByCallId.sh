#!/bin/bash

# Assign call id to a variable
callid="$1"

# Execute Python script with call id parameter
python3 /home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/describeCallByCallId.py "$callid"
