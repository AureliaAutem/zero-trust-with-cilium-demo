#!/bin/zsh

set -e

echo "📦 Clean Cilium..."
kubectl -n kube-system rollout restart ds/cilium

echo "⏳ Waiting for Cilium to be ready..."
cilium status --wait | egrep -o 'Cilium: .*$'

echo "🚀 Deploying Cilium Network Policies..."
kubectl apply -f cilium/policies.yml
