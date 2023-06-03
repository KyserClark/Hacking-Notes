"""
Written by Kyser Clark

KyserClark.com
@KyserClark
github.com/KyserClark
linkedin.com/in/KyserClark/

This python script takes any .txt file as an argument and removes all whitespace from it.
"""

import sys

def remove_whitespace(filename):
    with open(filename, 'r') as file:
        content = file.read()
        content = content.replace('\n', '').replace('\r', '').replace(' ', '')
    
    with open(filename, 'w') as file:
        file.write(content)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the filename as an argument.")
    else:
        filename = sys.argv[1]
        remove_whitespace(filename)
        print(f"Whitespace removed from {filename}.")
