def php_escape(input_string):
    """
    Created by Kyser Clark - Cybersecurity 
    @KyserClark

    Escapes a string for safe use in PHP commands, focusing on quotes and backslashes.
    Additional rules can be added as needed.

    To use: Call the script, then you will be prompted to input the string you wish to make safe for PHP commands.
    """
    # Replace backslashes first to avoid escaping already escaped characters
    escaped_string = input_string.replace("\\", "\\\\")
    
    # Escape single quotes
    escaped_string = escaped_string.replace("'", "\\'")
    
    # Escape double quotes
    escaped_string = input_string.replace('"', '\\"')
    
    # Replace newlines with the literal string '\n' if needed
    escaped_string = escaped_string.replace("\n", "\\n")
    
    return escaped_string

# Example usage
if __name__ == "__main__":
    original_string = input("Enter the string to be escaped for PHP: ")
    escaped_string = php_escape(original_string)
    print("Escaped string for PHP:")
    print(escaped_string)
