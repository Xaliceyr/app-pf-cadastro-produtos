import pymongo

url_database = 'mongodb+srv://rafaelcorrea:jJv7LHgH56Wja2UB@cluster0.5tbir.mongodb.net/'

banco = pymongo.MongoClient(url_database)
#db = banco['db_produto']
db = banco['Grupo_2']

Produtos = db.Produto