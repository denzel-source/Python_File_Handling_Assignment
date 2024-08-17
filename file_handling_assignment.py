

def create_and_write_file():
    try:
        # Create a new file and open it in write mode
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("Hello, this is the first line.\n")
            file.write("The number is 42.\n")
            file.write("This is the third line with some text.\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def read_and_display_file():
    try:
        # Open the file in read mode
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the file
            file.write("This is an additional line.\n")
            file.write("Appending more content to the file.\n")
            file.write("Final line appended to the file.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")


def main():
    try:
        # Create and write to the file
        create_and_write_file()

        # Read and display the file contents
        read_and_display_file()

        # Append additional lines to the file
        append_to_file()

        # Read and display the file contents again to see the changes
        read_and_display_file()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()


