from src.database.connection import Produto
from src.models.ProdutoModel import ProdutoModel
from src.models.idModel import number 
from fastapi import HTTPException
from datetime import datetime


class ProdutoService:
    async def ListarTodos() -> list:
        try:
            return list(Produto.find())
        except Exception as error:
            raise HTTPException(400, detail=error)
    
    async def CriarDados(produtoModel: ProdutoModel):
        try:
            Produto = {
                "id": 2,
                "nome": produtoModel.nome,
                "preco": produtoModel.preco,
                "quantidade": produtoModel.quantidade,
                "cor": produtoModel.cor,
                "data_criacao": datetime.now()
            }
            Produto.insert_one(Produto)
        except Exception as error:
            raise HTTPException(400, detail=error)
            
    async def Buscar(id):
        try:
            return Produto.find({"id": id})
        except Exception as error:
            raise HTTPException(400, detail=error)
    
    async def AtualizarDados(produtoModel: ProdutoModel, id: int):
        try:
            atualazar = {}

            if produtoModel.nome:
                atualazar["nome"] = produtoModel.nome

            if produtoModel.sobrenome:
                atualazar["sobrenome"] = produtoModel.sobrenome

            if produtoModel.email:
                atualazar["email"] = produtoModel.email

            if produtoModel.telefone:
                atualazar["telefone"] = produtoModel.telefone

            atualazar["data_atualizacao"] = datetime.now()

            if atualazar:
                Produto.update_one(
                    { "id": id },
                    { 
                        "$set": atualazar
                    }
                )
            else:
                raise HTTPException(400, detail="Nenhum campo foi preenchido para atualização.")
        except Exception as error:
            raise HTTPException(400, detail=str(error))
        
    async def Excluir(id):
        try:
            return Produto.delete_one({"id": id})
        except Exception as error:
            raise HTTPException(400, detail=error)