from fastapi import APIRouter, UploadFile, File
from backend.services.forecast_model import forecast_kpi

router = APIRouter()

@router.post("/forecast")
async def forecast_kpi_route(file: UploadFile = File(...)):
    content = await file.read()
    forecast_value, year = forecast_kpi(content)
    return {"predicted_year": year, "predicted_value": forecast_value}
