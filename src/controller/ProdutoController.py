from fastapi import APIRouter
from src.models.ProdutoModel import ProdutoModel 
from src.services.ProdutoService import ProdutoService
from src.models.respostasModel import Resposta
from typing import Optional

app_router = APIRouter(prefix="/produto")

@app_router.get("/list", status_code=200)
async def ListarTodos():
    resposta = await ProdutoService.ListarTodos()
    return Resposta(resposta)

@app_router.post('/criar', status_code=200)   
async def CriarDados(produtoModel: ProdutoModel):
   return await ProdutoService.CriarDados(produtoModel)

@app_router.get("/buscar", status_code=200)
async def Buscar(
    id: Optional[int] = None,
    preco_minimo: Optional[float] = None,
    preco_maximo: Optional[float] = None
):
    resposta = await ProdutoService.Buscar(id=id, preco_minimo=preco_minimo, preco_maximo=preco_maximo)
    return Resposta(resposta)


@app_router.put('/atualizar/{id}', status_code=200)   
async def AtualizarDados(produtoModel: ProdutoModel, id: int):
    await ProdutoService.AtualizarDados(produtoModel, id)
    

@app_router.delete('/excluir/{id}', status_code=200)   
async def Excluir(id: int):
    await ProdutoService.Excluir(id)

