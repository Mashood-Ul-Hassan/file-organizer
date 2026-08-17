# 📂 File Organizer

A Python automation tool that organizes files into categorized folders based on their file extensions.

Instead of manually sorting files, this script automatically identifies each file type and moves it into an appropriate category such as **Images, Documents, Videos, Music, Archives,** or **Others**.

## 📌 Overview

The File Organizer is a simple Python automation project designed to demonstrate file-system operations and automation.

The program scans a target folder, identifies files based on their extensions, creates category folders when necessary, and moves the files into their corresponding categories.

## ✨ Features

* 📂 Automatically organizes files
* 🖼️ Supports common image formats
* 📄 Supports common document formats
* 🎬 Supports video files
* 🎵 Supports audio files
* 📦 Supports archive files
* 📁 Automatically creates category folders
* 🔄 Moves files using Python's file-system utilities
* ❓ Places unsupported file types into an `Others` folder
* ⚠️ Handles file-movement errors

## 🗂️ Supported File Types

| Category     | Extensions                       |
| ------------ | -------------------------------- |
| 🖼️ Images   | `.jpg`, `.jpeg`, `.png`, `.gif`  |
| 📄 Documents | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| 🎬 Videos    | `.mp4`, `.mov`, `.avi`           |
| 🎵 Music     | `.mp3`, `.wav`                   |
| 📦 Archives  | `.zip`, `.rar`                   |
| 📁 Others    | Any unsupported extension        |

## 🛠️ Technologies Used

* **Python**
* **os**
* **shutil**

The project uses only Python's built-in libraries, so no external packages are required.

## 📁 Project Structure

```text
File_Organizer/
│
├── File_organizer.py
├── messey_folders/
│   ├── Images/
│   ├── Documents/
│   ├── Videos/
│   ├── Music/
│   ├── Archives/
│   └── Others/
│
├── README.md
└── .gitignore
```

## ▶️ How to Run

Navigate to the project directory:

```bash
cd File_Organizer
```

Run the Python script:

```bash
python File_organizer.py
```

The script will organize the files inside:

```text
messey_folders
```

## ⚙️ Change the Target Folder

The target folder is defined near the bottom of `File_organizer.py`:

```python
folder_to_organize = "messey_folders"
```

You can change this to another folder path if required.

For example:

```python
folder_to_organize = "Downloads"
```

Or use an absolute path:

```python
folder_to_organize = "/Users/yourname/Downloads"
```

## 🔄 How It Works

1. The program checks whether the target folder exists.
2. It scans the files inside the folder.
3. File extensions are extracted using `os.path.splitext()`.
4. The extension is matched against the category mapping.
5. A category folder is created if it doesn't already exist.
6. The file is moved into the appropriate category folder using `shutil.move()`.
7. Unsupported file types are placed in `Others`.
8. The program displays the number of files organized.

### Example

Before running:

```text
messey_folders/
├── photo.jpg
├── assignment.pdf
├── movie.mp4
├── song.mp3
└── archive.zip
```

After running:

```text
messey_folders/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── assignment.pdf
├── Videos/
│   └── movie.mp4
├── Music/
│   └── song.mp3
└── Archives/
    └── archive.zip
```

## 📚 Learning Objectives

This project demonstrates practical Python concepts including:

* File and directory handling
* `os` module
* `shutil` module
* Functions
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* File extensions
* Basic automation

## ⚠️ Important

The program **moves files** from the target folder into category folders. Make sure you select the correct folder before running it.

It is recommended to test the program with copies of files first.

## 🚀 Future Improvements

Possible improvements include:

* Add a graphical user interface (GUI)
* Add more file extensions
* Support custom categories
* Add duplicate-file handling
* Add logging
* Allow users to select folders through a GUI
* Add a dry-run mode before moving files

## 👨‍💻 Author

**Mashood Ul Hassan**

Computer Science Student | Python | Data Science & AI Enthusiast
