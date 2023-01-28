from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
import pyttsx3 as p
import sys

from loginframe import MyLogin
def main():
    app=QApplication(sys.argv)

    splash_pix=QPixmap("img10.jpg")
    splash=QSplashScreen(splash_pix)
    splash.showFullScreen()

    current_window_flags=splash.windowFlags()
    splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|current_window_flags)

    font=QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setPointSize(80)
    splash.setFont(font)
    message=" APP WELCOME YOU"

    #to write sm text alomg with the welcome
    splash.showMessage(message,QtCore.Qt.AlignCenter | QtCore.Qt.AlignBaseline,QtGui.QColor.fromRgb(100,100,100,))

    # splash.setMask(splash_pix.mask())
    # splash.showFullScreen()

    splash.show()
    app.processEvents()
    import time
    time.sleep(2)

    engine = p.init()  # object creation
    engine.setProperty("rate",150)

    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.say("App Welcomes you")
    engine.runAndWait()
    engine.stop()

    login = MyLogin()
    login.show()
    splash.finish(login)
    app.exec_()

if __name__ == '__main__':
    main()