from src.database.connection import Produto
from src.models.ProdutoModel import ProdutoModel
from src.models.idModel import number 
from fastapi import HTTPException
from datetime import datetime
from typing import Optional

class ProdutoService:
    async def ListarTodos() -> list:
        try:
            return list(Produto.find())
        except Exception as error:
            raise HTTPException(400, detail=error)
    
    async def CriarDados(produtoModel: ProdutoModel):
        try:
            ultimo_Produto = Produto.find_one(sort=[("id", -1)])
            id = ultimo_Produto["id"] + 1 if ultimo_Produto else 1
            Novo_Produto = {
                "id": id,
                "nome": produtoModel.nome,
                "preco": produtoModel.preco,
                "quantidade": produtoModel.quantidade,
                "cor": produtoModel.cor,
                "data_criacao": datetime.now()
                
            }
            Produto.insert_one(Novo_Produto)
        except Exception as error:
            raise HTTPException(400, detail=error)
            
    async def Buscar(
            id: Optional[int] = None,
            preco_minimo: Optional[float] = None,
            preco_maximo: Optional[float] = None,
    ):
            try:
                filtro = {}
                if id :
                    filtro["id"] = id
                if preco_minimo :
                    filtro["preco"] = {"$gte": preco_minimo}
                if preco_maximo :
                    filtro["preco"] = {"$lte": preco_maximo}
                return list(Produto.find(filtro))

            
            except Exception as error:
                raise HTTPException(400, detail=error)
    
    async def AtualizarDados(produtoModel: ProdutoModel, id: int):
        try:
            atualizar = {}

            if produtoModel.nome:
                atualizar["nome"] = produtoModel.nome

            if produtoModel.preco:
                atualizar["preco"] = produtoModel.preco

            if produtoModel.quantidade:
                atualizar["quantidade"] = produtoModel.quantidade

            if produtoModel.cor:
                atualizar["cor"] = produtoModel.cor


            atualizar["data_atualizacao"] = datetime.now()

            if atualizar:
                Produto.update_one(
                    { "id": id },
                    { 
                        "$set": atualizar
                    }
                )
            else:
                raise HTTPException(400, detail="Nenhum campo foi preenchido para atualização.")
        except Exception as error:
            raise HTTPException(400, detail=str(error))
        

        
    async def Excluir(id: int):
        try:
            resultado = Produto.delete_one({"id": id})
            if resultado.deleted_count == 0:
                raise HTTPException(status_code=404, detail="Produto não encontrado")
            return {"message": "Produto removido com sucesso"}
        except Exception as error:
            raise HTTPException(400, detail=str(error))