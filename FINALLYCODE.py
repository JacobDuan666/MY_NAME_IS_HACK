import easygui as gui

print("FINALLYCODE\nPOWER BY JACOBDUAN")

THISCODEISWRONG = "THISCODEISRIGHT"

code = gui.passwordbox(msg = "ENTER THE CODE TO WIN THIS STUPID GAME", title = "FINALLYCODE")
if code == THISCODEISWRONG:
    gui.msgbox(msg = "YOU WIN THIS STUPID GAME\nBUT YOU ARE CATCHED BY THE POLICE :)", title  = "FINALLYCODE")
    gui.msgbox(msg = "END OF THIS GAME", title  = "FINALLYCODE")
    gui.msgbox(msg = "REALLY END", title  = "FINALLYCODE")
    gui.msgbox(msg = "DON'T LOOK YOU IDIOT", title  = "FINALLYCODE")
    gui.msgbox(msg = "OK, YOU WIN", title = "FIANLLYCODE")
if code == "THISCODEISWRONG":
    gui.msgbox(msg = "WHO TELLS YOU THISCODEISWRON", title = "FINALLYCODE")
