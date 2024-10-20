import pymongo

url_database = ''

banco = pymongo.MongoClient(url_database)
#db = banco['db_produto']
db = banco['backoffice-iot']

Patient = db.Patient
Usuario =  db.Usuario
Produto = db.Produto 