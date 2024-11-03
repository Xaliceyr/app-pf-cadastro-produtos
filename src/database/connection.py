import pymongo

url_database = 'mongodb+srv://rafaelcorrea:<db_password>@cluster0.5tbir.mongodb.net/'

banco = pymongo.MongoClient(url_database)
#db = banco['db_produto']
db = banco['backoffice-iot']


Produto = db.Produto 