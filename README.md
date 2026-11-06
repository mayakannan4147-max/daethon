# Python Practice Project Collection

This repository contains multiple beginner-friendly Python console applications built with the standard library. Each script focuses on a different practical programming concept such as string logic, file handling, CSV export, directory automation, and rule-based conversation logic.

## Included Programs

### 1. Hangman Game
File: `hangman.py`

A terminal-based Hangman game where the player guesses letters to reveal a hidden word before making 6 incorrect guesses.

Features:
- random word selection
- masked word display
- duplicate-letter prevention without penalty
- ASCII gallows updates after each wrong guess
- win/lose screens
- replay option

Run:
```bash
py hangman.py
```

### 2. Portfolio Tracker
File: `portfolio.py`

A simple portfolio tracking utility that stores holdings and calculates current value and gain/loss.

Features:
- stock ticker dictionary
- buy price and share quantity tracking
- market value and percentage gain/loss calculations
- CSV export to `portfolio_summary.csv`
- formatted console summary

Run:
```bash
py portfolio.py
```

### 3. File Organizer
File: `organizer.py`

An automation utility that organizes files in a selected folder by extension into category folders like Documents, Images, Videos, Archives, and Code.

Features:
- extension-to-folder mapping
- automatic folder creation
- safe file moving with collision handling
- permission and OS error handling
- execution summary output

Run:
```bash
py organizer.py
```

You can also pass a target folder as an argument:
```bash
py organizer.py "C:\path\to\folder"
```

### 4. Customer Support Chatbot
File: `chatbot.py`

A rule-based chatbot that responds to user queries about business hours, support, shipping, returns, and pricing.

Features:
- normalized user input
- keyword and regex-based intent matching
- fallback responses for unknown questions
- exit commands: `bye`, `exit`, `quit`
- interactive console chat loop

Run:
```bash
py chatbot.py
```

## Project Structure

```text
daethon/
├── README.md
├── hangman.py
├── portfolio.py
├── portfolio_summary.csv
├── organizer.py
├── chatbot.py
└── .gitignore
```

## Requirements

- Python 3
- Standard library only (`random`, `csv`, `os`, `shutil`, `pathlib`, `re`, `json`)

## Notes

These programs are designed for learning and practice, with simple logic and console-based interfaces. They can be extended with real APIs, external datasets, or GUI improvements.

## How to Use

Open a terminal in the project folder and run any script individually:

```bash
py hangman.py
py portfolio.py
py organizer.py
py chatbot.py
```
