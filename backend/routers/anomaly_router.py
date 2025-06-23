from fastapi import APIRouter, UploadFile, File
from backend.services.anomaly_detector import detect_anomalies

router = APIRouter()

@router.post("/anomaly")
async def detect_anomaly_route(file: UploadFile = File(...)):
    content = await file.read()
    anomalies = detect_anomalies(content)
    return {"anomalies": anomalies, "count": len(anomalies)}
