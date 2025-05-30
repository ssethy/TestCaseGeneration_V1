#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until pg_isready -h "$host" -p "$port" > /dev/null 2>&1; do
  echo "Waiting for PostgreSQL at $host:$port..."
  sleep 2
done

echo "PostgreSQL is available. Running: $cmd"
exec $cmd
