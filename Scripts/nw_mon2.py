# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 21:54:12 2017

@author: DREAM
"""

import subprocess, os
import var, tasks, prtpi

try:
    import nmap
except ImportError:
    print ("Package 'nmap' not found.")
    tasks.pause(1)

netid = "192.168.0.0/24"
    
lst1_online_nmap = []    
lst2_online_nmap = []
lst3_online_nmap = []
lst1_output_arp = []
lst2_output_arp = []
lst3_output_arp = []
lst_ref1 = []
lst_ref2 = []
lst_ref3 = []

status0='offline'.rjust(8)
status1='online'.rjust(8)

x=0

def reset_ref():
    global output_nmap
    global lst_output_nmap
    global lst1_online_nmap
    global lst2_online_nmap
    global lst3_online_nmap
    global lst_ref1

    #create reference'offline'
    for i in range(256):
       lst_ref1.append([str(i).zfill(3), 'none', status0, '00-00-00-00-00-00', 
                        var.currdate, var.currtime, 0])
    
    lst1_online_nmap = []    
    lst2_online_nmap = []
    lst3_online_nmap = []    

    #read the output from nmap into a string
    output_nmap = subprocess.Popen(['nmap', '-sL', netid], stdout = subprocess.PIPE).communicate()[0]
    
    #split output from nmap into a list
    lst_output_nmap = output_nmap.splitlines()
    
    #decode the list items from byte objects
    for i in range(len(lst_output_nmap)):
        lst_output_nmap[i] = (lst_output_nmap[i].decode('UTF-8'))
    
    #adds the list items that are actually online to a new list
    for i in lst_output_nmap:
        if "(" in i:
            lst1_online_nmap.append(i)
    del lst1_online_nmap[0]
    del lst1_online_nmap[-1]
    
    #splits the items from the prior list into sublists for parsing
    for i in range(len(lst1_online_nmap)):
        lst2_online_nmap.append(lst1_online_nmap[i].split())
           
    #puts parsed items into new list
    for i in range(len(lst2_online_nmap)):
        lst3_online_nmap.append([lst2_online_nmap[i][5], lst2_online_nmap[i][4]])

    
    #Gets last octet out of lst2_online_nmap items
    for i in range(len(lst3_online_nmap)):
        
        x = int(lst3_online_nmap[i][0].split('.')[3].strip(")"))
        lst_ref1[x][2] = status1
        lst_ref1[x][1] = lst3_online_nmap[i][1]
        if lst_ref1[x][6] == 0:
            lst_ref1[x][6] = 1
            #Prints online devices.
            #print(lst_ref1[x][0], lst_ref1[x][1], lst_ref1[x][3], lst_ref1[x][5])

    #Using arp to get MAC addresses
    output_arp = subprocess.Popen(['arp', '-n'], stdout = subprocess.PIPE).communicate()[0]
    
    output_arp = output_arp.decode('UTF-8')
    lst1_output_arp = output_arp.splitlines()
    del lst1_output_arp[0]
        
    #decode the list items from byte objects
    for i in range(len(lst1_output_arp)):
        lst2_output_arp.append(lst1_output_arp[i].split())
        
    for i in range(len(lst2_output_arp)):
        x = int(lst2_output_arp[i][0].split('.')[3])
        lst_ref1[x][3] = lst2_output_arp[i][2]      


    for i in range(len(lst_ref1)):    
        if lst_ref1[i][6] == 1:
            #Prints online devices.
            #print(lst_ref1[i][0]+" - "+lst_ref1[i][1]+" - "+lst_ref1[i][3])
            prtpi.prt(lst_ref1[i][0]+" - "+lst_ref1[i][3]+" - "+lst_ref1[i][1])
 
            
def reset_chkbit():
    for i in range(256):
        lst_ref1[i][5] = 0           
            
            
def chk_arp():    
    global output_arp
    global lst1_output_arp, lst2_output_arp, lst3_output_arp, lst_ref1
    output_arp = subprocess.Popen(['arp', '-n'], stdout = subprocess.PIPE).communicate()[0]
    
    output_arp = output_arp.decode('UTF-8')
    lst1_output_arp = output_arp.splitlines()
    del lst1_output_arp[0]
        
    #decode the list items from byte objects
    for i in range(len(lst1_output_arp)):
        lst2_output_arp.append(lst1_output_arp[i].split())
        
    for i in range(len(lst2_output_arp)):
        x = int(lst2_output_arp[i][0].split('.')[3])
        lst_ref1[x][3] = lst2_output_arp[i][2]

        
def update_ref():
    global output_nmap
    global lst_output_nmap
    global lst1_online_nmap
    global lst2_online_nmap
    global lst3_online_nmap
    global lst_ref1

    #create reference'offline'
    #for i in range(256):
    #   lst_ref1.append([str(i).zfill(3), 'none', status0, '00-00-00-00-00-00', 
    #                    var.currdate, var.currtime, 0])
    
    lst1_online_nmap = []    
    lst2_online_nmap = []
    lst3_online_nmap = []    
    lst1_output_arp=[]
    lst2_output_arp=[]
    lst3_output_arp=[]

    #read the output from nmap into a string
    output_nmap = subprocess.Popen(['nmap', '-sL', netid], stdout = subprocess.PIPE).communicate()[0]
    
    #split output from nmap into a list
    lst_output_nmap = output_nmap.splitlines()
    
    #decode the list items from byte objects
    for i in range(len(lst_output_nmap)):
        lst_output_nmap[i] = (lst_output_nmap[i].decode('UTF-8'))
    
    #adds the list items that are actually online to a new list
    for i in lst_output_nmap:
        if "(" in i:
            lst1_online_nmap.append(i)
    del lst1_online_nmap[0]
    del lst1_online_nmap[-1]
    
    #splits the items from the prior list into sublists for parsing
    for i in range(len(lst1_online_nmap)):
        lst2_online_nmap.append(lst1_online_nmap[i].split())
           
    #puts parsed items into new list
    for i in range(len(lst2_online_nmap)):
        lst3_online_nmap.append([lst2_online_nmap[i][5], lst2_online_nmap[i][4]])

    
    #Gets last octet out of lst2_online_nmap items
    for i in range(len(lst3_online_nmap)):
        
        x = int(lst3_online_nmap[i][0].split('.')[3].strip(")"))
        lst_ref1[x][2] = status1
        lst_ref1[x][1] = lst3_online_nmap[i][1]
        if lst_ref1[x][6] == 0:
            lst_ref1[x][6] = 1
            #Prints online devices.
            #print(lst_ref1[x][0], lst_ref1[x][1], lst_ref1[x][3], lst_ref1[x][5])

    #Using arp to get MAC addresses
    output_arp = subprocess.Popen(['arp', '-n'], stdout = subprocess.PIPE).communicate()[0]
    
    output_arp = output_arp.decode('UTF-8')
    lst1_output_arp = output_arp.splitlines()
    del lst1_output_arp[0]
        
    #decode the list items from byte objects
    for i in range(len(lst1_output_arp)):
        lst2_output_arp.append(lst1_output_arp[i].split())
        
    for i in range(len(lst2_output_arp)):
        x = int(lst2_output_arp[i][0].split('.')[3])
        lst_ref1[x][3] = lst2_output_arp[i][2]      


    #for i in range(len(lst_ref1)):    
    #    if lst_ref1[i][6] == 1:
    #        #Prints online devices.
    #        #print(lst_ref1[i][0]+" - "+lst_ref1[i][1]+" - "+lst_ref1[i][3])
    #        prtpi.prt(lst_ref1[i][0]+" - "+lst_ref1[i][3]+" - "+lst_ref1[i][1])
 
    #Gets last octet out of lst2_online_nmap items
    for i in range(len(lst3_online_nmap)):
        
        x = int(lst3_online_nmap[i][0].split('.')[3].strip(")"))
        lst_ref1[x][2] = status1
        lst_ref1[x][1] = lst3_online_nmap[i][1]
        if lst_ref1[x][6] == 0:
            lst_ref1[x][6] = 1
            #Prints online devices.
            #print(lst_ref1[x][0], lst_ref1[x][1], lst_ref1[x][3], lst_ref1[x][5])                   
            prtpi.prt(lst_ref1[i][0]+" - "+lst_ref1[i][3]+" - "+lst_ref1[i][1])
        
if __name__ == '__main__':
    reset_ref()

    
   