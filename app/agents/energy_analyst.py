from pydantic import BaseModel
from typing import List, Optional

class AnalysisRequest(BaseModel):
    region: str
    time_range: str
    question: str

class AnalysisResponse(BaseModel):
    region: str
    time_range: str
    metrics: LoadPriceMetrics
    summary: str
    notes: List[str] = []

