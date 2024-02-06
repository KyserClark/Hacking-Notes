#!/bin/bash

# Function to display the help menu
show_help() {
    echo "Search for STRING in FILEPATH and return NUM characters that appear after each instance."
    echo "created by Kyser Clark - Cybersecurity | KyserClark.com | @KyserClark"
    echo ""
    echo "Usage: ./getcharacters.sh [OPTION]... FILEPATH STRING NUM"
    echo ""
    echo "Example usage: ./getcharacters.sh text.txt key= 1"
    echo ""
    echo "The above example will return the 1st character after every instance of key="
    echo "I created this code because I couldn't find a tool to filter out"
    echo "user input via a keylogger that receives user input via a python3 http server"
    echo ""
    
    echo "Options:"
    echo "  -c          Make the search case sensitive."
    echo "  -d DELIM    Use DELIM as a character delimiter for the output."
    echo "  -h          Display this help and exit."
}

# Default options
CASE_SENSITIVE=false
DELIMITER=""

# Parse options
while getopts "hcd:" opt; do
    case ${opt} in
        h )
            show_help
            exit 0
            ;;
        c )
            CASE_SENSITIVE=true
            ;;
        d )
            DELIMITER=$OPTARG
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            show_help
            exit 1
            ;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            show_help
            exit 1
            ;;
    esac
done

# Remove parsed options from the positional parameters
shift $((OPTIND -1))

# Check for the correct number of positional arguments
if [ $# -ne 3 ]; then
    echo "Error: Invalid number of arguments."
    show_help
    exit 1
fi

FILEPATH="$1"
SEARCH_STRING="$2"
NUM_CHARS="$3"

# Perform search
if $CASE_SENSITIVE; then
    grep -oP "$SEARCH_STRING\K.{0,$NUM_CHARS}" "$FILEPATH" | tr -d '\n' | sed "s/./&$DELIMITER/g"
else
    grep -oPai "$SEARCH_STRING\K.{0,$NUM_CHARS}" "$FILEPATH" | tr -d '\n' | sed "s/./&$DELIMITER/g"
fi

# Ensure the delimiter does not appear at the end of the output
if [ -n "$DELIMITER" ]; then
    echo -n | awk '{print substr($0, 1, length($0)-1)}'
fi

echo
