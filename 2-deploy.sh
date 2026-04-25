#!/bin/zsh

set -e

echo "🧱 Creating kind cluster..."
kind create cluster --name security-demo

echo "🐳 Loading images into kind..."

kind load docker-image frontend:latest --name security-demo
kind load docker-image backend:latest --name security-demo
kind load docker-image clientapi:latest --name security-demo
kind load docker-image clientdb:latest --name security-demo

echo "🚀 Applying Kubernetes manifests..."
kubectl apply -f kube-manifests.yml

sleep 3

echo "⏳ Waiting for pods..."
kubectl wait --for=condition=ready pod --all --timeout=120s
