# Python Password Manager

A desktop-based password manager built using Python, Tkinter and CustomTkinter. The application allows users to save website login credentials locally, retrieve previously saved passwords, and generate random passwords.

The project was developed as a practical exercise in Python GUI development, file handling, JSON data storage, and working with external libraries.

## Features

- **Save Passwords:** Store website names, email addresses/usernames, and passwords locally in a JSON file.
- **Password Search:** Search for saved credentials using the associated website name.
- **Clipboard Integration:** Automatically copy retrieved passwords to the clipboard when searching for saved credentials.
- **Password Generator:** Generate random passwords containing uppercase and lowercase letters, numbers, and special characters.
- **Automatic Data Storage:** Save and update credentials in a local JSON file, allowing information to persist between application sessions.
- **Input Validation:** Prevent saving entries when required fields are left empty.
- **Confirmation Dialogues:** Display entered credentials for confirmation before saving them.

<img width="384" height="240" alt="passwordmanager" src="https://github.com/user-attachments/assets/47c7c412-0801-45d7-b4ce-ad9c215d98eb" />

## Technologies & Libraries

- **Python** – Core programming language.
- **Tkinter** – GUI development.
- **CustomTkinter** – Enhanced GUI widgets and interface styling.
- **JSON** – Local data storage and retrieval.
- **Pyperclip** – Clipboard functionality.
- **Pillow** – Image library dependency.

## Project Structure

```text
Python-Password-Manager/
│
├── main.py
├── logo.png
├── requirements.txt
├── .gitignore
└── README.md
```

`Password File.json` is automatically created when credentials are saved for the first time. It is not included in the GitHub repository.

## Installation & Setup

1. Clone this repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Python-Password-Manager
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

   Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## How It Works

The application uses a graphical interface to collect website names, usernames/email addresses, and passwords.

When a user saves credentials, the application checks whether a JSON file already exists. If it does, the new entry is added to the existing data. Otherwise, a new JSON file is created.

The search functionality retrieves credentials using the website name as the lookup key. Retrieved passwords are automatically copied to the clipboard for convenience.

The password generator creates random passwords by combining letters, numbers, and special characters before shuffling them into a single string.

## Security Considerations & Limitations

This project was developed as a Python programming and GUI development exercise rather than a production-ready security application.

- Passwords are stored locally in a JSON file in plain text.
- No encryption or password-protection mechanism is implemented.
- The password generator uses Python's `random` module rather than a cryptographically secure random number generator.
- Clipboard contents are not automatically cleared after copying a password.

**Important:** This application is intended for educational and demonstration purposes. It should not be used to store real or sensitive account credentials.

## Learning Outcomes

Through this project, I gained practical experience with:

- Developing desktop applications using Python.
- Creating interactive GUI elements and handling user input.
- Reading, writing, and updating JSON files.
- Implementing search functionality using dictionary lookups.
- Generating random passwords using Python's built-in modules.
- Integrating external libraries and clipboard functionality.
- Handling exceptions and validating user input.

