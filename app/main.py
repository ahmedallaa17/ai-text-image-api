from fastapi import APIRouter,FastAPI
from app.routes import health
from app.routes import image_route

app = FastAPI()

app.include_router(health.router)

app.include_router(image_route.router)