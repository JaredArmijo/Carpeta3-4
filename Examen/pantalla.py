# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pantalla.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.Qt import QSqlDatabase
import sqlite3
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_viewdata = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_viewdata.setObjectName("pushButton_viewdata")
        self.verticalLayout.addWidget(self.pushButton_viewdata)
        self.pushButton_addRow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.verticalLayout.addWidget(self.pushButton_addRow)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.verticalLayout.addWidget(self.pushButton_deleteRow)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_viewdata.setText(_translate("MainWindow", "View Data"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.pushButton_deleteRow.setText(_translate("MainWindow", "Delete Row"))

        
 #

        self.create_DB()
        self.pushButton_viewdata.clicked.connect(self.print_data)
        self.model = None
        self.pushButton_viewdata.clicked.connect(self.sql_table_view_model)
        self.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.pushButton_deleteRow.clicked.connect(self.sql_delete_row)
        
    def sql_delete_row(self):
        try:
            if self.model:
                self.model.removeRow(self.tableView.currentIndex().row())
            else:
                self.sql_tableview_model
        except Exception as e:
            print(e)
            
    def sql_add_row(self):
        try:
            if self.model:
                self.model.insertRows(self.model.rowCount(),1)
            else:
                self.sql_tableview_model()
        except Exception as e:
            print(e)
                 
    def sql_table_view_model(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('Invoices.db')
            
            tableview=self.tableView
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('invoices')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "InvoiceId")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "CustomerId")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "InvoiceDate")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "BillingAddress")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "BillingCity")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "BillingState")
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, "BillingCountry")
            self.model.setHeaderData(7, QtCore.Qt.Horizontal, "BillingPostalCode")
            self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Total")
        except Exception as e:
            print(e)
            
    def print_data(self):
        try:
            sqlite_file='Invoices.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'invoices' ORDER BY InvoiceId")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(e)
            
        
        
    def create_DB(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('Invoices.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table invoices(InvoiceId int primary key,"
                            "CustomerId int,InvoiceDate varchar(30), BillingAddress varchar(30), BillingCity varchar(30), BillingState varchar(30), BillingCountry varchar(30), BillingPostalCode varchar(30), Total int)")
            query.exec_("insert into invoices values(500,'2514','29','Dolores calle 3','Mexico','Gto','jsj','2525252525', 555)")
           
        except Exception as e:
            print(e)
              



        #-------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
