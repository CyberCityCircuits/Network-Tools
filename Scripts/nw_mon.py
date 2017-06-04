# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 23:06:12 2017

@author: DREAM

WRITTEN FOR USE ON RASPBERRY PI 3 AND PYTHON 3
"""

import subprocess, os
import var, tasks

try:
    import nmap
except ImportError:
    print ("Package 'nmap' not found.")
    tasks.pause(1)


netid = "192.168.0.0/24"
    
lst1_online = []    
lst2_online = []
lst3_online = []

def chk_new():

    global output_nmap, output_arp
    global lst_output_nmap
    global lst1_online
    global lst2_online
    global lst3_online
    
    lst1_online = []    
    lst2_online = []
    lst3_online = []    

    output_nmap = subprocess.Popen(['nmap', '-sL', netid], stdout = subprocess.PIPE).communicate()[0]
    
    lst_output_nmap = output_nmap.splitlines()
    
    for i in range(len(lst_output_nmap)):
        lst_output_nmap[i] = (lst_output_nmap[i].decode('UTF-8'))
        
    #for i in lst_output_nmap:
    #    print(i)
    
    for i in lst_output_nmap:
        if "(" in i:
            lst1_online.append(i)
    del lst1_online[0]
    del lst1_online[-1]
    
    for i in range(len(lst1_online)):
        lst2_online.append(lst1_online[i].split())
    
    #for i in lst1_online:
    #    print (i)
            
    for i in range(len(lst2_online)):
        lst3_online.append([lst2_online[i][5], lst2_online[i][4]])
        #del lst2_online[i][0]
        #del lst2_online[i][1]
        #del lst2_online[i][2]
        #del lst2_online[i][3]
    
    #Gets last octet out of lst2_online items
    #lst3_online[i][0].split('.')[3].strip(")")

    output_arp = subprocess.Popen(['arp'], stdout = subprocess.PIPE).communicate()[0]

    




if __name__ == "__main__":
    
    var.width = 400
    var.lines = 250
    
    #define cosole size and color
    os.system("mode con: cols=" + str(var.width) + " lines=" + str(var.lines))
    os.system("color F")
    os.system("cls")
    os.system("echo off")





