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
file_ext = re.compile('^\\w+.([a-zA-Z]+)$')

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
        ext = 'html'
    else:
        print('client requested: %s' % file_req)
        ext = file_ext.match(file_req).group(1)
        try:
            response = open(file_req, 'rb').read()
        except OSError:
            response = open('page_not_found.html', 'rb').read()
            ext = 'html'

    
    # Set mime type appropriately
    if(ext == 'html'):
        mime = 'text/html'
    elif(ext == 'acc'):
        mime = 'audio/acc'
    elif(ext == 'abw'):
        mime = 'application/x-abiword'
    elif(ext == 'arc'):
        mime = 'application/x-freearc'
    elif(ext == 'avi'):
        mime = 'video/x-msvideo'
    elif(ext == 'azw'):
        mime = 'application/vnd.amazon.ebook'
    elif(ext == 'bin'):
        mime = 'application/octet-stream'
    elif(ext == 'bmp'):
        mime = 'image/bmp'
    elif(ext == 'bz'):
        mime = 'application/x-bzip'
    elif(ext == 'bz2'):
        mime = 'application/x-bzip2'
    elif(ext == 'csh'):
        mime = 'application/x-csh'
    elif(ext == 'css'):
        mime = 'text/css'
    elif(ext == 'csv'):
        mime = 'text/csv'
    elif(ext == 'doc'):
        mime = 'application/msword'
    elif(ext == 'docx'):
        mime = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    elif(ext == 'eot'):
        mime = 'application/vnd.ms-fontobject'
    elif(ext == 'epub'):
        mime = 'application/epub+zip'
    elif(ext == 'gz'):
        mime = 'application/gzip'
    elif(ext == 'gif'):
        mime = 'image/gif'
    elif(ext == 'htm'):
        mime = 'text/html'
    elif(ext == 'ico'):
        mime = 'image/vnd.microsoft.icon'
    elif(ext == 'ics'):
        mime = 'text/calendar'
    elif(ext == 'jar'):
        mime = 'application/java-archive'
    elif(ext == 'jpeg'):
        mime = 'image/jpeg'
    elif(ext == 'jpg'):
        mime = 'image/jpeg'
    elif(ext == 'js'):
        mime = 'text/javascript'
    elif(ext == 'json'):
        mime = 'application/json'
    elif(ext == 'jsonld'):
        mime = 'application/ld+json'
    elif(ext == 'mid'):
        mime = 'audio/midi'
    elif(ext == 'midi'):
        mime = 'audio/midi'
    elif(ext == 'mjs'):
        mime = 'text/javascript'
    elif(ext == 'mp3'):
        mime = 'audio/mpeg'
    elif(ext == 'mpeg'):
        mime = 'video/mpeg'
    elif(ext == 'mpkg'):
        mime = 'application/vnd.apple.installer+xml'
    elif(ext == 'odp'):
        mime = 'application/vnd.oasis.opendocument.presentation'
    elif(ext == 'ods'):
        mime = 'application/vnd.oasis.opendocument.spreadsheet'
    elif(ext == 'odt'):
        mime = 'application/vnd.oasis.opendocument.text'
    elif(ext == 'oga'):
        mime = 'audio/ogg'
    elif(ext == 'ogv'):
        mime = 'video/ogg'
    elif(ext == 'ogx'):
        mime = 'application/ogg'
    elif(ext == 'opus'):
        mime = 'audio/opus'
    elif(ext == 'otf'):
        mime = 'font/otf'
    elif(ext == 'png'):
        mime = 'image/png'
    elif(ext == 'pdf'):
        mime = 'application/pdf'
    elif(ext == 'php'):
        mime = 'application/x-httpd-php'
    elif(ext == 'ppt'):
        mime = 'application/vnd.ms-powerpoint'
    elif(ext == 'pptx'):
        mime = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
    elif(ext == 'rar'):
        mime = 'application/vnd.rar'
    elif(ext == 'rtf'):
        mime = 'application/rtf'
    elif(ext == 'sh'):
        mime = 'application/x-sh'
    elif(ext == 'svg'):
        mime = 'image/svg+xml'
    elif(ext == 'swf'):
        mime = 'application/x-shockwave-flash'
    elif(ext == 'tar'):
        mime = 'application/x-tar'
    elif(ext == 'tif'):
        mime = 'image/tiff'
    elif(ext == 'tiff'):
        mime = 'image/tiff'
    elif(ext == 'ts'):
        mime = 'video/mp2t'
    elif(ext == 'ttf'):
        mime = 'font/ttf'
    elif(ext == 'txt'):
        mime = 'text/plain'
    elif(ext == 'vsd'):
        mime = 'application/vnd.visio'
    elif(ext == 'wav'):
        mime = 'audio/wav'
    elif(ext == 'weba'):
        mime = 'audio/webm'
    elif(ext == 'webm'):
        mime = 'audio/webm'
    elif(ext == 'webp'):
        mime = 'image/webp'
    elif(ext == 'woff'):
        mime = 'font/woff'
    elif(ext == 'woff2'):
        mime = 'font/woff2'
    elif(ext == 'xhtml'):
        mime = 'application/xhtml+xml'
    elif(ext == 'xls'):
        mime = 'application/vnd.ms-excel'
    elif(ext == 'xlsx'):
        mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    elif(ext == 'xml'):
        mime = 'text/xml'
    elif(ext == 'xul'):
        mime = 'application/vnd.mozilla.xul+xml'
    elif(ext == 'zip'):
        mime = 'application/zip'
    elif(ext == '3gp'):
        mime = 'video/3gpp'
    elif(ext == '3g2'):
        mime = 'video/3gpp2'
    elif(ext == '7z'):
        mime = 'application/x-7z-compressed'
    else:
        mime = 'text'

    conn.send('HTTP/1.1 200 OK\n')
    c_type = 'Content-Type: ' + mime + '\n'
    conn.send(c_type)
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()