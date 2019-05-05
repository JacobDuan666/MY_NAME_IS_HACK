# -*- coding: utf8 -*-

#模块区
import easygui as gui

#授权区
print("PYTHON LOGIN SYSTEM\nPOWER BY JACOBDUAN")

#定义区
otz = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] #1 - 0

#函数区
#登陆
def login(user_list):
      lock_list = ["hacksmltr@mail.com"]
      lock = []
      name = gui.enterbox(msg = "Your account or your sign up email", title = "Python login system")
      password = gui.passwordbox(msg = "Password:", title = "Python login system")
      if name in lock_list:
            gui.msgbox(msg = "This account has been locked, please use another account, please check pylogin.com/has_been_locked for more information", title = "Python login system")
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
      while True:
            cui = gui.choicebox(msg = "Welcome to Python login system", choices = ["Tools", "Help", "Copyright", "Exit"], title = "Python login system")
            if cui == "Tools":
                  gui.msgbox(msg = "Welcome to Python tools system", title = "Python login system")
                  gui.msgbox(msg = "Please go to tools.me to get more free tools", title = "Python login system")
                  continue
            if cui == "Help":
                  gui.msgbox(msg = "Welcome to Python Help system", title = "Python login system")
                  ge = gui.choicebox(msg = "Help system", title = "Python login system", choices = ["No.1: Application guide", "No.2: About HUGEHARD System", "No.3: About this game"])
                  if ge == "No.1: Application guide":
                        gui.msgbox(msg = "No.1\nApplication guide\nEvery application is useful in this system, if you don't know how to use them, please read README.md in the folder of the application or the introduction of the application\nSome application might need the key, you need to buy it or contact the developer for the key", title = "Python login system")
                  if ge == "No.2: About HUGEHARD System":
                        gui.msgbox(msg = "No.2\nAbout HUGEHARD System\nCOPYRIGHT HUGEHARD 2019\nThe System's interface is very simple and easy to use. The whole system have 1042 ports, you can open any port if you want, open them in your terminal. Type 'help' in your terminal to get the code", title = "Python login system")
                  if ge == "No.3: About this game":
                        gui.msgbox(msg = "No.3\nAbout this game\nThe game is made by jacobduan666@outlook.com, his wechat is king20051209, email is jacobduan666@outlook.com, more information please look at Readme.md which is in the same folder of this game, have fun!!!", title = "Python login system")
                  continue
            if cui == "Copyright":
                  gui.msgbox(msg = "Copyright\nCOPYRIGHT JACOBDUAN PERSONAL, ALL RIGHTS RESERVED", title = "Python login system")
                  continue
            if cui == "Exit":
                  exit()

if __name__ == "__main__":
    user_list = [["jacobduan666@outlook.com", "1433233"], ["admin", "admin"], ["test_user", "test"]]

#界面区
signup = gui.passwordbox(msg = "If you don't have the code send a email to pythonloginsys@pls.com to get the code", title = "Python login system")
if signup == "join":
      jos = gui.choicebox(msg = "Signin if you have an account, sighup if you don't have an account", choices = ["I have an account", "I don't have an account", "I forgot my password"], title = "Python login system")
      if jos == "I don't have an account":
            gui.msgbox(msg = "Welcome to Pythom login system", title = "Python login system")
            msg = "Signup account for Python login system"
            title = "Python login sytem"
            fieldNames = ["Username: ", "Email: ", "Password: ", "Verify code: \n[FN7G5]"]
            fieldValues = []
            fieldValues = gui.multenterbox(msg, title, fieldNames, fieldValues)
            gui.msgbox(msg = "We are cheking your account, please wait..\nConnecting to 10.1.12.3...\nConnecting complete", title = "Python login system")
            gui.msgbox(msg = "Complete!", title = "Python login system")
            gui.msgbox(msg = "connecting to 10.1.12.24 for checking the account...\nComplete", title = "Python login system")
            gui.msgbox(msg = "Your account cannot be used, please use other email account for sign up", title = "Python login system")
      if jos == "I have an account":
            login(user_list)
            ps()
      if jos == "I forgot my password":
            em = gui.enterbox(msg = "Type your signup email here and the system will send you a verify email for reset your password", title = "Python login system")
            if em == "hacksmltr@mail.com":
                  gui.msgbox(msg = "Your account has been locked by the system, go to 'pylogin.com/has_been_locked' for more information", title = "Python login system")
            if em == "jacobduan666@outlook.com":
                  gui.msgbox(msg = "System already send you an email for last 30 days, you cannot get a verify email until after 30 days", title = "Python login system")
            else:
                  gui.msgbox(msg = "The email should be send, please check your email for the verify email", title = "Python login system")
            
#设定备注
#Python login system:
#10.1.12.3是主服务器服务器
#10.1.12.24是安全检查的服务器
