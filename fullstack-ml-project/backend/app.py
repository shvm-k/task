from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from extract_pdf import extract_text_from_pdf

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to restrict access in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        content = await file.read()
        with open("temp.pdf", "wb") as f:
            f.write(content)
        extracted_data = extract_text_from_pdf("temp.pdf")
        return {"success": True, "data": extracted_data}
    except Exception as e:
        return {"success": False, "error": str(e)}
