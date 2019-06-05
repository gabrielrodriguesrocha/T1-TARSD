import json
from bottle import request, route, run
import docker
import sys

client = docker.from_env()

@route('/info/<id>')
def service_post():
    #Obtém informações sobre o container
    try:
        info = client.containers.get(id).stats(stream=False)
        response['id'] = info.content['id']
        response['image'] = client.containers.get(id).image
        response['name'] = info.content['name']
        response['timestamp'] = info.content['read']
        response['memory_usage'] = float(info.content['memory_stats']['usage']) / (1024.0 ** 2) # in MB
        cpu_delta = float(info.content['cpu_stats']['cpu_usage']['total_usage']) - float(info.content['pre_cpu_stats']['cpu_usage']['total_usage'])
        system_delta = float(info.content['cpu_stats']['system_cpu_usage']) - float(info.content['pre_cpu_stats']['system_cpu_usage'])
        response['cpu_usage'] = cpu_delta / system_delta
        return info
    except:
        return ('Container %s not found' % s)



run(host='0.0.0.0',port=80,debug=True)