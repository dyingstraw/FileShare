import http.server
import socketserver
import socket

import numpy as np
import os
import random

import qrcode
from qrcode.constants import ERROR_CORRECT_H


ips = socket.gethostbyname_ex(socket.gethostname())
print(ips)
if len(ips[2])>1:
    for index,ip in enumerate(ips[2]):
        print(index,ip)
n=input("请输入你局域网内的IP序号：")
n=int(n)
ip=ips[2][n]
print("选择的ip是：",ip)
port = random.randint(8000,30000)
qr = qrcode.QRCode(version=1,
                       error_correction=ERROR_CORRECT_H,
                       box_size=1, border=1)
qr.add_data("http://{}:{}".format(ip,port))
img = qr.make_image()

img=np.array(img)
for i in range(img.shape[0]):
    str="echo "
    for j in range(img.shape[1]):
        if img[i][j]:
            str+="  \x1b[40;37m"
        else:
            str+="  \x1b[47;37m"
    str+="\x1b[0m"
    os.system(str)
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
    print("serving at http://{}:{}".format(ip,port))
    httpd.serve_forever()
