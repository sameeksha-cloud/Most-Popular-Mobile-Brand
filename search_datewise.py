from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import sys


from db.dboperation import DbConnection as dbc
class TblDemo(QFrame):
    def __init__(self):
        super().__init__()
        loadUi("SoldMobile.ui",self)
        self.con = dbc.CreateConnection()
        self.mycursor = self.con.cursor()
        self.populateTable()
    def populateTable(self):
        strsql="select Date,ModelNumber from sales"
        self.mycursor.execute(strsql)
        dataset=self.mycursor.fetchall()
        rownum=0
        for row in dataset:
            for column in range(len(row)):
                print(row[column])
                self.tbl.setItem(rownum,column,QTableWidgetItem(str(row[column])))
            rownum=rownum+1


def main():
    app=QApplication([])
    t=TblDemo()
    t.show()
    app.exec_()

if __name__ == '__main__':
    main()

