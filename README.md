# File Organizer Tool

A simple Python automation script that organizes files in a selected folder into category-based subfolders.

## Features

- Opens a folder picker so you can choose the target folder
- Automatically scans all files inside that folder
- Sorts files into separate folders based on extension
- Creates destination folders automatically if they do not already exist
- Moves files into:
  - `PDFs`
  - `Images`
  - `Videos`
  - `Documents`
  - `Others`

## File Categories

This script currently organizes files using these rules:

- `.pdf` → `PDFs`
- `.jpg`, `.jpeg`, `.png` → `Images`
- `.mp4`, `.mov` → `Videos`
- `.docx`, `.docs`, `.csv` → `Documents`
- Any other file type → `Others`  [oai_citation:1‡GitHub](https://github.com/Shree927432/File_organizer_tool/blob/main/file_org.py)

## Tech Used

- Python
- `pathlib`
- `shutil`
- `tkinter`  [oai_citation:2‡GitHub](https://github.com/Shree927432/File_organizer_tool/blob/main/file_org.py)

## How It Works

1. The script opens a folder selection dialog.
2. You choose the folder you want to organize.
3. The script checks each file in that folder.
4. Based on the file extension, it creates a matching category folder.
5. The file is moved into the correct folder.
6. When complete, it prints: `All files are moved successfully`.  [oai_citation:3‡GitHub](https://github.com/Shree927432/File_organizer_tool/blob/main/file_org.py)

## How to Run

```bash
python file_org.py
