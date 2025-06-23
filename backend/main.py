from fastapi import FastAPI
from backend.routers import chat_router
from backend.routers import summarize_router
from backend.routers import kpi_router
from backend.routers import feedback_router
from backend.routers import eco_tips_router
from backend.routers import anomaly_router
from backend.routers import vector_router


app = FastAPI()

app.include_router(chat_router.router, prefix="/api")

app.include_router(summarize_router.router, prefix="/api")

app.include_router(kpi_router.router, prefix="/api")

app.include_router(feedback_router.router, prefix="/api")

app.include_router(eco_tips_router.router, prefix="/api")

app.include_router(anomaly_router.router, prefix="/api")

app.include_router(vector_router.router, prefix="/api")
