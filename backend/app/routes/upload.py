from fastapi import APIRouter, UploadFile, File
import pdfplumber
import tempfile

from app.utils.skills import extract_skills
from app.utils.ats import calculate_ats
from app.utils.sections import detect_sections
from app.utils.missing_skills import get_missing_skills
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
    sections = detect_sections(text)
    missing_skills = get_missing_skills(skills)
    ats_result = calculate_ats(skills, sections, text)

    return{
      "filename":file.filename,
      "ats_score":ats_result["score"],
      "score_breakdown":ats_result["breakdown"],
      "skills":skills,
      "missing_skills": missing_skills,
      "sections":sections,
      "preview":text[:500]
}