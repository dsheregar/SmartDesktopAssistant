#Prerequisite: Run the script
#                   py -m pip install spacy
#                   py -m spacy download en_core_web_sm

import spacy
import FileHandling

# Initialize spaCy with the English language model
nlp = spacy.load("en_core_web_sm")

# Function to extract file names from a user's query
def extract_file_name(query):
    doc = nlp(query)

    # Initialize an empty list to store extracted file names
    file_names = []

    for token in doc:
        if token.ent_type_ == "FILE_NAME":
            # Add the extracted file name (excluding the extension) to the list
            file_names.append(token.text.split('.')[0])

    return file_names

# Function to process the user's query and search for files
def process_query(query):
    file_names = extract_file_name(query)
    found_files = []

    for file_name in file_names:
        result = FileHandling.search_file_by_name("C:\\", file_name)  # Change the directory as needed
        if result != "Not found":
            found_files.append(result)

    return found_files