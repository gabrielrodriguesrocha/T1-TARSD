import json
from bottle import request, route, run
from tinydb import TinyDB, Query
import requests
import sys

#Carrega o banco
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
#Define a tabela
service_table = db.table('service')

@post('/service')
def service_post():
	#Carrega do bory da requisição o arquivo json recebido
	params = json.loads(request.body.getvalue().decode('utf-8'))
	#Printa o arquivo recebido
	print('Service Received:')
	print(params)
	#insere na tabela
	document_id = service_table.insert(params)
	#verifica se realmete foi adicionado o arquivo
	if document_id == None:
		print('Failed on to update')

@get('/service')
def service_get():
	#Retorna o banco inteiro
	return json.loads('db.json')



run(host='0.0.0.0',port=80,debug=True)