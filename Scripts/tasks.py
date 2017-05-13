# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:18:16 2017

@author: admin
"""

import var

import os, re, sys
import datetime as dt
from time import sleep
from shutil import copyfile
from shutil import rmtree as rm_dir
from pathlib import Path
from bs4 import BeautifulSoup as bs
import lxml.etree as et

#from tkinter import *
from tkinter import messagebox, Label
from tkinter import simpledialog


var.currdate = dt.date.today().strftime("%Y%m%d")
var.currtime = dt.datetime.now().strftime("%H%M%S")


#checks if file exists in var.dir_temp
def chk_file_temp(file_name):
    if not Path(var.dir_temp + "/" + file_name).is_file():
        msg_error("T04: Check Error\nFile Not Found. \n ")   
        
        
def client_exit():
    option = messagebox.askquestion("Exit", "Are You Sure?", icon="question")
    if option =="yes":
        sys.exit()
        

#copy files
def copy(fn1,fn2):
    if os.path.isfile(fn1):
        copyfile(fn1,fn2)
    else:
        msg_error("T03: Copy Error\nFile Doesn't Exit")
    
        
#delete a directory
def delete_dir(dir_name):
    if os.path.exists(dir_name):
        rm_dir(dir_name)
    #else:
    #    msg_error("T01: Delete Error\nDirectory Doesn't Exist")
    
        
#delete file
def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        msg_error("T02: Delete Error\nFile Doesn't Exit")

        
#make directories as needed
def mk_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

        
def mk_log():
    #creates and writes to log file
    f = open(var.dir_temp + "\\" + var.log_name + ".txt","w")
    log_currdate = dt.date.today().strftime("%m/%d/%Y")
    log_currtime = dt.datetime.now().strftime("%H:%M:%S")
    f.write(var.app_name + " V" + var.version + "\n"
            "Starting Date - " + log_currdate + "\n"
            "Starting Time - " + log_currtime + "\n"
            "\n")
    f.close()    
    
    
def msg(text):
    messagebox.showinfo(var.long_app, text)
    
    
def msg_error(text):
    messagebox.showerror(var.long_app, text)

    
#set wait command
def pause(value):
    if value == 0:   #if 0 is entered it creates a press any key prompt.
        os.system("pause")
    elif int(value):
        sleep(value)


#set date and time        
def set_date_time():
    global currdate, currtime
    var.currdate = dt.date.today().strftime("%Y%m%d")
    var.currtime = dt.datetime.now().strftime("%H%M%S")
    
        
    

