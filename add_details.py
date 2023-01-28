from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from db.dboperation import DbConnection as dbc
import sys
import imgresource


class AddDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("Adddetails.ui", self)
        self.con = dbc.CreateConnection()
        self.mycursor = self.con.cursor()
        self.btnadd.clicked.connect(self.fetchData)

    def fetchData(self):
        self.md=self.txtid.text().strip()
        self.id=self.txtid.text().strip()
        self.nm=self.txtname.text().strip()
        self.f=self.txtfeatures.text().strip()
        self.p=self.txtprice.text().strip()
        self.q=self.txtquantity.text().strip()

        if len(self.md)==0 or len(self.id)==0 or len(self.nm)==0 or len(self.f)==0 or len(self.f)==0 or len(
                self.p)==0 or len(self.q)==0:
            self.showMessage("error", "data needed")
        else:
            strinsert = "insert into modeldetails(ModelNumber,BrandId, ModelName, Price, Features, Quantity)values(%s,%s,%s,%s,%s,%s)"
            self.mycursor.execute(strinsert, (self.md,self.id, self.nm, self.p, self.f, self.q))
            self.con.commit()
            self.showMessage("insertion", "data added sucessfully")

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.show()
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    frame = AddDetails()
    frame.show()
    app.exec_()


if __name__ == '__main__': main()

