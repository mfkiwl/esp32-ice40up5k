import machine
import time
import re


import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)

print('listening on', addr)

file_pat = re.compile('GET\\s+/(\\S*)\\s+')

while True:
    conn, addr = s.accept()
    print('client connected from', str(addr))
    request = conn.recv(1024)
    request = request.decode('utf-8')
    print('Content = \n%s' % request)
    file_req = file_pat.match(request).group(1)
    if(file_req == ''):
        print('Client requested root\n')
        response = open('demo_server.html', 'rb').read()
    else:
        print('client requested: %s' % file_req)
        response = open(file_req, 'rb').read()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()