from pydantic import BaseModel

class FeedbackInput(BaseModel):
    name: str
    category: str
    message: str
