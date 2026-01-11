# CA4 – Flask Web Application Demonstrating 5 OWASP Top 10 Vulnerabilities

## Project Description
This project is a deliberately vulnerable **Flask-based web application** developed as part of the **CA4 Ethical Hacking assignment**.

The application demonstrates **five selected vulnerabilities from the OWASP Top 10 list** for educational and demonstration purposes.  
The vulnerabilities are intentionally implemented to understand how real-world web applications can be attacked.


## Vulnerabilities Implemented
The following OWASP Top 10 vulnerabilities are demonstrated in this project:

1. **SQL Injection**  
   - Login authentication bypass using malicious SQL queries.

2. **Cross-Site Scripting (XSS)**  
   - Execution of injected JavaScript code through unsanitized user input.

3. **Broken Authentication**  
   - Direct access to admin page without any login or session validation.

4. **Sensitive Data Exposure**  
   - User credentials (username and password) stored and displayed in plain text.

5. **Security Misconfiguration**  
   - Debug mode enabled, exposing internal stack traces and application details during errors.

## Technologies Used
- Python 3
- Flask (Web Framework)
- SQLite (Database)
- HTML
- CSS

## Project Structure


## Setup Instructions

1. Install Python (version 3.x)
2. Install Flask using pip:
3. Navigate to the project folder.

## Database Setup

Run the database creation script:

This will create the SQLite database file (`database.db`).

## How to Run the Application

Start the Flask server:
Open a web browser and visit:  http://localhost:5000

