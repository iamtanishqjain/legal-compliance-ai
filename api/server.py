from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
import shutil
import os
from preprocessing.pdf_to_text import extract_text_from_pdf
from evaluation.run_on_text import run_on_text
from evaluation.metrics import summarize_results, compliance_score
from api.auth import create_access_token, authenticate_user, verify_token


app = FastAPI(title="Legal Compliance AI API")

ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "temp_uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}


@app.post("/analyze")
async def analyze_contract(
    file: UploadFile = File(...),
    user: dict = Depends(verify_token)
):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    raw_text = extract_text_from_pdf(file_path)
    results, final_risk = run_on_text(raw_text)

    summary = summarize_results(results)
    score = compliance_score(summary)

    response = {
        "final_risk": final_risk,
        "compliance_score": score,
        "summary": summary,
        "results": results
    }

    return response
