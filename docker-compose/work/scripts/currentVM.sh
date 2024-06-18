#!/bin/bash

# Define the path to the config file
CONFIG_FILE="/home/dmytro/.kube/config"

# Check if the config file exists
if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Config file not found at $CONFIG_FILE"
  exit 1
fi

# Search for the word 'server' in the config file and display the matching lines
grep -n 'server' "$CONFIG_FILE"
