#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import os
import time
import sys
from subprocess import Popen
devnull = open(os.devnull, 'wb')
try:
  blok=0
  hosts=[]
  aliveHosts=[]
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  ipA=s.getsockname()[0]
  s.close()
except socket.error as msg:
  print("internet erisimi yok")
def ipBlok(ipA,blok):
 blok0=ipA.split('.')[0]
 blok1=ipA.split('.')[1]
 blok2=ipA.split('.')[2]
 blok=blok0+"."+blok1+"."+blok2+"."
 return blok
ipb=(ipBlok(ipA,blok))
for x in range(0,255):
  ip=ipb+str(x)
  if ip!=ipA:
   hosts.append((ip, Popen(['ping', '-c', '1', ip], stdout=devnull)))
while hosts:
    for i, (ip, proc) in enumerate(hosts[:]):
        if proc.poll() is not None:
            hosts.remove((ip, proc))
            if proc.returncode == 0:
                print(ip + " :up")
    time.sleep(.04)
devnull.close()


 
  

 






