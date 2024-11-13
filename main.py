from fastapi import FastAPI, APIRouter
from src.controller.ProdutoController import app_router

router = APIRouter()
app = FastAPI()

app.include_router(app_router)