# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:54:42 2022

@author: Aman Poovalapppil
"""

import socket
import pytz
import datetime

#import sys

# To receive data continuously by the server to mimic mabx
# server = 'mabx'
server = 'spectra'

spectra_ip = '192.168.74.8'
spectra_port = 5001

mabx_ip = '192.168.74.11'
mabx_port = 5002

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
if server == 'mabx':
    server_address = (mabx_ip, mabx_port)
elif server == 'spectra':
    server_address = (spectra_ip, spectra_port)
else:
    print('check the server name. mabx or spectra')
    exit(1)

s.bind(server_address)
print("Do Ctrl+c to exit the program !!")
try:
    while True:
        # print("####### Server is listening #######")
        data, address = s.recvfrom(1024)
        print(datetime.datetime.now(pytz.timezone('US/Eastern')),
              server," received: ", data.decode('utf-8'), "from ",address, "\n")
        # print(datetime.datetime.now(pytz.timezone('US/Eastern')),
        #   server," received: ", data, "from ",address, "\n")
except:
    s.close()