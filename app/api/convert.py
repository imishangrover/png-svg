from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_utils import save_upload_file
from app.services.preprocess import preprocess_image
from app.services.vectorize import vectorize_bitmap
from app.services.svg_writer import save_svg
from pathlib import Path

router = APIRouter(prefix="/convert", tags=["Converter"])

@router.post("/")
async def convert_png_to_svg(file: UploadFile = File(...)):
    if file.content_type != "image/png":
        raise HTTPException(status_code=400, detail="Only PNG files allowed")

    image_path = save_upload_file(file)

    bw_image = preprocess_image(image_path)

    vector_path = vectorize_bitmap(bw_image)

    output_svg = Path("uploads") / f"{image_path.stem}.svg"
    save_svg(vector_path, output_svg)

    return {
        "status": "success",
        "svg_path": str(output_svg)
    }
