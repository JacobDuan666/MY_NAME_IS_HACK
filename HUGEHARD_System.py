#import
import easygui as gui
import tkinter as tk
import sys
import time
import os
import subprocess

#varibles
nowtime_gm = time.gmtime()
nowtime = str(nowtime_gm.tm_mon) + "/" + str(nowtime_gm.tm_mday) + "/" + str(nowtime_gm.tm_year) + "  "
ve = "Version: "
sp = "Meomery: "
de = "Developer: "

#system loading
def sysload():
    startsys = gui.msgbox(msg = "Welcome to HUGEHARD SYSTEM, now I am starting your system\nYou might wait a while for the system starting program", title = "HUGEHARD SYSTEM", ok_button = "CONTINUE")
    if startsys == "CONTINUE":
        gui.textbox(msg = "Now I am starting your system", title = "HUGEHARD System", text = "Checking system files...\nComplete\nChecking updates\nComplete\nReading system file...\nComplete\nLoading system file...\nComplete\nStarting yousr system...\ncomplete")
        gui.msgbox(msg = "Welcome to HUGEHARD System", image = "/Users/jacobduan/Desktop/WORK/MY_NAME_IS_HACK-BETA/Images/load.gif", title = "HUGEHARD System")
        

#terminal
def ter():
    appinfo = gui.buttonbox(msg = "Application: Terminal", title = "HUGEHARD System", choices = ("Open", "Info", "Cancel"), image = "/Users/jacobduan/Desktop/WORK/MY_NAME_IS_HACK-BETA/Images/Terminal.gif")
    if appinfo == "Open":
        #subprocess.call(['python3', 'simulateTerminal.py'])
        os.system("python3 simulateTerminal.py")
    if appinfo == "Info":
        gui.msgbox(msg = ve+"1.0e"+"\n"+sp+"3.01M"+"\n"+de+"HUGEHARD SYSTEM DEVELOPER"+"\n", title = "HUGEHARD System", image = "/Users/jacobduan/Desktop/WORK/MY_NAME_IS_HACK-BETA/Images/Terminal.gif")

#waterf0x browser
def bs():
    while True:
        appinfo = gui.buttonbox(msg = "Application: Waterf0x", title = "HUGEHARD System", choices = ("Open", "Info", "Cancel"), image = "/Users/jacobduan/Desktop/WORK/MY_NAME_IS_HACK-BETA/Images/waterf0x.gif")
        if appinfo == "Open":
            web = gui.enterbox(msg = "Welcome to Waterf0X broswer, type the website here", title = "HUGEHARD System -- Waterf0X")
            if web == "pylogin.com/has_been_locked":
                gui.textbox(msg = "The user has been locked", text = "The user has been locked might be you don't have a account or your account is not safe, or your account has been hacked")
            if web == "10.10.10.14/23":
                gui.textbox(msg = "PROBLEM\nNo.8", text = "The account cannot be hack might because the account has protect by some encrypt system that we don't know, until this encrypt system's source code is open to us, the hack might be succed", title = "Waterf0X")
            if web == "tools.me":
                gui.textbox(msg = "tools.me\nCOPYRIGHT TOOLS.ME, TEMPLE MONKEY COMPANY", text = "Welcome to tools.me, there are a lot of free tools and fee-paying tools here", title = "HUGEHARD System -- Waterf0X")
                dl = gui.choicebox(msg = "Tools", choices = ["Waterf0X - Fast and simple broswer", "Mail Box - Fast speed email tools", "HTTP Catcher - Powerful HTTP catching tools"], title = "HUGEHARD System -- Waterf0X")
                if dl == "Waterf0X":
                    gui.msgbox(msg = "You already download this application in your computer", title = "HUGEHARD System -- Waterf0X")
                    continue
                else:
                    gui.msgbox(msg = "You already download this application in your computer", title = "HUGEHARD System -- Waterf0X")
                    continue
            else:
                chs = gui.buttonbox(msg = "Can't found the server, continue?", choices = ["continue searching", "exit"], title = "HUGEHARD System -- Waterf0X")
                if chs == "continue searching":
                    continue
                if chs == "exit":
                    exit()
        if appinfo == "Info":
            gui.msgbox(msg = ve+"1.13"+"\n"+sp+"95.3M"+"\n"+de+"WATERF0X GRUOP", title = "HUGEHARD System", image = "/Users/jacobduan/Desktop/WORK/MY_NAME_IS_HACK-BETA/Images/waterf0x.gif")

#system
def syst():
    sysload()
    while True:
        sysapp = gui.choicebox(msg = "Welcome,"+userinfo, title = "HUGEHARD System", choices = ("Terminal", "Browser", "Exit"))
        if sysapp == "Terminal":
            ter()
        if sysapp == "Browser":
            bs()
        if sysapp == "Exit":
            exit()

#login
while True:
    lg = gui.buttonbox(msg = "Welcome to HUGEHARD SYSTEM\n\n\n\n\n\n\n\n\n\n\n\nUser list:", title = "HUGEHARD SYSTEM", choices = ("Admin: admin", "User: HACK", "Exit"))
    if lg == "Admin: admin":
        pswd = gui.passwordbox(msg = "Enter your password here:", title = "HUGEHARD System")
        if pswd == "admin":
            qx = "admin"
            nam = "admin"
            userinfo = qx+"-"+nam
            syst()
        else:
            if gui.ccbox(msg = "Your password is wrong", choices = ("Continue", "Exit")):
                continue
            else:
                exit()
    if lg == "User: HACK":
        qx = "user"
        nam = "HACK"
        userinfo = qx+"-"+nam
        syst()
    if lg == "Exit":
        exit()
