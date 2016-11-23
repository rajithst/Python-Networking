import os.path
import socket
host = ""
port = 3090
rootdir = "root"

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(10)


def getextention(data):
    rf=data[5:data.find(' ',5)+1]
    rf=rf.strip()
    return rf[rf.find('.'):]


def contentse(typeofcont):
    contarray = {
    '.css': 'text/css',
    '.txt': 'text/plain',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.png': 'image/png',
    '.html':'text/html',

    }
    return contarray[typeofcont]



while 1:
    connect,address = sock.accept()
    data = connect.recv(1024)
    req_method = data.split(' ')[0]

    if (req_method == 'GET') | (req_method == 'HEAD'):
        header = ''
        file = data.split(' ')[1]
        #print file

        if (file == '/'): 
            indexpath = rootdir+'/index.html'
            existfile = os.path.exists(indexpath)
            if (existfile == True):
                header = 'HTTP/1.0 200 OK\r\n'
                contentType = "Content-Type: text/html\n\n"
                file_handler = open(indexpath,'rb')
                content = file_handler.read() 
                response = content.encode('utf-8')
                file_handler.close()
            else:
                header = 'HTTP/1.0 404 Not Found\r\n'
                contentType = "Content-Type: text/html\n\n"
                notfoundpath = path = rootdir+'/404.html'
                file_handler = open(notfoundpath,'rb')
                content = file_handler.read() 
                response = content.encode('utf-8')
                file_handler.close()
        else:
            pnewpath = rootdir+ file
            existfile = os.path.exists(pnewpath)
            if (existfile == True):
                ex = getextention(data)
                cttype=contentse(ex.strip())
                print cttype
                header = 'HTTP/1.0 200 OK\r\n'
                contentType = cttype+'\r\n' 
                file_handler = open(pnewpath,'rb')
                content = file_handler.read() 
                response = content
                file_handler.close()
            else:
                header = 'HTTP/1.0 404 Not Found\r\n'
                contentType = "Content-Type: text/html\n\n"
                notfoundpath = path = rootdir+'/404.html'
                file_handler = open(notfoundpath,'rb')
                content = file_handler.read() 
                response = content.encode('utf-8')
                file_handler.close()
    


    connect.send(header)
    connect.send(contentType)
    connect.send(response)
    connect.close()
