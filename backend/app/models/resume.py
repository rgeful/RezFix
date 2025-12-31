from beanie import Document
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Resume(Document):
    user_id: str
    original_filename: str
    extracted_text: str
    ats_score: Optional[float] = None
    diagnostics: Optional[dict] = None
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "resumes"

class DiagnosticIssue(BaseModel):
    label: str
    details: str
    severity: str

class ResumeDiagnostics(BaseModel):
    ats_score: int
    missing_keywords: List[str]
    suggested_fixes: List[DiagnosticIssue]
