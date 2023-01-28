from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
from db.dboperation import DbConnection as dbc
from PyQt5 import QtGui


class Update(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("update.ui", self)
        self.con=dbc.CreateConnection()
        self.mycursor=self.con.cursor()
        self.btnupdate.clicked.connect(self.checkupdate)
        pixmap = QtGui.QPixmap("img5.jpg")
        self.lbl_image.setPixmap(pixmap)

    def checkupdate(self):
        self.mn=self.txtmn.text()
        self.pr=self.txtprice.text()
        self.qnty=self.txtquantity.text()
        strupdate="update modeldetails set  Price=%s,Quantity=%s where ModelNumber=%s"
        self.mycursor.execute(strupdate,(self.pr,self.qnty,self.mn))
        self.con.commit()

        if len(self.mn)==0 or len(self.pr)==0 or len(self.qnty)==0:
              self.showmessage("error","data needed")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("successful")
            msg.setText("data updated")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.show()
            msg.exec_()

    def showmessage(self,title,message):
         msg = QMessageBox()
         msg.setWindowTitle("errormessage")
         msg.setText("invalid userid\password")
         msg.setStandardButtons(QMessageBox.Ok)
         msg.setDefaultButton(QMessageBox.Ok)
         msg.show()
         msg.exec_()

def main():
    app=QApplication(sys.argv)
    frame=Update()
    frame.show()
    app.exec_()

if __name__ == '__main__':
    main()
