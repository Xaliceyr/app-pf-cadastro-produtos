from fastapi import APIRouter
from src.models.ProdutoModel import ProductModel 
from src.services.ProdutoService import ProductService
from src.models.respostasModel import Resposta

app_router = APIRouter(prefix="/hub")

@app_router.get("/list", status_code=200)
async def ListarTodos():
    resposta = await ProductService.ListarTodos()
    return Resposta(resposta)

@app_router.post('/criar', status_code=200)   
async def CriarDados(ProductModel: ProductModel):
    await ProductService.CriarDados(ProductModel)