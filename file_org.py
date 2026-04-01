import shutil
from pathlib import Path

folder = Path.home() / "Desktop" / "test_folder"

def make_directory(destination):
    destination.mkdir(parents=True, exist_ok=True)

def move_files(item, destination):
    shutil.move(str(item), str(destination / item.name))

for item in folder.iterdir():
    if item.is_file():
        ext = item.suffix.lower()

        if ext == ".pdf":
            destination = folder / "PDFs"
        elif ext in [".jpg", ".jpeg"]:
            destination = folder / "Images"
        elif ext in [".mp4", ".mov"]:
            destination = folder / "Videos"
        elif ext in [".docx", ".docs"]:
            destination = folder / "Documents"
        else:
            destination = folder / "Others"

        make_directory(destination)
        move_files(item, destination)

print("All files are moved successfully")