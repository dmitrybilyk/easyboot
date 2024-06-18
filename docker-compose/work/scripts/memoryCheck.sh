#!/bin/bash

resources=(
    "encourage-data"
    "interaction-service"
    "encourage-conversations"
    "encourage-correlation"
    "encourage-zqm-connector"
    "scorecard"
    "encourage-scheduler"
    "encourage-framework"
    "encourage-integrations"
    "automated-qm"
    "interaction-player"
    "speechrec"
)

for resource in "${resources[@]}"; do
    echo "Checking memory usage for resource: $resource"
    kubectl top pods --all-namespaces | grep $resource
    echo ""
done
