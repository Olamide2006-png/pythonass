def modify_content(content):
    # Example modification: Convert text to uppercase
    return content.upper()

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        modified_content = modify_content(content)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_filename = 'input.txt'
output_filename = 'output.txt'

process_file(input_filename, output_filename)