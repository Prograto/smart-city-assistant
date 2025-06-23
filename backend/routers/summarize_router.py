from fastapi import APIRouter
from backend.models.summary_schema import SummaryInput
from backend.services.summarizer_model import summarize_text

router = APIRouter()

@router.post("/summarize")
def summarize_text_endpoint(data: SummaryInput):
    result = summarize_text(data.text)
    return {"summary": result}
