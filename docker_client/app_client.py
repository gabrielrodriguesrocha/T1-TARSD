import requests

while (True):
    x = input()
    if x == 'get':
       r = requests.get('http://192.168.50.2:5001/service')
       print(r.content)
    elif x == 'post':
        r = requests.get('http://192.168.50.3/info', data=json.dumps({'id': socket.gethostname()}))
        requests.post('http://192.168.50.2:5001/service', data=r.content)
    elif x == 'exit':
        exit()
    else:
        print('Options are get, post and exit')

