from src.database.connection import Produto

def number ():
    number = Produto.estimated_document_count()
    print(number)
    if number >= 1:
        number += 1

    return number