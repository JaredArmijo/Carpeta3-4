# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Video15.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget, QApplication
from PyQt5.Qt import QTcpServer, QHostAddress, QDataStream, QByteArray,\
    QIODevice, QTcpSocket, QSqlDatabase, QColor, QCalendarWidget
from PyQt5.QtCore import pyqtSignal, QPoint, Qt
import sqlite3
from pprint import pprint


#Globals
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 12345

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0,  x2:1, y2:0, stop:0\n"
"rgba(85, 170, 255, 255), stop:1 rgba(255,255,255,255));")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.animation = QtWidgets.QTabWidget(self.centralwidget)
        self.animation.setStyleSheet("")
        self.animation.setObjectName("animation")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 331, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 321, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget_2)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_2.addWidget(self.treeWidget)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_4)
        self.dateEdit.setGeometry(QtCore.QRect(0, 0, 321, 22))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 30, 321, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tab_signals_slots = QtWidgets.QWidget(self.tab_10)
        self.tab_signals_slots.setGeometry(QtCore.QRect(0, 10, 321, 221))
        self.tab_signals_slots.setObjectName("tab_signals_slots")
        self.button_slot = QtWidgets.QPushButton(self.tab_signals_slots)
        self.button_slot.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.button_slot.setObjectName("button_slot")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.animation.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 111, 111))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 114, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_5.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_5.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_5.addWidget(self.radioButton_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 20, 151, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.dial = QtWidgets.QDial(self.groupBox_2)
        self.dial.setGeometry(QtCore.QRect(0, 10, 50, 64))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 10, 71, 71))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(0, 250, 341, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab_2)
        self.fontComboBox.setGeometry(QtCore.QRect(10, 130, 188, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 160, 161, 71))
        self.label.setText("")
        self.label.setObjectName("label")
        self.animation.addTab(self.tab_2, "")
        self.tab_drag_drop = QtWidgets.QWidget()
        self.tab_drag_drop.setObjectName("tab_drag_drop")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_drag_drop)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 520, 194))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.listView = QtWidgets.QListView(self.layoutWidget1)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_drag_drop)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 10, 511, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        #self.comboBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox = DragDropCombo(MainWindow)

        
        self.comboBox.setMinimumSize(QtCore.QSize(111, 22))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        #self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)

        self.pushButton = DragDropButton('DropButton', MainWindow)
        
        self.pushButton.setAcceptDrops(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.animation.addTab(self.tab_drag_drop, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.frame_gl = QtWidgets.QFrame(self.tab_6)
        self.frame_gl.setGeometry(QtCore.QRect(20, 0, 491, 291))
        self.frame_gl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gl.setObjectName("frame_gl")
        self.animation.addTab(self.tab_6, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 211, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_client1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_client1.setGeometry(QtCore.QRect(10, 20, 191, 151))
        self.textEdit_client1.setObjectName("textEdit_client1")
        self.lineEdit_client1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_client1.setGeometry(QtCore.QRect(10, 180, 191, 20))
        self.lineEdit_client1.setObjectName("lineEdit_client1")
        self.button_client_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.button_client_1.setGeometry(QtCore.QRect(10, 210, 191, 23))
        self.button_client_1.setObjectName("button_client_1")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 20, 221, 261))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_client2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_client2.setGeometry(QtCore.QRect(20, 180, 201, 20))
        self.lineEdit_client2.setObjectName("lineEdit_client2")
        self.button_client_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.button_client_2.setGeometry(QtCore.QRect(20, 210, 201, 23))
        self.button_client_2.setObjectName("button_client_2")
        self.textEdit_client2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_client2.setGeometry(QtCore.QRect(10, 20, 201, 151))
        self.textEdit_client2.setObjectName("textEdit_client2")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget3.setGeometry(QtCore.QRect(250, 10, 77, 301))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_start_server = QtWidgets.QPushButton(self.layoutWidget3)
        self.button_start_server.setObjectName("button_start_server")
        self.verticalLayout_3.addWidget(self.button_start_server)
        self.animation.addTab(self.tab_5, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_7)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 10, 77, 112))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_viewdata = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_viewdata.setObjectName("pushButton_viewdata")
        self.verticalLayout_4.addWidget(self.pushButton_viewdata)
        self.pushButton_addRow = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.verticalLayout_4.addWidget(self.pushButton_addRow)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.verticalLayout_4.addWidget(self.pushButton_deleteRow)
        self.pushButton_createDB = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_createDB.setObjectName("pushButton_createDB")
        self.verticalLayout_4.addWidget(self.pushButton_createDB)
        
        self.tableview = QtWidgets.QTableView(self.tab_7)
        self.tableview.setGeometry(QtCore.QRect(90, 0, 421, 281))
        self.tableview.setObjectName("table_view")
        self.animation.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tab_animation = QtWidgets.QWidget(self.tab_8)
        self.tab_animation.setGeometry(QtCore.QRect(0, 0, 631, 321))
        self.tab_animation.setObjectName("tab_animation")
        self.frame_animation = QtWidgets.QFrame(self.tab_animation)
        self.frame_animation.setGeometry(QtCore.QRect(30, 10, 101, 71))
        self.frame_animation.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.frame_animation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_animation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_animation.setObjectName("frame_animation")
        self.toolButton = QtWidgets.QToolButton(self.tab_animation)
        self.toolButton.setGeometry(QtCore.QRect(280, 40, 41, 21))
        self.toolButton.setObjectName("toolButton")
        self.lcdNumber_animation = QtWidgets.QLCDNumber(self.tab_animation)
        self.lcdNumber_animation.setGeometry(QtCore.QRect(390, 20, 101, 71))
        self.lcdNumber_animation.setMouseTracking(False)
        self.lcdNumber_animation.setTabletTracking(False)
        self.lcdNumber_animation.setSmallDecimalPoint(False)
        self.lcdNumber_animation.setObjectName("lcdNumber_animation")
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_animation)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 170, 168, 25))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_start_animation = QtWidgets.QPushButton(self.layoutWidget5)
        self.button_start_animation.setObjectName("button_start_animation")
        self.horizontalLayout_4.addWidget(self.button_start_animation)
        self.button_stop_animation = QtWidgets.QPushButton(self.layoutWidget5)
        self.button_stop_animation.setObjectName("button_stop_animation")
        self.horizontalLayout_4.addWidget(self.button_stop_animation)
        self.animation.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tab_CSS = QtWidgets.QWidget(self.tab_9)
        self.tab_CSS.setGeometry(QtCore.QRect(0, 0, 641, 331))
        self.tab_CSS.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 0, 127);\n"
