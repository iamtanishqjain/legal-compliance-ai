from fastapi import FastAPI, UploadFile, File
import shutil
import os
from evaluation.run_on_text import run_on_text
from evaluation.metrics import summarize_results, compliance_score
from fastapi import Depends, HTTPException
from api.auth import (
    create_access_token,
    authenticate_user,
    verify_token
)


app = FastAPI(title="Legal Compliance AI API")

UPLOAD_FOLDER = "temp_uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/analyze")
async def analyze_contract(
    file: UploadFile = File(...),
    user: dict = Depends(verify_token)
):


    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results, final_risk = run_on_text(file_path)

    summary = summarize_results(results)
    score = compliance_score(summary)

    response = {
        "final_risk": final_risk,
        "compliance_score": score,
        "summary": summary,
        "results": results
    }

    return response
