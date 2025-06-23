from fastapi import APIRouter, UploadFile, File
from backend.services.vector_store import VectorSearchEngine

router = APIRouter()
engine = VectorSearchEngine()
uploaded_texts = []

@router.post("/upload-policy")
async def upload_policy_file(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    uploaded_texts.append(text)
    engine.build_index(uploaded_texts)
    return {"message": "Policy uploaded and indexed."}

@router.get("/search-policy")
def search_policy(query: str):
    results = engine.search(query)
    return {"result": results[0] if results else "No match found."}
