from fastapi import APIRouter
from backend.models.feedback_schema import FeedbackInput

# For now, store in-memory (in real-world, use DB)
feedback_list = []

router = APIRouter()

@router.post("/feedback")
def submit_feedback(data: FeedbackInput):
    feedback_list.append(data.dict())
    return {"message": "Feedback received", "total_feedback": len(feedback_list)}

@router.get("/feedback")
def get_feedback():
    return feedback_list
