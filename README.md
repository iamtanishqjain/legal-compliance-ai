# Legal Compliance AI

An AI-assisted system that pre-screens employment contracts (India) for labour-law
compliance risks, using sentence-embedding similarity against a set of legal
obligations. It flags risk levels (LOW/MEDIUM/HIGH), explains why, and marks
findings that need human review — a decision-support tool, not a legal opinion.

## Architecture

```
frontend/   React + Vite + Tailwind — the web UI
api/        FastAPI backend (JWT auth + /analyze endpoint)
clause_matching/     Sentence-transformer semantic matching
risk_engine/         Risk scoring, confidence, manual-review rules
explainability/       Human-readable explanations per finding
preprocessing/         PDF → text → sentences
regulation_engine/    Loads the obligations to check against
evaluation/            CLI tools: batch runner, accuracy eval, report generator
```

## Running locally

**Backend**
```bash
python -m venv .venv
.venv/Scripts/activate      # or source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn api.server:app --reload
```

**Frontend**
```bash
cd frontend
npm install
cp .env.example .env        # points at http://localhost:8000 by default
npm run dev
```

Open the printed local URL, sign in with `admin` / `admin123`, and upload an
employment contract PDF.

## Deployment

- **Backend** — deploy `Dockerfile` to [Render](https://render.com) (see `render.yaml`)
  or any Docker host. Set `JWT_SECRET_KEY` and `ALLOWED_ORIGINS` env vars.
- **Frontend** — deploy the `frontend/` folder to [Vercel](https://vercel.com).
  Set `VITE_API_URL` to your deployed backend URL.

## Scope

- Employment contracts (India)
- Labour law compliance
- Human-in-the-loop decision support
- Risk scoring (not legal judgment)
