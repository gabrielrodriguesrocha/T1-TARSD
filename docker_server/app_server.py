import json
from bottle import request, route, run
from tinydb import TinyDB, Query
import sys

#Carrega o banco
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
#Define a tabela
service_table = db.table('service')

@route('/service', method='POST')
def service_post():
	#Carrega do body da requisição o arquivo json recebido
	params = json.loads(request.body.getvalue().decode('utf-8'))
	#Printa o arquivo recebido
	print('Data Received:')
	print(params)
	#insere na tabela
	document_id = service_table.insert(params)
	#verifica se realmete foi adicionado o arquivo
	if document_id == None:
		print("Failed on insertion")

@route('/service')
def service_get():
	#Retorna o banco inteiro
	return db.all()



run(host='0.0.0.0',port=80,debug=True)