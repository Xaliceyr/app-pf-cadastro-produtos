from fastapi import APIRouter
from src.models.ProdutoModel import ProdutoModel 
from src.services.ProdutoService import ProdutoService
from src.models.respostasModel import Resposta

app_router = APIRouter(prefix="/produto")

@app_router.get("/list", status_code=200)
async def ListarTodos():
    resposta = await ProdutoService.ListarTodos()
    return Resposta(resposta)

@app_router.post('/criar', status_code=200)   
async def CriarDados(ProdutoModel: ProdutoModel):
    await ProdutoService.CriarDados(ProdutoModel)