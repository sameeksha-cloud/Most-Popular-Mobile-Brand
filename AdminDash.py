from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import pandas as pd
import sys
from add_details import AddDetails
from cstmr_details import Cstmr_info
from srchbymodelno import SearchModel
from search_datewise import TblDemo
from search_brand import Search
from delete import Delete
from update_data import Update
from charts.best_mobile import BestBrand
from Email.RandomEmail import Read
from charts.sold_mbl import PieChart


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("AdminDash.ui",self)
        self.mbladd.triggered.connect(lambda:self.loadFrame(self.mbladd))
        self.cstmradd.triggered.connect(lambda:self.loadFrame(self.cstmradd))
        self.mblsearchmodel.triggered.connect(lambda:self.loadFrame(self.mblsearchmodel))
        self.mblsearch.triggered.connect(lambda:self.loadFrame(self.mblsearch))
        self.mbldelete.triggered.connect(lambda:self.loadFrame(self.mbldelete))
        self.mblupdate.triggered.connect(lambda:self.loadFrame(self.mblupdate))
        self.mblchart.triggered.connect(lambda:self.loadFrame(self.mblchart))
        self.mblpie.triggered.connect(lambda:self.loadFrame(self.mblpie))
        self.mblsold.triggered.connect(lambda:self.loadFrame(self.mblsold))
        self.email.triggered.connect(lambda:self.loadFrame(self.email))

    def loadFrame(self,menuitem):
        caption=menuitem.text()
        print(caption)
        if caption=="MobileDetails":
            self.m=AddDetails()
            self.m.show()
        if caption=="CustomerDetails":
            self.c =Cstmr_info()
            self.c.show()
        if caption=="byModelno.":
            self.s=SearchModel()
            self.s.show()
        if caption=="MobileUpdate":
            self.u=Update()
            self.u.show()
        if caption=="MobileDelete":
            self.d=Delete()
            self.d.show()
        if caption=="soldMobile":
            self.sl=TblDemo()
            self.sl.show()
        if caption=="barchart":
            bestselling = pd.read_excel("mblselling.xlsx", sheet_name="selling")
            self.b=BestBrand()
            self.b.showChart()
        if caption=="piechart":
            self.p=PieChart()
            self.p.show()
        if caption=="byBrand":
            self.br=Search()
            self.br.show()
        if caption=="CustomerMail":
            self.r=Read()
            self.r.fetchmail()
def main():
        app=QApplication(sys.argv)
        tm=Main()
        tm.show()
        app.exec_()
if __name__ == '__main__':main()