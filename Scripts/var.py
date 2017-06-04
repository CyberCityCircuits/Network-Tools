# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:18:16 2017

@author: admin
"""
import datetime as dt


#set varibales
app_name = "Net Tools"
ver = "0.00.10"
build = "20170513"

name = app_name + " V" + ver

email = "David@DREAM-Enterprise.com"

currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M%S")

package = "pyinstaller"
text1 = "readme.txt"
text2 = "changelog.txt"

#set system varibles
width = 120
lines = 50

cent_width = width-1