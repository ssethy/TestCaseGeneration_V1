#!/bin/bash

echo "🔧 Switching to Minikube Docker context..."
eval $(minikube docker-env)

services=(
  "document-preprocessor"
  "requirement-service"
  "testcase-db-service"
  "api-layer"
)

for service in "${services[@]}"; do
  echo "🐳 Building image for $service..."
  docker build -t "$service:latest" "./$service"
done

echo "✅ All images built in Minikube context."

