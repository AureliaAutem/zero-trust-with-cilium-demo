#!/bin/bash

set -e

echo "🧽 Deleting Kubernetes resources..."
kubectl delete -f kube-manifests.yml --ignore-not-found

echo "⏳ Waiting for resources to terminate..."
sleep 5

echo "💣 Deleting kind cluster..."
kind delete cluster --name security-demo

echo "✅ Cleanup complete!"