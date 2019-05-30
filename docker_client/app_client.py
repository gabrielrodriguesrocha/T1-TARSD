from bottle import request, route, run
import socket

while ((x = input()) != 'exit'):
    if x == 'get':
       r = requests.get('192.168.50.2/service')
       print(r.content)
    elif x == 'post':
        r = requests.get('192.168.50.3', data=json.dumps({'id': socket.gethostname()}))´
        requests.post('192.168.50.3/service', data=r.content)
    else:
        print('Options are get and post')

