from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from db.dboperation import DbConnection as dbc
import sys

class SearchModel(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("srchby_modelno..ui", self)
        self.con = dbc.CreateConnection()
        self.mycursor=self.con.cursor()
        self.btnclick.clicked.connect(self.fetchdata)
    def fetchdata(self):
        md=self.txtno.text()
        print(md)
        searchmd=(md,)
        strsql="select* from modeldetails where ModelNumber=%s"
        self.mycursor.execute(strsql,searchmd)
        dataset=self.mycursor.fetchone()
        print(type(dataset))
        chk=self.mycursor.rowcount
        if chk>0:
            print("is exists")
            print(dataset[1])
            print(dataset[2])
            print(dataset[3])
            print(dataset[4])
            print(dataset[5])

            self.txtbrandid.setText(dataset[1])
            self.txtname.setText(dataset[2])
            self.txtprice.setText(str(dataset[3]))
            self.txtfeatures.setText(dataset[4])
            self.txtquantity.setText(str(dataset[5]))
        else:
            msg = QMessageBox()
            msg.setWindowTitle("error")
            msg.setText("id not exist")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            msg.exec_()




def main():
    app=QApplication(sys.argv)
    frame=SearchModel()
    frame.show()
    app.exec_()
if __name__ == '__main__':
    main()