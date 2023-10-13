#Prerequisite: Run the script
#                   py -m pip install SpeechRecognition
#                   py -m pip install spacy
#                   py -m spacy download en_core_web_sm

import os
import NLP
import FileHandling

while True:
    query = input("Enter a query with file names (e.g., 'Find the Word document called Report'): ")

    found_files = NLP.process_query(query)

    if found_files:
        print("Found the following files:")
        for file in found_files:
            print(file)
    else:
        print("No matching files found.")