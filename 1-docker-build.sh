#!/bin/zsh

set -e

echo "🐳 Building images..."

docker build -t frontend ./website-app/frontend
docker build -t backend ./website-app/backend
docker build -t clientapi ./client-app/clientapi
docker build -t clientdb ./client-app/clientdb