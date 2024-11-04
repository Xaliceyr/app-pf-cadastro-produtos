from src.database.connection import Usuario, Patient
from src.models.ProdutoModel import ProdutoModel
from fastapi import HTTPException
from datetime import datetime

class ProdutoService:
    async def ListarTodos() -> list:
        try:
            return list(Patient.find())
        except Exception as error:
            raise HTTPException(400, detail=error)
    
    async def CriarDados(ProdutoModel: ProdutoModel, idModel):
        try:
            id = idModel.number
            hub = {
                "id": id,
                "nome": ProdutoModel.nome,
                "datacricao": datetime.now
            }
            Usuario.insert_one(hub)
        except Exception as error:
            raise HTTPException(400, detail=error)
            
        