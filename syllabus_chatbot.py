import tkinter as tk
from tkinter import messagebox
from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request
import fitz  # PyMuPDF library
import re
import os
import sys
import glob

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        pdf_document = fitz.open(pdf_file)
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text += page.get_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    finally:
        pdf_document.close()
    return text


# Create a Tkinter GUI
def send_message():
    user_input = entry.get()
    text_widget.insert(tk.END, f"You: {user_input}\n", "user_question")
    response = chatbot.respond(user_input)
    if not response:
        error_message = "Sorry, at this moment I can only give you information about Office hours, Office location, no class dates, and due dates. Please try a different question."
        text_widget.insert(tk.END, f"Error: {error_message}\n", "error_message")
        # messagebox.showerror("Error", error_message)
    else:
        text_widget.insert(tk.END, f"Chatbot: {response}\n", "chatbot_response")

# Flask web application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return render_template('chat.html', user_input=user_input, response=response)

if __name__ == "__main__":
    # Get PDF file input from the user
    # Course_code = input("Enter the course code: ")
    Course_code = "BCN 4787"
    pdf_file = Course_code + "*.pdf"

    # Use glob to find files that match the pattern
    matching_files = glob.glob(pdf_file)

    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(matching_files[0])

    # Extract attendance hours and due date from the PDF text
    attendance_hours_match = re.search(r'Office hours:\s*([^\n]+)', pdf_text)
    office_location_match = re.search(r'Office Location:\s*([^\n]+)', pdf_text)
    assignment_due_dates_match = re.findall(r'(\d{1,2}/\d{1,2})\s+\([^)]+\)\s+.*?\s+Assignments (\d+)-(\d+) due', pdf_text)
    no_class_match = re.findall(r'(\d{1,2}/\d{1,2})\s+\([^)]+\)\s+.*?No Class', pdf_text)

    # print(attendance_hours_match)
    # print(office_location_match)
    # print(assignment_due_dates_match)
    # print(no_class_match)
    
    # Create a dictionary to store assignment due dates
    assignment_due_dates_dict = {}
    for due_date, start_assignment, end_assignment in assignment_due_dates_match:
        for assignment_number in range(int(start_assignment), int(end_assignment) + 1):
            assignment_key = f'Assignment {assignment_number}'
            assignment_due_dates_dict[assignment_key] = due_date

    extracted_attendance_hours = attendance_hours_match.group(1) if attendance_hours_match else "Not available"
    extracted_office_location = office_location_match.group(1) if office_location_match else "Not available"
    
    # Create chat responses with extracted information
    pairs = [
        (r'Hi', ['Hello, Please ask your question regarding the syllabus']),
        (r'Hello', ['Hello, Please ask your question regarding the syllabus']),
        (r'(.*)not(.*)class(.*)', [f'In the following dates you don\'t have class:\n{", ".join(f"{date}" for date in no_class_match)}']),
        (r'(.*)n\'t(.*)class(.*)', [f'In the following dates you don\'t have class:\n{", ".join(f"{date}" for date in no_class_match)}']),
        (r'(.*)no class(.*)', [f'In the following dates you don\'t have class:\n{", ".join(f"{date}" for date in no_class_match)}']),
        (r'(.*)attendance hour(.*)', [f'Professor\'s office hours: {extracted_attendance_hours}']),
        (r'(.*)office hour(.*)', [f'Professor\'s office hours: {extracted_attendance_hours}']),
        (r'(.*)office(.*)location(.*)', [f'Professor\'s office location: {extracted_office_location}']),
        (r'(.*)due(.*)', [f'Due dates for assignments:\n{", ".join(f"{assignment}: {due_date}" for assignment, due_date in assignment_due_dates_dict.items())}']),
        (r'(.*)assignment(.*)', [f'Due dates for assignments:\n{", ".join(f"{assignment}: {due_date}" for assignment, due_date in assignment_due_dates_dict.items())}']),
    ]


    chatbot = Chat(pairs, reflections)

    # Run the Tkinter GUI
    root = tk.Tk()
    root.title("Syllabus Queries")

    label = tk.Label(root, text="Ask your question:", font=("Helvetica", 16))
    label.pack(pady=20)

    entry = tk.Entry(root, width=50, font=("Helvetica", 14))
    entry.pack(pady=20)

    button = tk.Button(root, text="Get Response", command=send_message, font=("Helvetica", 14))
    button.pack(pady=20)

    # Create a Text widget for displaying the chatbot's responses
    text_widget = tk.Text(root, height=10, width=60, wrap="word", font=("Helvetica", 12))
    
    # Set the background color for the chatbot's responses
    text_widget.configure(bg="lightgray")
    
    text_widget.pack(pady=20)

    # Tag the chatbot's response with the "chatbot_response" tag
    text_widget.tag_configure("user_question", foreground="green")  
    text_widget.tag_configure("chatbot_response", foreground="blue")  
    text_widget.tag_configure("error_message", foreground="red")  

    root.mainloop()

    # Run the Flask web application
    app.run(debug=True)
