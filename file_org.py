import shutil
from pathlib import Path

folder = Path.home() / "Desktop" / "test_folder"



for item in folder.iterdir():
    if item.is_file():
        if item.suffix.lower() in [".pdf"]:
            pdf_folder = folder / "PDFs"
            pdf_folder.mkdir(exist_ok= True)
            shutil.move(str(item),str(pdf_folder/item.name))
        
        elif item.suffix.lower() in ['.jpg',".jpeg"]:
            img_folder = folder / "Images"
            img_folder.mkdir(exist_ok = True)
            shutil.move(str(item),str(img_folder/item.name))

        elif item.suffix.lower() in [".mp4",".mov"] :
            video_folder = folder / "Videos"
            video_folder.mkdir(exist_ok=True)
            shutil.move(str(item),str(video_folder/item.name))

        elif item.suffix.lower() in [".docx",".docs"]:
            doc_folder = folder / "Documents"
            doc_folder.mkdir(exist_ok=True)
            shutil.move(str(item),str(doc_folder/item.name))

        else:
            other_folder = folder / "Other"
            other_folder.mkdir(exist_ok=True)
            shutil.move(str(item),str(other_folder/item.name))


print("All files are moved successfully")