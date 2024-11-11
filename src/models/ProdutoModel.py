from pydantic import BaseModel, Field, field_validator
from typing import Optional

class ProdutoModel(BaseModel):
    nome: str = Field(..., description="nome não pode ser nulo")
    preco: float = Field(..., description="")
    categoria: str = Field(..., description="")
    quantidade: int = Field(..., description="")
    cor: str
    tamanho: str
    validade: str

    @field_validator('preco')
    def preco_nao_ser_null(cls, value):
        if value <= 0:
            raise ValueError('preço tem que ser positivo.')
        return value
    
    @field_validator('nome')
    def must_not_be_empty(cls, value):
        if not value or value.strip() == "":
            raise ValueError('campo não pode ser nulo')
        return value
    