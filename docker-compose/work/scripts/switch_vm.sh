#!/bin/bash

# Default value for VM_SUB_IP
DEFAULT_VM_SUB_IP="085"

# Check if an argument is provided, otherwise use the default value
if [ $# -eq 0 ]; then
    VM_SUB_IP=$DEFAULT_VM_SUB_IP
else
    VM_SUB_IP=$1
fi

# Execute the Python script with the provided arguments
$HOME/dev/projects/easyboot/venv/bin/python $HOME/dev/projects/easyboot/docker-compose/work/scripts/switch_vm.py "$VM_SUB_IP"

