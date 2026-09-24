<div align="center">

# 💌 Automated Invitation Generator
*“Because writing individual invites by hand is a crime! 🛑✉️”*

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

</div>

---

### 🚀 About The Project
A smart and clean Python automation script designed to save time and effort! Instead of writing individual invitation letters manually for every single person, this script takes a template letter and a list of names, then performs a fully automated **Mail Merge** to generate a customized invitation for each person in seconds. ✨

---

### 📂 Project Structure
Organization is half the battle! Here is how the project files and folders are structured:

```text
invitations/
│
├── input/
│   ├── Letters/
│   │   └── starting_letter.txt   # Base template letter with placeholders
│   └── Names/
│       └── invited_names.txt     # List of recipient names to process
│
├── output/
│   └── Ready_to_send/            # Output: Generated personalized invitation files ready to send
│
└── main.py                       # Core Python automation script




⚙️ How It Works
Reads recipient names line by line from the input file using Python file I/O operations (readlines()).

Loads the content of the base template letter.

Dynamically replaces placeholders (like {name} and {signature}) for each individual.

Saves a unique, personalized text file for every recipient into the output directory.

🛠️ Tech Stack
Language: Python 🐍

Concepts: File Handling (open, read, readlines), String Manipulation (replace, strip), Path Automation.

💡 Summary
A small project, but it solves a real-world repetitive task with clean and professional code. If you like this project, don't forget to give it a ⭐ on GitHub!
