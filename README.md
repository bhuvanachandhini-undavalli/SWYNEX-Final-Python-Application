# SWYNEX-Final-Python-Application
A Python-based Student Report Management System with input validation, grade calculation, and error handling.
SWYNEX Final Python Application

Student Report Management System

A beginner-friendly Python application that manages student reports, validates subject marks, calculates totals and averages, and assigns grades.

Features

- Add student reports.
- Validate student names and subject marks.
- Calculate total marks and average percentage.
- Assign grades automatically.
- View multiple student reports during a session.
- Handle invalid numeric input and menu choices.

Requirements

- Python 3.8 or later
- No external Python packages required

Installation and Setup

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the application using:

python main.py

If your system uses the "python3" command, run:

python3 main.py

How to Use

1. Run "main.py".
2. Select option "1" to add a student report.
3. Enter the student's name.
4. Enter marks for three subjects, each between 0 and 100.
5. Select option "2" to view reports.
6. Select option "3" to exit.

Grade Criteria

Average| Grade
90–100| A
75–89.99| B
60–74.99| C
40–59.99| D
Below 40| F

Data Storage

Student reports are stored in memory while the application is running. Records are not saved permanently after the program exits.

Error Handling

The application handles invalid numeric input, marks outside the accepted range, empty student names, and invalid menu choices.

Author

SWYNEX Internship Task 4