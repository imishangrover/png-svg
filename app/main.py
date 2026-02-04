from fastapi import FastAPI
from app.api.convert import router as convert_router

app = FastAPI(title="PNG to SVG Converter")

app.include_router(convert_router)

@app.get("/")
def health_check():
    return {"status": "API running"}
