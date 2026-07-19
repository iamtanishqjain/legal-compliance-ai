# Legal Compliance AI

### AI-Assisted Contract Compliance Pre-Screening | Tanishq Jain

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![React](https://img.shields.io/badge/Frontend-React_%2B_Vite-61DAFB?logo=react)
![Sentence Transformers](https://img.shields.io/badge/NLP-MiniLM_Embeddings-informational)
![Eval](https://img.shields.io/badge/Eval_Accuracy-65%25_(13%2F20)-yellow)
![Docker](https://img.shields.io/badge/Container-Docker_Ready-2496ED?logo=docker)

---

## About This Project

Legal Compliance AI pre-screens employment contracts against labour-law obligations
and flags where a contract falls short — **before** a human lawyer ever has to read
the full document. It's a decision-support tool, not a legal opinion: every finding
comes with a plain-language explanation and a flag for whether it needs manual review.

**Scope:** Employment contracts under Indian labour law. Given a contract PDF, the
system checks it against a set of legal obligations (minimum wage, working hours,
termination notice, leave policy) and produces a per-obligation risk report.

---

## How It Works

```
PDF upload
   │
   ▼
pdf_to_text (pdfplumber) ──▶ text_cleaner ──▶ sentence_splitter (spaCy)
                                                       │
regulation_loader ──▶ labour_obligations.json         │
                          │                            │
                          ▼                            ▼
              clause_matching (sentence-transformers: all-MiniLM-L6-v2)
                          │
                          ▼
              risk_engine (similarity + keyword coverage + criticality)
                          │
                          ▼
              explainability (per-finding, human-readable rationale)
                          │
                          ▼
              JSON risk report ──▶ React dashboard
```

**Risk scoring** combines two signals per obligation:
- **Semantic similarity** — cosine similarity between contract sentences and the
  obligation's description, via a MiniLM sentence-transformer (threshold 0.45)
- **Keyword coverage** — fraction of the obligation's required keywords actually
  present in the matched sentence

These are weighted by the obligation's criticality (HIGH obligations weight
similarity less, coverage more) and banded into LOW / MEDIUM / HIGH risk. Any
HIGH-risk finding is always flagged for manual review, regardless of confidence —
a HIGH-risk finding is never allowed to slip through silently.

---

## Validation

Ran against 5 synthetic test contracts (20 obligation checks total,
`evaluation/evaluate_system.py`):

| Metric | Result |
|---|---|
| Correct detections | 13 / 20 |
| False positives | 2 |
| False negatives | 0 |
| Ambiguous (no ground truth) | 5 |

Zero false negatives is the more important number here — the system never misses
an obligation that's actually present in the test set, which matters more than
precision for a pre-screening tool (a human reviews anything it flags anyway).

---

## Repository Structure

```
legal-compliance-ai/
│
├── frontend/                React + Vite + Tailwind — login, upload, risk dashboard
│
├── api/
│   ├── server.py            FastAPI app — /token (login), /analyze (PDF upload)
│   └── auth.py               JWT auth, bcrypt password hashing
│
├── preprocessing/            PDF → text → cleaned → sentences (pdfplumber + spaCy)
├── regulation_engine/         Loads labour_obligations.json
├── clause_matching/
│   ├── semantic_matcher.py   MiniLM sentence-transformer matching (used in prod)
│   └── baseline_tfidf.py     TF-IDF baseline (used by the legacy Streamlit UI)
├── risk_engine/               Risk scoring, confidence, manual-review rules
├── explainability/            Human-readable explanations per finding
│
├── evaluation/
│   ├── run_on_text.py         Shared pipeline entry point (used by API + CLI)
│   ├── evaluate_system.py     Accuracy eval against labeled test contracts
│   ├── run_portfolio.py       Batch-analyze every contract in data/contracts/
│   └── report_generator.py    Writes JSON reports to outputs/
│
├── data/
│   ├── regulations/labour_obligations.json   The 4 obligations checked against
│   └── contracts/test_contracts.json          Labeled test set for evaluation
│
├── ui/app.py                  Legacy Streamlit prototype (TF-IDF baseline)
├── Dockerfile                  Backend container definition
└── render.yaml                 Render blueprint config (see Deployment notes below)
```

---

## Running Locally

**Backend**
```bash
python -m venv .venv
.venv/Scripts/activate       # or source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn api.server:app --reload
```

**Frontend**
```bash
cd frontend
npm install
cp .env.example .env         # points at http://localhost:8000 by default
npm run dev
```

Open the printed local URL, sign in with `admin` / `admin123`, and upload an
employment contract PDF.

---

## Deployment Notes

The app is containerized and deploy-ready (`Dockerfile`, `render.yaml`,
`frontend/vercel.json`), but currently runs locally rather than on a public URL.

The backend's ML stack (torch + sentence-transformers + spaCy) needs roughly
600MB-1GB of RAM at idle, which exceeds the free tier on most PaaS platforms
(Render free tier caps at 512MB; Hugging Face Spaces now requires a paid plan
for Docker SDK). A production deploy would need either a paid instance
(e.g. Render Starter, ~$7/mo) or a platform with a generous free compute tier
(e.g. Google Cloud Run).

- **Backend** — `uvicorn api.server:app`, containerized via `Dockerfile`.
  Needs `JWT_SECRET_KEY` and `ALLOWED_ORIGINS` env vars set for a real deploy.
- **Frontend** — static Vite build, deployable as-is to Vercel/Netlify once
  `VITE_API_URL` points at a live backend.

---

## Tech Stack

- **Backend:** FastAPI, python-jose (JWT), bcrypt, pdfplumber, spaCy, sentence-transformers, scikit-learn
- **Frontend:** React, Vite, Tailwind CSS
- **Model:** `all-MiniLM-L6-v2` (sentence-transformers)
- **Containerization:** Docker

---

## Author

**Tanishq Jain**
B.Tech Computer Science (AI & ML), 3rd Year
