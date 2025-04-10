def read_and_modify_file():
    input_filename = input("Enter the filename to read from: ")

    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\n File read successfully!")

        # Modify content (you can change this logic as needed)
        modified_content = content.upper()

        # Create a new filename for the modified version
        output_filename = f"modified_{input_filename}"

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f" Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print(" Error: File not found.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
