# -*- coding: utf8 -*-

#模块区
import math
import sys
import easygui as gui
from tkinter import Tk

#授权区
print("PYTHON LOGIN SYSTEM\nPOWER BY JACOBDUAN")

#定义区
otz = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] #1 - 0

#函数区
#登陆
def login(user_list):
      lock_list = []
      lock = []
      name = gui.enterbox(msg = "Your account or your sign up email", title = "Python login system")
      password = gui.passwordbox(msg = "Password:", title = "Python login system")
      if name in lock_list:
            gui.msgbox(msg = "This account has been locked, please use another account", title = "Python login system")
      if [name, password] in user_list:
            gui.msgbox(msg = "Login sucsessfully", title = "Python login system")
      else:
            lock.append(name)
            gui.msgbox(msg = "Are you guessing the password? No more try!!!", title = "Python login system")
            exit()
            if lock.count(name) == 3:
                  lock_list.append(name)
                  gui.msgbox(msg = "Now you are in lock_list, bro, suprise", title = "Python login system")
                  exit()
#主界面
def ps():
      gui.choicebox(msg = "Welcome to Python login system", choices = ["Document", "Tools", "Question", "Help"], title = "Python login system")
            
                  
if __name__ == "__main__":
    user_list = [["jacobduan666@outlook.com", "1433233"], ["admin", "admin"], ["test", "test"]]

#界面区
signup = gui.passwordbox(msg = "If you don't have the code send a email to pythonloginsys@pls.com to get the code", title = "Python login system")
if signup == "join":
      jos = gui.choicebox(msg = "Signin if you have an account, sighup if you don't have an account", choices = ["I have an account", "I don't have an account", "I forgot my password"], title = "Python login system")
      if jos == "I don't have an account":
            gui.msgbox(msg = "Welcome to Pythom login system", title = "Python login system")
            msg = "Signup account for Python login system"
            title = "Python login sytem"
            fieldNames = ["Username: ", "Email: ", "Password: ", "Verify code: \n [FN7G5]"]
            fieldValues = []
            fieldValues = gui.multenterbox(msg, title, fieldNames, fieldValues)
            gui.msgbox(msg = "We are cheking your account, please wait..\nConnecting to 10.1.12.3...\nConnecting complete", title = "Python login system")
            gui.msgbox(msg = "Complete!", title = "Python login system")
            gui.msgbox(msg = "connecting to 10.1.12.24 for checking the account...\nComplete", title = "Python login system")
            gui.msgbox(msg = "Your account cannot be used, please use other email account for sign up", title = "Python login system")
      if jos == "I have an account":
            login(user_list)



#设定备注
#Python login system:
#10.1.12.3是主服务器服务器
#10.1.12.24是安全检查的服务器
