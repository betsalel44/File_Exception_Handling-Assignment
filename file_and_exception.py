def modify_content(content):
    """
    Example modification: convert text to uppercase.
    You can change this function to apply any modification you like.
    """
    return content.upper()


def main():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to read the file
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8") as file:
            file.write(modified_content)

        print(f"Modified file has been saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
