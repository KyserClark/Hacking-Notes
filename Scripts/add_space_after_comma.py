"""
Written by Kyser Clark

KyserClark.com
@KyserClark
github.com/KyserClark
linkedin.com/in/KyserClark/

This python script takes any .txt file as an argument and adds a space after every comma in the file.
"""

import sys

def add_space_after_comma(file_path):
    try:
        # Read the input file
        with open(file_path, 'r') as file:
            content = file.read()

        # Add a space after each comma
        updated_content = content.replace(',', ', ')

        # Rewrite the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        # Print the output
        print(updated_content)

    except IOError:
        print(f"Error: Could not read the file '{file_path}'")

# Check if the file path is provided as an argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    add_space_after_comma(file_path)
else:
    print("Please provide the file path as an argument.")
