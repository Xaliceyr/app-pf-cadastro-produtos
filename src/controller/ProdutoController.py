from fastapi import APIRouter, HTTPException
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
@app_router.get('/criar', status_code=200)   
async def CriarDados(produtoModel: ProdutoModel):
    resposta = await ProdutoService.AdicionarEstoque(ProdutoModel)
    return Resposta(resposta)
   
@app_router.get("/buscar/{id}", status_code=200)
async def Buscar(id):
    resposta = await ProdutoService.Buscar(id, 0)
    return Resposta(resposta)

@app_router.put('/atualizar/{id}', status_code=200)   
async def CriarDados(produtoModel: ProdutoModel):
    await ProdutoService.AtualizarDados(produtoModel)
    

@app_router.delete('/excluir/{id}', status_code=200)   
async def CriarDados(id):
    await ProdutoService.Excluir(id)    
