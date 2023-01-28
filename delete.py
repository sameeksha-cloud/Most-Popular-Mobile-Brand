from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
from db.dboperation import DbConnection as dbc
import imgresource
class Delete(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("delete.ui",self)
        self.con=dbc.CreateConnection()
        self.mycursor=self.con.cursor()
        self.btndel.clicked.connect(self.delete)

    def delete(self):
        self.mn=self.txtmn.text()
        if len(self.mn)==0:
            self.showmessage("error","data needed")

        else:
            self.idcheck=self.searchId(self.mn)
            if self.idcheck>0:
                strdelete="delete from modeldetails where ModelNumber=%s"
                modelnumber=(self.mn,)
                self.mycursor.execute(strdelete,modelnumber)
                self.con.commit()
                self.showmessage("deleted","data deleted")

            else:
                self.showmessage("error","no such id")

    def searchId(self,mn):
        strsearch="select ModelNumber from modeldetails where ModelNumber =%s"
        data=(self.mn,)
        self.mycursor.execute(strsearch,data)
        self.mycursor.fetchone()
        self.check=self.mycursor.rowcount
        return self.check

    def showmessage(self,title,message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.show()
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    frame = Delete()
    frame.show()
    app.exec_()

if __name__ == '__main__': main()