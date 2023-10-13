import os

# Function to search for a file by name (excluding extension) in a specified directory
def search_file_by_name(directory, file_name):
    result = "Not found"

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file_name.lower() == os.path.splitext(file)[0].lower():
                result = os.path.join(root, file)
                break

    return result
