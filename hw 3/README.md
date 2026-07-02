homework 3 : working with CSV 

You are given a text file named std_info_4042.txt that contains student information for a specific term. The file is structured as follows: First row (Header): Contains the column captions: std_id, name, advanced_programming, data_structure, mathematics2, physic2 Rows 2 to 31: Contain information for exactly 30 students, with each field separated by commas. Your task is to write a Python program that processes this data and performs the following operations. Open and read the std_info_4042.txt file and store all student dictionaries in a list. Example:
 "std_id': '123456' name': 'John Doe' advanced_programming': "18.5', data structure': '17.0' mathematics2': '19.5° physic2": '16.5
 more students
Homework (Cont.)
• Write the data to a CSV file with the same name (std_info_4042.csv) Include the headers in the first row • Preserve the data structure exactly as in the original file • Ensure proper CSV formatting (commas, quotes if needed) • Please Send me python code, text file, and csv file created as result of your code
 Hints
• Use csv module for CSV operations
• Consider using strip() to clean whitespace
• Remember that grades might be stored as strings or floats • The with open() statement ensures proper file closing
 • Use DictWriter to write dictionary to csv file