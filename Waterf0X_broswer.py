#-*- coding: utf-8 -*-
import easygui as gui
import sys

print("Waterf0X_broswer\nPOWER BY JACOBDUAN")

#界面以及网页
while True:
    web = gui.enterbox(msg = "Welcome to Waterf0X broswer, type the website here", title = "Waterf0X")
    if web == "pylogin.com/has_been_locked":
        gui.textbox(msg = "The user has been locked", text = "The user has been locked might be you don't have a account or your account is not safe, or your account has been hacked")
    if web == "10.10.10.14/23":
        gui.textbox(msg = "PROBLEM\nNo.8", text = "The account cannot be hack might because the account has protect by some encrypt system that we don't know, until this encrypt system's source code is open to us, the hack might be succed", title = "Waterf0X")
    if web == "tools.me":
        with open("log.txt") as f:
            f.write("tools.me-run")
        gui.textbox(msg = "tools.me\nCOPYRIGHT TOOLS.ME, HUGEHARD COMPANY", text = "Welcome to tools.me, there are a lot of free tools and fee-paying tools here", title = "Waterf0X")
        dl = gui.choicebox(msg = "Tools", choices = ["Waterf0X - Fast and simple broswer", "Mail Box - Fast speed email tools", "HTTP Catcher - Powerful HTTP catching tools"], title = "Waterf0X")
        if dl == "Waterf0X":
            gui.msgbox(msg = "You already download this application in your computer", title = "Waterf0X")
        else: 
            gui.msgbox(msg = "You already download this application in your computer", title = "Waterf0X")
    else:
        chs = gui.buttonbox(msg = "Can't found the server, continue?", choices = ["continue searching", "exit"], title = "Waterf0X")
        if chs == "continue searching":
            continue
        if chs == "exit":
            exit()

