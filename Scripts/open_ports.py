"""
Written by Kyser Clark

KyserClark.com
@KyserClark
github.com/KyserClark
linkedin.com/in/KyserClark/

This python scripts takes any nmap scan output file as an argument and prints all open ports on a single line seperated
by commas. This is useful to do follow up scans on the open ports with the -p argument.
"""

import sys

# Open the file containing nmap scan output
with open(sys.argv[1], 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Split the contents of the file by newline characters
lines = contents.split('\n')

# Create an empty list to store the open port numbers
open_ports = []

# Iterate over each line
for line in lines:
    # Split the line by whitespace characters
    parts = line.split()
    # Check if the line contains an open port
    if len(parts) > 1 and parts[1] == 'open':
        # Get the port number from the first whitespace-separated part of the line
        port_number = parts[0].split('/')[0]
        # Add the port number to the list
        open_ports.append(port_number)

# Print the list of open port numbers separated by commas
print(','.join(open_ports))
