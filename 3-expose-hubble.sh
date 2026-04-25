#!/bin/zsh

set -e

echo "🌐 Open hubble UI..."
cilium hubble ui
sleep 2
open http://localhost:12000