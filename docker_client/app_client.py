import json
import requests
import socket, sys

while (True):
    x = input()
    if x == 'get':
       r = requests.get('http://192.168.50.2:5001/service')
       print(r.content)
    elif x == 'post':
        if len(sys.argv) > 1:
            own_id = sys.argv[1]
        else:
            own_id = socket.gethostname()
        r = requests.get('http://192.168.50.3/info/' + own_id)
        print(r.content)
        requests.post('http://192.168.50.2:5001/service', data=r.content)
    elif x == 'exit':
        exit()
    else:
        print('Options are get, post and exit')