# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:34:42 2017

@author: DREAM
"""

import subprocess, os
import var, tasks


#define cosole size and color
os.system("mode con: cols=" + str(var.width) + " lines=" + str(var.lines))
os.system("color F")
os.system("cls")
os.system("echo off")


def logo():
    print()
    print()                                       
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()    
    print("888b      88 88888888888 888888888888".center(var.cent_width))
    print("8888b     88 88               88     ".center(var.cent_width))  
    print("88 `8b    88 88               88     ".center(var.cent_width))  
    print("88  `8b   88 88aaaaa          88     ".center(var.cent_width))  
    print("88   `8b  88 88\"\"\"\"\"          88     ".center(var.cent_width))  
    print("88    `8b 88 88               88     ".center(var.cent_width))  
    print("88     `8888 88               88     ".center(var.cent_width))  
    print("88      `888 88888888888      88     ".center(var.cent_width))  
    print()
    print("888888888888 ,ad8888ba,     ,ad8888ba,   88          ad88888ba ".center(var.cent_width))
    print("     88     d8\"'    `\"8b   d8\"'    `\"8b  88         d8\"     \"8b".center(var.cent_width))  
    print("     88    d8'        `8b d8'        `8b 88         Y8,        ".center(var.cent_width))  
    print("     88    88          88 88          88 88         `Y8aaaaa,  ".center(var.cent_width))  
    print("     88    88          88 88          88 88           `\"\"\"\"\"8b,".center(var.cent_width))  
    print("     88    Y8,        ,8P Y8,        ,8P 88                 `8b".center(var.cent_width))  
    print("     88     Y8a.    .a8P   Y8a.    .a8P  88         Y8a     a8P".center(var.cent_width))  
    print("     88      `\"Y8888Y\"'     `\"Y8888Y\"'   88888888888 \"Y88888P\" ".center(var.cent_width))  
    print()
    print(var.name.center(var.cent_width))
    print(var.email.center(var.cent_width))

def run_ping(host):
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],
                            stdout = subprocess.PIPE).communicate()[0]

def run_netstat():
    os.system("cls")
    dataset = []
    data = subprocess.Popen(["netstat","-no"],
                            stdout = subprocess.PIPE).communicate()[0]
                            
    data=(data.decode('utf-8'))
    dataset = data.splitlines()          
    del dataset[:4]
    
    for i in dataset:
       if len(i)>=50:
           line = i.split()
           
           print ((line[0]+
                  " - Local: "+line[1].rjust(22)+
                  " - Foreign: "+line[2].rjust(22)+
                  " - Process ID: "+line[4].rjust(6)+
                  " - State: "+line[3].rjust(13))
                  .center(var.cent_width))  
           tasks.pause(.05)
          
logo()
tasks.pause(2)
run_netstat()