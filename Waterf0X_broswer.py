import easygui as gui

while True:
    web = gui.enterbox(msg = "Welcome to Waterf0X broswer, type the website here", title = "Waterf0X")
    if web == "10.10.10.14/23":
        gui.msgbox(msg = "PROBLEM\nNo.23\nThe account cannot be hack might because the account has protect by some encrypt system that we don't know, until this encrypt system's source code is open to us, the hack might be succed", title = "Waterf0X")
        
    else:
        chs = gui.choicebox(msg = "Can't found the server, continue?", choices = ["continue", "exit"], title = "Waterf0X")
        if chs == "continue":
            continue
        if chs == "exit":
            exit()

