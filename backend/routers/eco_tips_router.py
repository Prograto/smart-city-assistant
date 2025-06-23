from fastapi import APIRouter
from backend.models.eco_tip_schema import EcoTipInput
from backend.services.eco_tips_model import generate_eco_tips

router = APIRouter()

@router.post("/eco-tip")
def get_eco_tip(data: EcoTipInput):
    tips = generate_eco_tips(data.topic)
    return {"tips": tips}
