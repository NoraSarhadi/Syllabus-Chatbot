# Syllabus-Chatbot

**Overview**

This documentation provides a comprehensive guide to the Python codebase designed to process natural language using the NLTK library. The primary objective of this code is to provide specific information about the Construction Capstone Project class from the syllabus text. This simple method involves pattern matching, and the code is tailored to a specific syllabus structure. The code identifies specific patterns within the syllabus text, such as: professor attendance hours, assignment due dates, no Class  date, and office Location. To address queries that do not conform to the expected patterns, an error message is displayed, prompting users to ask questions relevant to the chatbot structure. 

**Code Structure**

The codebase is organized into the following main files:
main.py: The main entry point for the program.
syllabus_processor.py: Contains the core functionality for processing syllabus text.
chatbot.py: Implements a simple chatbot for interacting with users.

**Dependencies**

The code relies on the following external libraries:
NLTK (Natural Language Toolkit): Used for natural language processing tasks.

Ensure that these libraries are installed before running the code.

**Execution**

To run the project successfully, both the “syllabus_chatbot.py” file and the “BCN 4787C Syllabus with Schedule - Fall 2023 GC.pdf” file must be in the same folder. 
Execute the py file to initiate the program.

**Limitation**

Due to time constraints, a straightforward pattern-matching approach was adopted and has limitations, as it is specifically tailored to a certain syllabus format. If a different syllabus structure is encountered, the code may not successfully extract the required data. Advanced natural language processing techniques could be used to make the code adaptable to various syllabus structures but I didn’t have enough time for that.
