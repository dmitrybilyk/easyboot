#!/bin/bash

# Execute kubectl command and decode base64 secret
kubectl get secret/postgres-secrets -ndefault -ojsonpath='{.data.db\.pass}{"\n"}' | base64 -d;echo
