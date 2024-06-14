#!/bin/bash

# Example usage: ./run_script.sh vm_ip service_name tag_version

# Parameters
VM_IP=$1
SERVICE_NAME=$2
TAG_VERSION=$3

# Run Python script with parameters
/home/dmytro/dev/projects/easyboot/venv/bin/python /home/dmytro/dev/projects/easyboot/docker-compose/work/scripts/buildAndPushImage.py "$VM_IP" "$SERVICE_NAME" "$TAG_VERSION"
