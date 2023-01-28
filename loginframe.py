from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import sys
import imgresource
from AdminDash import Main

class MyLogin(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("loginframe.ui", self)
        self.btnlogin.clicked.connect(self.checklogin)

    def checklogin(self):
        ui=self.txtuser.text()
        upass=self.txtpswd.text()

        if ui =="shop" and upass =="123":
            self.ad=Main()
            self.ad.show()
            self.close()
            print("login successful")

        else:
            msg = QMessageBox()
            msg.setWindowTitle("errormessage")
            msg.setText("invalid userid\password")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setDetailedText("incorrect userid and password")
            # msg.buttonClicked.connect(self.checkButton)
            msg.show()
            msg.exec_()

def main():
    app = QApplication(sys.argv)
    frame = MyLogin()
    frame.show()
    app.exec_()

if __name__ == '__main__':
    main()





