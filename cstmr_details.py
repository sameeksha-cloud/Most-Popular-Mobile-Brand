from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from db.dboperation import DbConnection as dbc
from PyQt5 import QtGui
import sys


class Cstmr_info(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("cstmr_details.ui", self)
        self.con = dbc.CreateConnection()
        self.mycursor = self.con.cursor()
        self.btnok.clicked.connect(self.info)
        pixmap = QtGui.QPixmap("img6.jpg")
        self.label_image.setPixmap(pixmap)

    def info(self):
        self.md= self.txtnm.text().strip()
        self.qnty = self.txtqnty.text().strip()
        self.nm= self.txtname.text().strip()
        self.em = self.txtemail.text().strip()
        self.add= self.txtaddress.text().strip()
        self.ph= self.txtph.text().strip()
        self.date=self.txtdate.text().strip()


        if len(self.md)==0 or len(self.qnty)==0 or len(self.nm)==0 or len(self.em)==0 or len(self.add)==0 or len(self.ph)==0 or len(self.date)==0:
             self.showMessage("error","data needed")
        else:
         strinsert = "insert into sales(ModelNumber, Quantity, CustomerName, Email, Address, Phone, Date)values(%s,%s,%s,%s,%s,%s,%s)"
         self.mycursor.execute(strinsert,(self.md,self.qnty,self.nm,self.em,self.add,self.ph,self.date))
         self.con.commit()
         self.showMessage("insertion","data added sucessfully")

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    frame = Cstmr_info()
    frame.show()
    app.exec_()


if __name__ == '__main__': main()

