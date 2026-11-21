# Python Password Manager

A desktop password management application built using **Python and CustomTkinter**. The application allows users to save website credentials locally, search for previously stored passwords, and generate random passwords through a graphical user interface.

## Overview

This project is a locally running password manager developed using Python.

The idea behind it was to create a simple desktop application that could store website login credentials, make retrieving saved passwords easier, and generate random passwords without relying on an online password management service.

The application uses JSON files to store saved credentials locally on the computer. It also integrates clipboard functionality to make copying generated and stored passwords more convenient.

The project was developed as a practical exercise in Python GUI development, working with JSON data, file handling, and integrating external Python libraries.

<img width="384" height="240" alt="passwordmanager" src="https://github.com/user-attachments/assets/47c7c412-0801-45d7-b4ce-ad9c215d98eb" />

## Features

- **Save Credentials:** Store website names, email addresses/usernames, and passwords locally.
- **Search Credentials:** Retrieve previously saved login details by entering a website name.
- **Password Generator:** Generate random passwords containing uppercase and lowercase letters, numbers, and special characters.
- **Clipboard Integration:** Automatically copy generated passwords and retrieve saved passwords to the clipboard.
- **Persistent Storage:** Save credentials in a local JSON file so they remain available between application sessions.
- **Graphical User Interface:** Interact with the application through a desktop interface built using CustomTkinter.
- **Input Validation:** Prevent saving entries with missing website names, usernames, or passwords.
- **Confirmation Dialogues:** Ask users to confirm their credentials before saving them.

## Technologies Used

- **Python 3** – Main programming language.
- **CustomTkinter** – Desktop graphical user interface.
- **Tkinter** – GUI functionality and message boxes.
- **JSON** – Local storage and retrieval of saved credentials.
- **Pyperclip** – Clipboard integration.
- **Pillow (PIL)** – Image handling.

## Application Structure

```text
python-password-manager/
│
├── main.py
├── logo.png
├── README.md
├── requirements.txt
└── .gitignore
```

The application also generates a `Password File.json` file when credentials are saved for the first time.

## How It Works

### 1. Saving Passwords

Users enter a website name, email address or username, and password.

After clicking the Add button, the application displays a confirmation dialogue before saving the information into a local JSON file.

### 2. Searching for Passwords

Users can enter a previously saved website name and click Search.

The application retrieves the associated username and password from the JSON file, displays the credentials, and automatically copies the password to the clipboard.

### 3. Generating Passwords

The password generator creates random passwords using a combination of:

- Uppercase and lowercase letters.
- Numbers.
- Special characters.

The generated password is automatically inserted into the password field and copied to the clipboard.

## Installation & Usage

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/python-password-manager.git
```

**2. Navigate into the project directory**

```bash
cd python-password-manager
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python main.py
```

**5. Start managing your credentials**

Use the graphical interface to save, search, and generate passwords.

## Security Considerations

**Important:** This project was developed as a learning exercise and is not intended for storing real or sensitive passwords.

- Passwords are stored locally in plain text within a JSON file.
- No encryption or master-password protection is implemented.
- The password generator uses Python's standard `random` module rather than a cryptographically secure random number generator.
- Passwords copied to the clipboard may remain accessible to other applications.

For these reasons, this application should only be used with dummy credentials or for demonstration purposes.

## Project Background

This project was developed to explore Python desktop application development and the practical use of file handling, JSON data storage, and external libraries.

It provided an opportunity to combine several Python concepts into one functional application, including GUI development, data persistence, random password generation, and clipboard integration.
