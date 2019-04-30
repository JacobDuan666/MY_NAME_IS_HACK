# -*- coding: utf8 -*-

#调用模块
import math
import sys
import easygui as gui
from tkinter import Tk

#授权
print("PYTHON LOGIN SYSTEM\nPOWER BY JACOBDUAN")

#界面
signup = gui.passwordbox(msg = "If you don't havce the code send a email to jacobduan2022@163.com to get the code", title = "Python login system")
if signup == "Join":
      jos = gui.passwordbox(msg = "Type signin if you have an account, type sighup if you don't have an account", title = "Python login system")
      if jos == "signup":
            gui.msgbox(msg = "Welcome to Pythom login system\nLogin succesfully", title = "Python login system")
            gui.enterbox(msg = "Welcome to Python login system \nEnter your name(Can be your fake name)", title = "Python login system")
            gui.enterbox(msg = "Now type your email here and the system will send you an email", title = "Python login system")
            gui.msgbox(msg = "MESAAGE:\n\nSend by jacobduan2022@163.com\nYour password is V2NE7W", title = "Email simulater")
            getpasswd = gui.passwordbox(msg = "Check your email to get your own user password, you can change it after this, the email should be send", title = "Python login system")
            if getpasswd == "V2NE7W":
                  gui.msgbox(msg = "Complete!", title = "Python login system")
                  gui.enterbox(msg = "Now you can change your user password, if you don't want to change it, press cancel to skip this step", title = "Python login system")
                  gui.msgbox(msg = "Check your email for thr verify email", title = "Python login system")
                  gui.enterbox(msg = "Now type your email here and the system will send you an email", title = "Python login system")
                  gui.msgbox(msg = "MESSAGE:\n\nSend by jacobduan2022@163.com\nYour code is F67NM", title = "Email simulater")
                  verify = gui.passwordbox(msg = "Type the code of email verify here", title = "Python login system")
                  if verify == "F67NM":
                        gui.msgbox(msg = "Complete!\nThis will be your password", title = "Python login system")
                        gui.msgbox(msg = "Complete signup?", title = "Python login system")
                        gui.msgbox(msg = "connecting to 10.21.23.12 for checking the account...\nComplete", title = "Python login system")
                        gui.msgbox(msg = "Your account cannot be used, please use other email account for sign up", title = "Python login system")
                        gui.msgbox(msg = "Welcome to Pythom login system\nLogin succesfully", title = "Python login system")
                        gui.enterbox(msg = "Welcome to Python login system \nEnter your name(Can be your fake name)", title = "Python login system")
                        gui.enterbox(msg = "Now type your email here and the system will send you an email", title = "Python login system")
                        gui.msgbox(msg = "MESAAGE:\n\nSend by jacobduan2022@163.com\nYour password is V2NE7W", title = "Email simulater")
                        getpasswd2 = gui.passwordbox(msg = "Check your email to get your own user password, you can change it after this, the email should be send", title = "Python login system")
                        if getpasswd2 == "W2NX8D":
                              gui.msgbox(msg = "")