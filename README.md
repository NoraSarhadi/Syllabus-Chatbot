# Syllabus-Chatbot

**Overview:**<br>
This code serves the primary purpose of extracting specific information from the Construction Capstone Project class syllabus. Employing a pattern-matching methodology, the code is intricately designed to navigate the distinctive structure of the syllabus. Key features include identification of professor attendance hours, assignment due dates, absence of class dates, and office locations. To address queries that do not conform to the expected patterns, an error message is displayed, prompting users to ask questions relevant to the chatbot structure. 

**Functionality:**<br>
The code utilizes the nltk library for natural language processing (NLP), employing a fundamental form of pattern matching. The nltk.chat.util.Chat class facilitates the creation of a rule-based chatbot by defining patterns and corresponding responses. It is imperative to note that this approach is tailored to a specific syllabus format, and any deviation may lead to limitations in data extraction.

**External Libraries Used:**<br>
Tkinter: Python's standard GUI (Graphical User Interface) library.<br>
nltk: Natural Language Toolkit library, used for chatbot development.<br>
Flask: A lightweight web application framework for Python.<br>
fitz (PyMuPDF): PyMuPDF library for working with PDF documents.<br>

**Usage Instructions:**<br>
In order to Run the chatbot either manually install the aforementioned libraries or utilize the provided environment YAML file named "nora_env.yml." The latter option offers a streamlined approach, as it automates the installation process for all essential libraries, ensuring a cohesive and efficient setup.
To execute the project successfully, ensure that both the "syllabus_chatbot.py" file and the "BCN 4787C Syllabus with Schedule - Fall 2023 GC.pdf" file are located in the same folder. Initiate the program by running the Python file ("syllabus_chatbot.py").

**Limitations:**<br>
Given time constraints, the code adopts a straightforward pattern-matching strategy, limiting its adaptability to a predefined syllabus structure. In the event of encountering a different syllabus format, the code may not successfully extract the requisite data. While advanced NLP techniques could enhance adaptability, their integration was precluded by time constraints.

**Examples:**

<img width="495" alt="1" src="https://github.com/NoraSarhadi/Syllabus-Chatbot/assets/155926181/f8a07242-03e2-4a23-b95a-f3fa8f5e338d">

<img width="492" alt="2" src="https://github.com/NoraSarhadi/Syllabus-Chatbot/assets/155926181/2cd230e5-0303-4e98-ad6a-dee35ec687b6">
