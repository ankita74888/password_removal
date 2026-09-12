# Password Protected PDF Remover

A Python-based utility that removes password protection from authorized PDF files when the correct password is provided.

## Features

* Remove password protection from PDF files
* Accepts the PDF password securely as user input
* Creates a new unlocked PDF
* Handles incorrect passwords
* Handles missing input files
* Simple command-line interface
* Built entirely with Python

## Technologies Used

* Python 3.11
* pypdf
* pathlib

## Project Structure

```text
password_removal/
│
├── src/
│   ├── __init__.py
│   └── password_remover.py
│
├── input_files/
├── output_files/
│
├── tests/
│   └── test_password_remover.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Go to the project directory:

```bash
cd password_removal
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python main.py
```

The program will ask for:

1. Input PDF path
2. Existing PDF password
3. Output PDF path

Example:

```text
==================================================
     PASSWORD PROTECTED PDF REMOVER
==================================================

Enter input PDF path:
C:\Users\Ankita\Downloads\sample.pdf

Enter PDF password:
********

Enter output PDF path:
C:\Users\Ankita\project\password_removal\output_files\unlocked.pdf

✅ Password protection removed successfully.
```

## Important Note

This project is intended for files that you own or are authorized to modify and requires the correct existing password. It does not attempt to crack, guess, or bypass passwords.

## Future Improvements

* Add a graphical user interface (GUI)
* Support batch PDF processing
* Add drag-and-drop functionality
* Improve logging and error reporting
* Add automated tests
* Add file selection through a GUI

## Author

Ankita

Python Developer | Insurance Domain Professional | Aspiring IT Professional
