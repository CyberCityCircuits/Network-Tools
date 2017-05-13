# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:34:42 2017

@author: DREAM
"""

import subprocess

def run_ping(host):
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],
                            stdout = subprocess.PIPE).communicate()[0]

def run_netstat():
    dataset = []
    data = subprocess.Popen(["netstat","-no"],
                            stdout = subprocess.PIPE).communicate()[0]
                            
    data=(data.decode('utf-8'))
    dataset = data.splitlines()          
    del dataset[:4]
    
    for i in dataset:
       if len(i)>=50:
           line = i.split()
           
           print (line[0]+
                  " - Local: "+line[1].rjust(22)+
                  " - Foreign: "+line[2].rjust(22)+
                  " - Process ID: "+line[4].rjust(6)+
                  " - State: "+line[3].rjust(13))             
           