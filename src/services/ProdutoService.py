<<<<<<< Updated upstream
from src.database.connection import Usuario, Patient
from src.models.ProdutoModel import ProdutoModel
=======
from src.database.connection import Produto  # Supondo que Produto seja a coleção do MongoDB
from src.models.ProdutoModel import ProdutoModel
from bson import ObjectId
>>>>>>> Stashed changes
from fastapi import HTTPException
from datetime import datetime

class ProdutoService:
    # Método para listar todos os produtos
    async def ListarTodos() -> list:
        try:
<<<<<<< Updated upstream
            return list(Patient.find())
=======
            # Retorna uma lista de produtos da coleção Produto
            return list(Produto.find())
>>>>>>> Stashed changes
        except Exception as error:
            raise HTTPException(400, detail=str(error))
    
<<<<<<< Updated upstream
    async def CriarDados(ProdutoModel: ProdutoModel, idModel):
        try:
            id = idModel.number
            hub = {
                "id": id,
                "nome": ProdutoModel.nome,
                "datacricao": datetime.now
            }
            Usuario.insert_one(hub)
=======
    # Método para criar um novo produto
    async def CriarDados(produtoModel: ProdutoModel):
        try:
            # Criando um novo produto com dados do produtoModel
            novo_produto = {
                "id": str(ObjectId()),  # Gerando um id único para o produto
                "nome": produtoModel.nome,
                "preco": produtoModel.preco,
                "quantidade": produtoModel.quantidade,
                "cor": produtoModel.cor,
                "data_criacao": datetime.now()
            }
            Produto.insert_one(novo_produto)  # Inserindo o produto na coleção
>>>>>>> Stashed changes
        except Exception as error:
            raise HTTPException(400, detail=str(error))
            
<<<<<<< Updated upstream
        
=======
    # Método para buscar um produto pelo id
    async def Buscar(id: str):
        try:
            # Retorna um único produto com o id fornecido
            produto = Produto.find_one({"id": id})
            if produto is None:
                raise HTTPException(404, detail="Produto não encontrado.")
            return produto
        except Exception as error:
            raise HTTPException(400, detail=str(error))
    
    # Método para atualizar os dados de um produto
    async def AtualizarDados(produtoModel: ProdutoModel, id: str):
        try:
            # Dicionário para armazenar os campos a serem atualizados
            atualizacao = {}

            # Atualiza apenas os campos que foram preenchidos no modelo
            if produtoModel.nome:
                atualizacao["nome"] = produtoModel.nome

            if produtoModel.preco:
                atualizacao["preco"] = produtoModel.preco

            if produtoModel.quantidade:
                atualizacao["quantidade"] = produtoModel.quantidade

            if produtoModel.cor:
                atualizacao["cor"] = produtoModel.cor

            atualizacao["data_atualizacao"] = datetime.now()  # Atualiza a data de modificação

            if atualizacao:
                # Realiza a atualização no banco de dados
                resultado = Produto.update_one(
                    {"id": id},
                    {"$set": atualizacao}
                )
                if resultado.matched_count == 0:
                    raise HTTPException(404, detail="Produto não encontrado para atualização.")
            else:
                raise HTTPException(400, detail="Nenhum campo foi preenchido para atualização.")
        except Exception as error:
            raise HTTPException(400, detail=str(error))
        
    # Método para excluir um produto
    async def Excluir(id: str):
        try:
            # Realiza a exclusão do produto
            resultado = Produto.delete_one({"id": id})
            if resultado.deleted_count == 0:
                raise HTTPException(404, detail="Produto não encontrado para exclusão.")
            return {"message": "Produto excluído com sucesso."}
        except Exception as error:
            raise HTTPException(400, detail=str(error))
>>>>>>> Stashed changes
