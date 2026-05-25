from fastapi import APIRouter, UploadFile, File
import pdfplumber
import tempfile

from app.utils.skills import extract_skills
from app.utils.score import calculate_score
router = APIRouter()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:

        content = await file.read()

        temp.write(content)

        temp_path = temp.name


    text = ""

    with pdfplumber.open(temp_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text


    skills = extract_skills(text)
    ats_score = calculate_score(skills)

    return {
        "filename": file.filename,
        "ats_score": ats_score,
        "skills": skills,
        "preview": text[:500]
    }