from src.database.connection import Patient

number = Patient.estimated_document_count()
print(number)
if number >= 1:
    number += 1