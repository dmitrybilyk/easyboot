#!/bin/bash

# Change directory to the Docker Compose directory
cd "$compose_dir" || exit

services=$(docker-compose ps --services)

for service in $services; do
  container=$(docker-compose ps -q $service)
  health_status=$(docker inspect --format='{{json .State.Health.Status}}' $container)

  while [ "$health_status" != "\"healthy\"" ]; do
    echo "Waiting for $service to be healthy..."
    sleep 5
    health_status=$(docker inspect --format='{{json .State.Health.Status}}' $container)
  done

  echo "$service is healthy."
done

echo "All services are healthy."


