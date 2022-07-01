# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:54:42 2022

@author: Aman Poovalappil

To send data continuously to server
"""

import socket
import pytz
import datetime

#  to mimic mabx
server = 'mabx'
# server = 'spectra'

spectra_ip = '192.168.74.8'
spectra_port = 5001

mabx_ip = '192.168.74.11'
mabx_port = 5002

# Create a UDP socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
if server == 'mabx':
    server_address = (mabx_ip, mabx_port)
elif server == 'spectra':
    server_address = (spectra_ip, spectra_port)
else:
    print('check the server name. mabx or spectra')
    exit(1)

# s.bind(server_address)
print("Do Ctrl+c to exit the program !!")
a = '[.1;This is a message: 12.98,3,4,5,6,7,8, +87,788.012]'

try:
    while True:
    
        # print("####### Server is listening #######")
        # data, address = s.recvfrom(4096)
        # print("\n\n 2. Server received: ",address, data, data.decode('utf-8'), "\n\n")
        # send_data =  input("Type some text to send => ")
        send_data =  (a).replace(' ','')
        # bts = s.sendto(send_data.encode('utf-8'), server_address)
        bts = s1.sendto(send_data.encode('utf-8'), server_address)
        print(datetime.datetime.now(pytz.timezone('US/Eastern')),
              "\t sent: ", send_data.encode('utf-8'), bts, " to ",server,"\n")
        #a = [a[i]+1 for i in range(0,len(a))]
except:
    s1.close()