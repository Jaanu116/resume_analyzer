from fastapi import APIRouter, UploadFile, File
import pdfplumber
import tempfile

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    # create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:

        content = await file.read()

        temp.write(content)

        temp_path = temp.name


    text=""

    with pdfplumber.open(temp_path) as pdf:

        for page in pdf.pages:

            page_text=page.extract_text()

            if page_text:
                text += page_text


    return {

        "filename":file.filename,

        "preview":text[:500]
    }