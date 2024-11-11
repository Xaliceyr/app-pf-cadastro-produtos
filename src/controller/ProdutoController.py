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
async def CriarDados(produtoModel: ProdutoModel):
   return await ProdutoService.CriarDados(produtoModel)

@app_router.get("/buscar/{id}", status_code=200)
async def Buscar(id):
    resposta = await ProdutoService.Buscar(id)
    return Resposta(resposta)


@app_router.put('/atualizar/{id}', status_code=200)   
async def AtualizarDados(produtoModel: ProdutoModel, id: int):
    await ProdutoService.AtualizarDados(produtoModel, id)
    

@app_router.delete('/excluir/{id}', status_code=200)   
async def Excluir(id: int):
    await ProdutoService.Excluir(id)

