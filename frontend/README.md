## RezFix.ai

The Precision Resume Fixer. Rezfix.ai diagnoses resume issues and provides surgical AI rewrites
to match specific job descriptions without the bloat of a full builder.

## Prerequisites:
- Node.js (v18+)
- Python (3.10+)
- MongoDB (Local or Atlas)

## Tech Stack:
- **Frontend**: Vite + React + TypeScript + Tailwind CSS
- **Backend**: FastAPI (Python)
- **Database**: MongoDB (Beanie ODM)
- **Auth**: Clerk (Google Auth)
- **AI**: GPT-4o

## Key Features (MVP):
- **Instant Diagnosis**: ATS match scoring and keyword gap analysis.
- **Surgical Rewriting**: One-click AI improvements for specific bullet points.
- **PDF Preservation**: Maintain your original layout while improving content.

Setup Backend:
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # Add your OpenAI & Mongo keys
fastapi dev main.py

Setup Frontend:
cd frontend
npm install
cp .env.example .env.local # Add VITE_API_URL=http://localhost:67
npm run dev