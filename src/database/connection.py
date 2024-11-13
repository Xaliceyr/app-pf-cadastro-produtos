import pymongo
	
url_database = 'mongodb+srv://RafaelAlmeida:d93MTCe5D6llRn4B@grupo2.5tbir.mongodb.net/'

banco = pymongo.MongoClient(url_database)
#db = banco['db_produto']
db = banco['Grupo2']

Produto = db.Produto