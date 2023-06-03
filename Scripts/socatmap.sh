#!/bin/bash

# Written by Kyser Clark

# KyserClark.com
# @KyserClark
# github.com/KyserClark
# linkedin.com/in/KyserClark/

# This bash script is useful if you need to perform a portscan on a machine that has socat, but not netcat, nc, or nmap. 
# This situation is very specific but I have seen it happen. Which is why I made this tool.

# Define the usage message function
function usage {
  echo "Usage: $0 -i [IP Address] -p [Port(s)]"
  echo "Example: $0 -i 192.168.0.1 -p 80,443,1000-2000,-"
  exit 1
}

# Parse the command-line arguments
while getopts ":i:p:" opt; do
  case ${opt} in
    i )
      IP=$OPTARG
      ;;
    p )
      PORTS=$OPTARG
      ;;
    * )
      usage
      ;;
  esac
done

# Check if the IP address and ports have been provided
if [[ -z $IP || -z $PORTS ]]; then
  usage
fi

# Use socat to scan the ports on the target machine
for PORT in $(echo $PORTS | tr ',' ' '); do
  if [[ $PORT == "-" ]]; then
    PORT_RANGE="1-65535"
  elif [[ $PORT == *-* ]]; then
    START_PORT=$(echo $PORT | cut -d '-' -f 1)
    END_PORT=$(echo $PORT | cut -d '-' -f 2)
    PORT_RANGE=$(seq $START_PORT $END_PORT | tr '\n' ',')
    PORT_RANGE=${PORT_RANGE::-1} # Remove the trailing comma
  else
    PORT_RANGE=$PORT
  fi

  for PORT in $(echo $PORT_RANGE | tr ',' ' '); do
    (echo >/dev/tcp/$IP/$PORT >/dev/null 2>&1) &
    PID=$!
    sleep 0.2s
    kill $PID >/dev/null 2>&1
    wait $PID >/dev/null 2>&1
    if [[ $? -eq 0 ]]; then
      echo "Port $PORT is open"
    fi
  done
done
