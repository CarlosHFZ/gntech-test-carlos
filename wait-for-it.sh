#!/usr/bin/env bash

hostport="$1"
shift
cmd="$@"

# Separar host e porta
host=$(echo "$hostport" | cut -d: -f1)
port=$(echo "$hostport" | cut -d: -f2)

until nc -z "$host" "$port"; do
  >&2 echo "Waiting for $host:$port to be available..."
  sleep 1
done

>&2 echo "$host:$port is available — starting the app"
exec $cmd
