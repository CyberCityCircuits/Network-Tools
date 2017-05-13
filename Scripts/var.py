# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:18:16 2017

@author: admin
"""
import datetime as dt


#set varibales
app_name = "Run_PyInstaller"
ver = "0.02.00"
build = "02232017"

name = app_name + " V" + ver

email = "David@DREAM-Enterprise.com"

currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M%S")

package = "pyinstaller"
text1 = "readme.txt"
text2 = "changelog.txt"

#set system varibles
width = 300
lines = 300
