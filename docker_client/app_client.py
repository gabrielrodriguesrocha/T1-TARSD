from bottle import requests, route, run
import socket
import request

while (True):
    x = input()
    if x == 'get':
       r = request.get('http://192.168.50.2/service')
       print(r.content)
    elif x == 'post':
        r = request.get('http://192.168.50.3', data=json.dumps({'id': socket.gethostname()}))
        request.post('http://192.168.50.3/service', data=r.content)
    elif x == 'exit':
        exit()
    else:
        print('Options are get, post and exit')

