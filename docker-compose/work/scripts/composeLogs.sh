#!/bin/bash

# Define your Docker Compose directory path
compose_dir="$HOME/dev/projects/easyboot/docker-compose/work"

# Change directory to the Docker Compose directory
cd "$compose_dir" || exit

# Execute docker-compose up
docker-compose logs
