from src.database.connection import Usuario, Patient
from src.models.ProdutoModel import ProductModel
from fastapi import HTTPException
from datetime import datetime

class ProductService:
    async def ListarTodos() -> list:
        try:
            return list(Patient.find())
        except Exception as error:
            raise HTTPException(400, detail=error)
    
    async def CriarDados(ProductModel: ProductModel):
        try:
            id = 1
            hub = {
                "id": id,
                "nome": ProductModel.nome,
                "sobrenome": ProductModel.sobrenome,
                "email": ProductModel.email,
                "telefone": ProductModel.telefone,
                "datacricao": datetime.now
            }
            Usuario.insert_one(hub)
        except Exception as error:
            raise HTTPException(400, detail=error)
            
        