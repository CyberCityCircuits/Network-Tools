# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 08:55:03 2017

@author: DREAM
"""

import var

import os, subprocess
import wmi

def wifi_pw():
    os.system("netsh wlan show profile")
    
def timed_shutdown():
    os.system("shutdown -f -t 5")
    
def prod_key():
    #global prod_key
    #os.system("wmic path softwarelicensingservice get OA3xOriginalProductKey")    
    
    prod_key = subprocess.Popen(["wmic","path","softwarelicensingservice","get","OA3xOriginalProductKey"],
                            stdout = subprocess.PIPE).communicate()[0]

    prod_key = str(prod_key)
    prod_key = prod_key.replace("\\r","")
    prod_key = prod_key.replace("\\n","")
    prod_key = prod_key.split()
    prod_key = str(prod_key[1])

    print("You Product Key is: "+str(prod_key))
    
def ipconfig_all():
    global ipconfig
    ipconfig = subprocess.Popen(["ipconfig","/all"],
                                stdout = subprocess.PIPE).communicate()[0]    
    ipconfig = str(ipconfig)
    ipconfig = ipconfig.replace("\\r","")
    #ipconfig = ipconfig.replace("\\n","")
    ipconfig = ipconfig.split("\\n")
    hostname = ipconfig[3].split()[-1]

    print("Hostname: "+hostname)
    print()

    if any(items.startswith("Ethernet") for items in ipconfig):
        print("Ethernet Adapter Present")
    else:
        print("Ethernet Adapter Not Present")
    if any(items.startswith("Wireless") for items in ipconfig):
        print("Wireless Adapter Present")
    else:
        print("Wireless Adapter Not Present")
    if any(items.startswith("Tunnel") for items in ipconfig):
        print("Tunnel Adapter Present")        
    else:
        print("Tunnel Adapter Not Present")

def find_ip(machine):
    global ip_list
    ip_list = []
    if machine == None:
        wmi_obj = wmi.WMI()
    else:
        wmi_obj = wmi.WMI(machine)
    wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
    wmi_out = wmi_obj.query( wmi_sql )
    
    for dev in wmi_out:
        print(("IPv4 Address: " + str(dev.IPAddress[0])).ljust(40) + ("Default IP Gateway: " + str(dev.DefaultIPGateway[0])).ljust(40))
        ip_list.append(("IPv4Address:", dev.IPAddress[0], "DefaultIPGateway:", dev.DefaultIPGateway[0]))


def ping(host):
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],
                            stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        print(host + " is Unreachable")
    else:
        print(host + " is Connectable")
                                    
    
        
if __name__ == "__main__":
    os.system("cls")
    prod_key()
    print()
    ipconfig_all()
    print()
    find_ip("")