#!/bin/zsh

set -e

echo "🌐 Forwarding frontend..."
kubectl port-forward svc/frontend 3000:3000 & 
PF_PID=$!
sleep 2
open http://localhost:3000
wait $PF_PID