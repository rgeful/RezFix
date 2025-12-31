import pymupdf
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.core.config import settings
from app.models.resume import Resume

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    await init_beanie(
        database=client[settings.DATABASE_NAME],
        document_models=[Resume],
    )
    print("Connected to MongoDB")
    yield
    client.close()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "database": "connected"}

@app.post("/api/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()

    with pymupdf.open(stream=content, filetype="pdf") as doc:
        extracted_text = ""
        for page in doc:
            extracted_text += page.get_text()

    new_resume = Resume(
        user_id="some_user",
        original_filename=file.filename,
        extracted_text=extracted_text
    )

    await new_resume.insert()

    return {
        "id": str(new_resume.id),
        "message": "Resume uploaded and text extracted!",
        "preview": extracted_text[:200] + "..."
    }