"}\n"
"QPushButton#pushButton_11{\n"
"background-color:rgb(255, 85, 255)\n"
"}")
        self.tab_CSS.setObjectName("tab_CSS")
        self.layoutWidget6 = QtWidgets.QWidget(self.tab_CSS)
        self.layoutWidget6.setGeometry(QtCore.QRect(110, 10, 77, 54))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_6.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_6.addWidget(self.pushButton_12)
        self.layoutWidget7 = QtWidgets.QWidget(self.tab_CSS)
        self.layoutWidget7.setGeometry(QtCore.QRect(20, 10, 77, 54))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget7)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_7.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget7)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_7.addWidget(self.pushButton_10)
        self.animation.addTab(self.tab_9, "")
        self.horizontalLayout_3.addWidget(self.animation)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.animation.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(2)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        #self.radioButton_3.clicked.connect(self.progressBar.reset)


        #------------DB-------------------------------------------------
        self.create_DB()
        self.pushButton_viewdata.clicked.connect(self.print_data)
        self.model = None
        self.pushButton_viewdata.clicked.connect(self.sql_table_view_model)
        self.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.pushButton_deleteRow.clicked.connect(self.sql_delete_row)
        
    def sql_delete_row(self):
        try:
            if self.model:
                self.model.removeRow(self.tableview.currentIndex().row())
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
            db.setDatabaseName('PEOPLE.db')
            
            tableview=self.tableview
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('PERSON')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First Name")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last Name")
        except Exception as e:
            print(e)
            
    def print_data(self):
        try:
            sqlite_file='PEOPLE.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'PERSON' ORDER BY ID")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(e)
            
        
        
    def create_DB(self):
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('PEOPLE.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table PERSON(ID int primary key,"
                            "FIRST_NAME varchar(20), LAST_NAME  varchar(20))")
            query.exec_("insert into PERSON values(1000, 'Albert', 'Einstein' )")
            query.exec_("insert into PERSON values(1001, 'Guido', 'Van Rossum' )")
            query.exec_("insert into PERSON values(1002, 'Steve', 'Jobs' )")
            query.exec_("insert into PERSON values(1003, 'Bill', 'Gates' )")
        except Exception as e:
            print(e)

        #-------------------------Animacion----------
        self.button_stop_animation.clicked.connect(self.stop_animation) 
        self.button_start_animation.clicked.connect(self.animate) 
        
        
        self.toolButton.hide()
        self.move_toolbutton = MoveToolButton(self.tab_8)
        self.move_toolbutton.setGeometry(QtCore.QRect(330,20,25,19))
        self.move_toolbutton.setAutoFillBackground(True)
        self.move_toolbutton.setText("***")
        
        

        self.radioButton_3.clicked.connect(self.reset_progressbar)
        self.radioButton_2.clicked.connect(self.start_progressbar)
        self.radioButton.clicked.connect(self.stop_progressbar)
        self.progress_value= 0
        self.stop_progress = False

        
        self.fontComboBox.activated['QString'].connect(self.label.setText)
        #self.button_slot.clicked.connect(MainWindow.slot1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
        open_gl = PyQtOpenGL(parent= self.frame_gl)
        open_gl.setMinimumSize(300, 300)
        open_gl.paint_0= True
        open_gl.paint_1= True
        open_gl.resize_lines= True
        open_gl.paint_rotation = True



        self.button_start_server.clicked.connect(self.start_server)
        self.lineEdit_client1.returnPressed.connect(self.send_data_1)
        self.button_client_1.clicked.connect(self.connect_to_server_1)
        self.lineEdit_client2.returnPressed.connect(self.send_data_2)
        self.button_client_2.clicked.connect(self.connect_to_server_2)

        #--------------------------boton slot-----------
        def slot1():
            print('hi from slot1')
            self.button_slot.setText('slot1')
        
        MainWindow.slot1 = slot1
        self.button_slot.clicked.connect(MainWindow.slot1)

       
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Header 1"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tree"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Calendar"))
        self.button_slot.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Signals & Slots"))
        self.animation.setTabText(self.animation.indexOf(self.tab), _translate("MainWindow", "Widget 1"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.radioButton_2.setText(_translate("MainWindow", "Start"))
        self.radioButton.setText(_translate("MainWindow", "Stop"))
        self.radioButton_3.setStatusTip(_translate("MainWindow", "This is option 2"))
        self.radioButton_3.setText(_translate("MainWindow", "Reset"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.animation.setTabText(self.animation.indexOf(self.tab_2), _translate("MainWindow", "Widget 2"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Item 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Item 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Item 3"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.animation.setTabText(self.animation.indexOf(self.tab_drag_drop), _translate("MainWindow", "Drag && Drop"))
        self.animation.setTabText(self.animation.indexOf(self.tab_6), _translate("MainWindow", "Open Gl"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Client 1"))
        self.button_client_1.setText(_translate("MainWindow", "Connect to Server"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Client 2"))
        self.button_client_2.setText(_translate("MainWindow", "Connect to Server"))
        self.button_start_server.setText(_translate("MainWindow", "Start Server"))
        self.animation.setTabText(self.animation.indexOf(self.tab_5), _translate("MainWindow", "Network"))
        self.pushButton_viewdata.setText(_translate("MainWindow", "View Data"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.pushButton_deleteRow.setText(_translate("MainWindow", "Delete Row"))
        self.pushButton_createDB.setText(_translate("MainWindow", "Create DB"))
        self.animation.setTabText(self.animation.indexOf(self.tab_7), _translate("MainWindow", "SQL"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.button_start_animation.setText(_translate("MainWindow", "Start animation"))
        self.button_stop_animation.setText(_translate("MainWindow", "Stop animation"))
        self.animation.setTabText(self.animation.indexOf(self.tab_8), _translate("MainWindow", "Animation"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.animation.setTabText(self.animation.indexOf(self.tab_9), _translate("MainWindow", "CSS"))

        #--------------Animation
    def stop_animation(self):
        try:
            self.animated_frame.stop()
            self.animated_lcd.stop()
            self.animated_toolbutton.stop()
        except Exception as e:
            print(e)
    
    def animate(self):
        try:
            self.animated_frame = QtCore.QPropertyAnimation(self.frame_animation, b'geometry')
            self.animated_frame.setDuration(10000)
            self.animated_frame.setStartValue(QtCore.QRect(10,10,100,100))
            self.animated_frame.setEndValue(QtCore.QRect(10,10,200,200))
            self.animated_frame.start()
            self.animated_frame.finished.connect(lambda: self.frame_animation.setFrameStyle(QtWidgets.QFrame.Box))
            
            self.animated_lcd = QtCore.QPropertyAnimation(self.lcdNumber_animation, b'value')
            self.animated_lcd.setDuration(9000)
            self.animated_lcd.setStartValue(0)
            self.animated_lcd.setEndValue(999)
            self.animated_lcd.start()
            self.animated_lcd.finished.connect(lambda: self.lcdNumber_animation.setFrameStyle(QtWidgets.QFrame.StyledPanel))
            
            self.move_toolbutton.change_palette()
            self.animated_toolbutton =QtCore.QPropertyAnimation(self.move_toolbutton, b'new_position')
            self.animated_toolbutton.setDuration(9000)
            self.animated_toolbutton.setStartValue(QtCore.QPoint(330, 20))
            self.animated_toolbutton.setKeyValueAt(0.2, QtCore.QPoint(398, 50))
            self.animated_toolbutton.setKeyValueAt(0.5, QtCore.QPoint(152, 120))
            self.animated_toolbutton.setKeyValueAt(0.6, QtCore.QPoint(420, 240))
            self.animated_toolbutton.setKeyValueAt(0.7, QtCore.QPoint(420, 260))
            self.animated_toolbutton.setKeyValueAt(0.9, QtCore.QPoint(330, 330))
            self.animated_toolbutton.setKeyValueAt(0.99, QtCore.QPoint(330, 310))
            self.animated_toolbutton.setEndValue(QtCore.QPoint(490,300))
            self.animated_toolbutton.start()
            
            self.animated_toolbutton.finished.connect(lambda: self.move_toolbutton.change_palette(QColor("#00aa00"), QColor("#00aa00")))
        except Exception as e:
            print(e)

                    
        
    #------------------------------Botones reset, start, stop---------------
    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.progressBar.value()
        while (self.progress_value <= 100.1) and not (self.stop_progress):
            self.progressBar.setValue(self.progress_value)
            self.progress_value += 0.0001
            QtWidgets.QApplication.processEvents()
            
    def stop_progressbar(self):
        self.stop_progress = 100
        
    def reset_progressbar(self):
        self.progress_value = 0
        self.progressBar.reset()
        self.stop_progress = False


   
    
    #----------------Cliente/Servidor--------------------------------

    def connect_to_server_1(self):
        try:
            self.tcp_client_1 = TcpClient(line_edit_widget=self.lineEdit_client1, text_widget=self.textEdit_client1)
            self.tcp_client_1.connect_server()
            self.button_client_1.setEnabled(False)
            
            self.tcp_client_1.socket.readyRead.connect(self.tcp_client_1.read_data)
            self.tcp_client_1.socket.disconnected.connect(self.server_disconnect_1)
            self.tcp_client_1.socket.error.connect(self.server_error_1)
        except Exception as e:
            print(e)
            
    def server_disconnect_1(self):
        try:
            self.tcp_client_1.socket.close()
            self.button_client_1.setEnabled(True)
        except Exception as e:
            print(e)
    
    def server_error_1(self):
        try:
            error ='Error {}'.format(self.tcp_client_1.socket.errorString())
            self.display_text_1(error)
            self.tcp_client_1.socket.close()
            self.button_client_1.setEnabled(True)
        except Exception as e:
            print(e)
        
    def display_text_1(self, text):
        self.textEdit_client1.append(text)
        
    def send_data_1(self):
        try:
           self.tcp_client_1.write_data()
        except Exception as e:
            print(e)
        
        
    
    def connect_to_server_2(self):
        try:
            self.tcp_client_2 = TcpClient(line_edit_widget=self.lineEdit_client2, text_widget=self.textEdit_client2)
            self.tcp_client_2.connect_server()
            self.button_client_2.setEnabled(False)
            
            self.tcp_client_2.socket.readyRead.connect(self.tcp_client_2.read_data)
            self.tcp_client_2.socket.disconnected.connect(self.server_disconnect_2)
            self.tcp_client_2.socket.error.connect(self.server_error_2)
        except Exception as e:
            print(e)
            
    def server_disconnect_2(self):
        try:
            self.tcp_client_2.socket.close()
            self.button_client_2.setEnabled(True)
        except Exception as e:
            print(e)
    
    def server_error_2(self):
        try:
            error ='Error {}'.format(self.tcp_client_2.socket.errorString())
            self.display_text_2(error)
            self.tcp_client_2.socket.close()
            self.button_client_2.setEnabled(True)
        except Exception as e:
            print(e)
        
    def display_text_2(self, text):
        self.textEdit_client1.append(text)
        
    def send_data_2(self):
        self.tcp_client_2.write_data()

    def start_server(self):
        self.tcp_server = TcpServer()
        
        
        
class TcpServer():
    def __init__(self):
        try:
            self.tcp_server =QTcpServer()
            self.tcp_server.listen(QHostAddress(SERVER_ADDRESS), SERVER_PORT)
            self.tcp_server.newConnection.connect(self.connect_client)
            self.clients =[]
        except Exception as e:
            print(e)
        
    def connect_client(self):
        try:
            
            client_socket = self.tcp_server.nextPendingConnection()
            self.clients.append(client_socket)
            client_socket.readyRead.connect(self.read_data)
        except Exception as e:
            print(e)
        
    def read_data(self):
        try:
            
            for client_id, client_socket in enumerate(self.clients):
                if client_socket.bytesAvailable() > 0:
                    stream = QDataStream(client_socket)
                    stream.setVersion(QDataStream.Qt_5_9)
                    stream.readUInt32()
                    client_data= stream.readQString()
                    self.return_data_to_clients(client_id, client_data)
        except Exception as e:
            print(e)
                
    def return_data_to_clients(self, client_id, data):
        try:
            for client_socket in self.clients:
                return_data_string = 'Client {} sent: {}'.format(client_id, data)
                data_byte_array =QByteArray()
                stream =QDataStream(data_byte_array, QIODevice.WriteOnly)
                stream.setVersion(QDataStream.Qt_5_9)
                stream.writeUInt32(0)
                stream.writeQString(return_data_string)
                client_socket.write(data_byte_array)
        except Exception as e:
            print(e)
            
class TcpClient():
    def __init__(self, line_edit_widget=None, text_widget=None):
        try:
            self.line_edit = line_edit_widget
            self.text_widget= text_widget
            self.socket =QTcpSocket()
        except Exception as e:
            print(e)
        
    def connect_server(self):
        try:
            
            print('inside connect_server')
            self.socket.connectToHost(SERVER_ADDRESS, SERVER_PORT)
        except Exception as e:
            print(e)
        
    def write_data(self):
        try:

            data_byte_array = QByteArray()
            stream =QDataStream(data_byte_array, QIODevice.WriteOnly)
            stream.setVersion(QDataStream.Qt_5_9)
            stream.writeUInt32(0)
            if self.line_edit:
                print('inside write_data')
                stream.writeQString(self.line_edit.text())
            self.socket.write(data_byte_array)
            data_byte_array = None
            if self.line_edit:
                self.line_edit.setText('')
        except Exception as e:
            print(e)
            
    def read_data(self):
        try:
            
            stream =QDataStream(self.socket)
            stream.setVersion(QDataStream.Qt_5_9)
            
            while True:
                if self.socket.bytesAvailable() <= 0:
                    break
                stream.readUInt32()
                text_from_server = stream.readQString()
                if self.text_widget:
                    print('display_text')
                    print(text_from_server)
                    self.text_widget.append(text_from_server)

        except Exception as e:
            print(e)

   
    
#-------------------------------------------------DRAG Y DROP----------------------------------------

class RunThread(QtCore.QThread):
    
    counter_value = QtCore.pyqtSignal(int)
    
    def __init__(self, parent= None, counter_start= 0):
        super (RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True
        
    def run(self):
        while self.counter < 100 and self.is_running == True:
            sleep(0.1)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)

    def stop(self):
        self.is_running = False
        print('Stoping thread...')
        self.terminate()
        

class DragDropButton(QtWidgets.QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())

class DragDropCombo(QtWidgets.QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        self.addItem(event.mimeData().text())

    
#---------------------------OpenGL------------------------------------------
        
class PyQtOpenGL(QOpenGLWidget):
    # rotation signals mouse movement
    x_rotation_changed = pyqtSignal(int)
    y_rotation_changed = pyqtSignal(int)
    z_rotation_changed = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.paint_0 = True
        self.paint_1 = True
        self.paint_2 = True
        self.resize_lines = True    # set orthographic matrix multiplier to large/small
        self.resize_lines = False
        
        self.paint_rotation = True
        self.paint_rotation = False
        self.x_rotation = 0         # rotation variables
        self.y_rotation = 0
        self.z_rotation = 0

        self.last_pos = QPoint()

    def normalize_angle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
    
    # slots for xyz-rotation 
    def set_x_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.x_rotation:
            self.x_rotation = angle
            self.x_rotation_changed.emit(angle)
            self.update()

    def set_y_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.y_rotation:
            self.y_rotation = angle
            self.y_rotation_changed.emit(angle)
            self.update()

    def set_z_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.z_rotation:
            self.z_rotation = angle
            self.z_rotation_changed.emit(angle)
            self.update()
            
    def initializeGL(self):
        # reimplemented
        glClearColor(0.0, 0.0, 1.0, 0.0)    # blue
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)  
        
        lightPosition = [0, 0, 10, 1.0]  
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition) 

    def paintGL(self):
        # reimplemented
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10.0)
        glRotatef(self.x_rotation / 16.0, 1.0, 0.0, 0.0)
        glRotatef(self.y_rotation / 16.0, 0.0, 1.0, 0.0)
        glRotatef(self.z_rotation / 16.0, 0.0, 0.0, 1.0)
        self.draw()      
   
    def draw(self):
        if self.paint_rotation:
            glColor3f(1.0, 0.0, 0.0)    
            glBegin(GL_QUADS)           # bottom of pyramid
            glNormal3f(0, 0, -1)
            glVertex3f(-1 ,-1, 0)
            glVertex3f(-1 ,1, 0)
            glVertex3f(1, 1, 0)
            glVertex3f(1, -1, 0)
            glEnd()
            
            glColor3f(0.0, 0.0, 0.0)
            glBegin(GL_TRIANGLES)       # four sides of pyramid
            glNormal3f(0, -1, 0.707)
            glVertex3f(-1, -1, 0)
            glVertex3f(1, -1, 0)
            glVertex3f(0, 0, 1.2)
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(1,0, 0.707)
            glVertex3f(1,-1,0)
            glVertex3f(1,1,0)
            glVertex3f(0,0,1.2)
            glEnd()
            
            glBegin(GL_TRIANGLES)
            glNormal3f(0,1,0.707)
            glVertex3f(1,1,0)
            glVertex3f(-1,1,0)
            glVertex3f(0,0,1.2)
            glEnd()
     
            glBegin(GL_TRIANGLES)
            glNormal3f(-1,0,0.707)
            glVertex3f(-1,1,0)
            glVertex3f(-1,-1,0)
            glVertex3f(0,0,1.2)
            glEnd()   

        # square and lines
        if self.paint_0:       
            glColor3f(1.0, 0.0, 0.0)    # functions expects 3 f(loats); RGB: red
            glRectf(-5, -5, 5, 5)       # draw a filled rectangle with above color, position(x,y) pairs from center of window
  
        if self.paint_1: 
            glColor3f(0.0, 1.0, 0.0)    # set color to RGB: green
            x=10
            y=10
            self.draw_loop(x, y)
         
        if self.paint_2: 
            glColor3f(0.0, 0.0, 0.0)    # set color to RGB: black
            x=5
            y=5
            self.draw_loop(x, y)
        
         
    def resizeGL(self, width, height):
        # reimplemented
        side = min(width, height)
        if side < 0:
            return
  
        glViewport((width - side) // 2, (height - side) // 2, side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        if self.resize_lines:
            glOrtho(-50, 50, -50, 50, -50.0, 50.0)  # for square and lines; combined with pyramid
        else:
            glOrtho(-2, +2, -2, +2, 1.0, 15.0)      # original pyramid setting
            
        glMatrixMode(GL_MODELVIEW)            
                
                
    def draw_loop(self, x, y, incr=10):
        for _ in range(5):
            self.draw_square_lines(x, y)
            x += incr
            y += incr

    def draw_square_lines(self, x=10, y=10, z=0):
        glBegin(GL_LINES)         # begin to draw a line
        glVertex3f(x, y, z)       # start line relative to center of window
        glVertex3f(x, -y, z)      # draw first line
         
        glVertex3f(x, -y, z)
        glVertex3f(-x, -y, z)
         
        glVertex3f(-x, -y, z)
        glVertex3f(-x, y, z)
         
        glVertex3f(-x, y, z)
        glVertex3f(x, y, z)
        glEnd()      


    def mousePressEvent(self, event):
        # reimplemented
        self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        # reimplemented
        move_x = event.x() - self.last_pos.x()
        move_y = event.y() - self.last_pos.y()

        if event.buttons() & Qt.LeftButton:                     # left mouse button
            self.set_x_rotation(self.x_rotation + 8 * move_y)
            self.set_y_rotation(self.y_rotation + 8 * move_x)
            
        elif event.buttons() & Qt.RightButton:                  # right mouse button 
            self.set_x_rotation(self.x_rotation + 8 * move_y)
            self.set_z_rotation(self.z_rotation + 8 * move_x)   # spin pyramid around itself

        self.last_pos = event.pos()

        #--------------------animation

class MoveToolButton(QtWidgets.QToolButton):

    def __init__(self, parent):
        try:
            super().__init__(parent)
            self.change_palette()
        except Exception as e:
            print(e)
            
    def change_palette(self, back=QColor("bd0000"), fore=QColor("#bd125c")):
        try:
            palette=self.palette()
            palette.setColor(self.backgroundRole(), back)
            palette.setColor(self.foregroundRole(), fore)
        except Exception as e:
            print(e)
        
    def position_button(self, new_position):
        try:
            
            self.move(new_position.x(), new_position.y())
        except Exception as e:
            print(e)
        
    new_position =QtCore.pyqtProperty(QtCore.QPoint, fset=position_button)
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    server = TcpServer()
    print(server.tcp_server)
    
    client = TcpClient()
    print(client.socket)
