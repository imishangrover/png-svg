import uuid
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_upload_file(upload_file):
    file_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{file_id}.png"

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path
