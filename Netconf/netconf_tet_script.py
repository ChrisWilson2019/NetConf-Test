#!/bin/bash

# Script to test NETCONF connectivity

read -p "Enter the IP address to test NETCONF: " IP

if [ -z "$IP" ]; then
    echo "No IP address provided."
    exit 1
fi

echo "Checking connectivity to $IP on port 830..."
if nc -zv "$IP" 830; then
    echo "Port 830 is open. Starting NETCONF SSH session..."
    ssh -s prime@"$IP" -p 830 netconf
else
    echo "Cannot connect to $IP on port 830. Please check the device or network."
    exit 2
fi
