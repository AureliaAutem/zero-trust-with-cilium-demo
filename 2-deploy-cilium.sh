#!/bin/zsh

set -e

CLUSTER_NAME="security-demo"

echo "🧱 Creating kind cluster with NO CNI..."
kind create cluster --name $CLUSTER_NAME --config cilium/kind-config.yml

echo "📦 Installing Cilium..."
cilium install

echo "🔍 Enabling Hubble (observability)..."
cilium hubble enable --ui

echo "⏳ Waiting for Cilium to be ready..."
cilium status --wait | egrep -o 'Cilium: .*$'

echo "🐳 Loading images into kind..."
kind load docker-image frontend:latest --name $CLUSTER_NAME
kind load docker-image backend:latest --name $CLUSTER_NAME
kind load docker-image clientapi:latest --name $CLUSTER_NAME
kind load docker-image clientdb:latest --name $CLUSTER_NAME

echo "🚀 Applying Kubernetes manifests..."
kubectl apply -f kube-manifests.yml

sleep 3

echo "⏳ Waiting for pods..."
kubectl wait --for=condition=ready pod --all --timeout=120s