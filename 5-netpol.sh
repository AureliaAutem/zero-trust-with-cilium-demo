#!/bin/zsh

set -e

echo "🚀 Deploying Cilium Network Policies..."
kubectl apply -f cilium/policies.yml
