import os
import shutil

# Map file extensions to category folders
EXTENSION_MAP = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents", ".xlsx": "Documents",
    ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos",
    ".mp3": "Music", ".wav": "Music",
    ".zip": "Archives", ".rar": "Archives",
}


def get_category(filename):
    _, ext = os.path.splitext(filename)   # splits "photo.jpg" into ("photo", ".jpg")
    ext = ext.lower()
    return EXTENSION_MAP.get(ext, "Others")   # defaults to "Others" if extension not mapped


def organize_folder(target_folder):
    if not os.path.exists(target_folder):
        print(f"Error: Folder '{target_folder}' does not exist.")
        return

    files_moved = 0

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # skip folders, only organize actual files
        if os.path.isdir(file_path):
            continue

        category = get_category(filename)
        category_folder = os.path.join(target_folder, category)

        # create the category folder if it doesn't exist yet
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination = os.path.join(category_folder, filename)

        try:
            shutil.move(file_path, destination)
            print(f"Moved: {filename} -> {category}/")
            files_moved += 1
        except Exception as e:
            print(f"Could not move {filename}: {e}")

    print(f"\nDone. {files_moved} file(s) organized.")


# Run it
folder_to_organize = "messey_folders"   # change this to your actual folder path
organize_folder(folder_to_organize)