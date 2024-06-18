#!/bin/bash

# Execute kubectl command and decode base64 secret
kubectl get secret/keycloak-master-client -ndefault -ojsonpath='{.data.secret}{"\n"}' | base64 -d;echo
