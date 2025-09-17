def read_file():
    # Ask the user for a filename
    filename = input("Enter the filename: ")
    
    try:
        # Try to open the file in read mode
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to start the process
read_file()
