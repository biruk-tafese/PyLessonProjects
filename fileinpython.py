def write_to_file(file_path,data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Sucessfully written to {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(f"Data read from {file_path}: {data}")
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"Error reading form file: {e}")
        return None
    

if __name__ == "__main__":
    file_path = 'example.txt'
    data_to_write="Hello, this is sample text from Biruk tafese"


    # Writing to the file
    write_to_file(file_path, data_to_write)

    # Reading from the file
    read_data = read_from_file(file_path)

    # Example of handling non-existent file
    non_existent_file_path = "non_existent.txt"
    read_from_file(non_existent_file_path)
