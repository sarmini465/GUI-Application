
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
from PyQt5 import QtPrintSupport

import sqlite3

import source_rc


class Ui_MainWindow(object):

        #Menampilkan messagebox pada button simpan
    def mess_simpan(self):
        mess=QMessageBox()
        mess.setWindowTitle("Selamat")
        mess.setText("Data Telah Ditambahkan")
        x=mess.exec_()

        #Menampilkan messagebox pada button batal
    def mess_batal(self):
        mess=QMessageBox()
        mess.setWindowTitle("Batal")
        mess.setText("Apakah Anda Yakin Ingin Membatalkannya?")
        x=mess.exec_()

        #Menampilkan messagebox pada button laporan pencetakan peminjaman
    def mess_cetak_peminjaman(self):
        mess=QMessageBox()
        mess.setWindowTitle("Cetak Laporan")
        mess.setText("Apakah Anda Yakin Ingin Mencetak Laporan Peminjaman?")
        x=mess.exec_()

        #Menampilkan messagebox pada button laporan pencetakan pengembalian
    def mess_cetak_pengembalian(self):
        mess=QMessageBox()
        mess.setWindowTitle("Cetak Laporan")
        mess.setText("Apakah Anda Yakin Ingin Mencetak Laporan Pengembalian?")
        x=mess.exec_()

        #Menampilkan messagebox pada button laporan pencetakan buku
    def mess_cetak_buku(self):
        mess=QMessageBox()
        mess.setWindowTitle("Cetak Laporan")
        mess.setText("Apakah Anda Yakin Ingin Mencetak Laporan Buku?")
        x=mess.exec_()


        #data from sqlite
    def loaddata(self):
        connection = sqlite3.connect("pinjambuku.sqlite")
        cur = connection.cursor()
        sqlquery = 'SELECT * FROM databuku LIMIT 2'

       #results = cur.execute(sqlquery)
        self.tableWidget.setRowCount(2)
        tablerow=0

        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            #self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1


        #print data lagi
    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        tablewidget = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(tablewidget)
        table = cursor.insertTable(
            self.tableWidget.rowCount(), self.tableWidget.columnCount())
        for row in range(table.rows()):
            for col in range(table.columns()):
                cursor.insertText(self.tableWidget.item(row, col).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        tablewidget.print_(printer)
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1371, 101))
        self.widget.setStyleSheet("background-color:rgba(13, 237, 225, 1);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(1040, 10, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 0, 91, 91))
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 81, 101))
        self.label_2.setStyleSheet("border-image: url(:/image/unnes.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 100, 141, 611))
        self.widget_2.setStyleSheet("background-color:rgba(164, 240, 236, 1);")
        self.widget_2.setObjectName("widget_2")

        # ------------------------------------------------------ #
        # btn_1 -> tombol untuk mengubungkan dengan page_1
        # ------------------------------------------------------ #

        self.btn_1 = QtWidgets.QPushButton(self.widget_2)
        self.btn_1.setGeometry(QtCore.QRect(20, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.btn_1.setFont(font)
        self.btn_1.setMouseTracking(True)
        self.btn_1.setStyleSheet("QPushButton {\n"
"    background-color:rgba(255, 255, 255, 1);\n"
"    border-radius:5px;\n"
"    border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_1.setObjectName("btn_1")

        # ------------------------------------------------------ #
        # btn_2 -> tombol untuk mengubungkan dengan page_2
        # ------------------------------------------------------ #

        self.btn_2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_2.setGeometry(QtCore.QRect(20, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("QPushButton {\n"
"    background-color:rgba(255, 255, 255, 1);\n"
"    border-radius:5px;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_2.setObjectName("btn_2")

        # ------------------------------------------------------ #
        # btn_3 -> tombol untuk mengubungkan dengan page_3
        # ------------------------------------------------------ #

        self.btn_3 = QtWidgets.QPushButton(self.widget_2)
        self.btn_3.setGeometry(QtCore.QRect(20, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("QPushButton {\n"
"    background-color:rgba(255, 255, 255, 1);\n"
"    border-radius:5px;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_3.setObjectName("btn_3")

        # ------------------------------------------------------ #
        # btn_4 -> tombol untuk mengubungkan dengan page_4
        # ------------------------------------------------------ #

        self.btn_4 = QtWidgets.QPushButton(self.widget_2)
        self.btn_4.setGeometry(QtCore.QRect(20, 240, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("QPushButton {\n"
"    background-color:rgba(255, 255, 255, 1);\n"
"    border-radius:5px;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_4.setObjectName("btn_4")

        # ------------------------------------------------------ #
        # btn_5 -> tombol untuk mengubungkan dengan page_5
        # ------------------------------------------------------ #

        self.btn_5 = QtWidgets.QPushButton(self.widget_2)
        self.btn_5.setGeometry(QtCore.QRect(20, 310, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("QPushButton {\n"
"    background-color:rgba(255, 255, 255, 1);\n"
"    border-radius:5px;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_5.setObjectName("btn_5")

        # ------------------------------------------------------ #
        # btn_6 -> tombol untuk mengubungkan dengan page_6
        # ------------------------------------------------------ #

        self.btn_6 = QtWidgets.QPushButton(self.widget_2)
        self.btn_6.setGeometry(QtCore.QRect(20, 380, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("QPushButton {\n"
"    background-color:rgba(255, 255, 255, 1);\n"
"    border-radius:5px;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_6.setObjectName("btn_6")

        # ------------------------------------------------------ #
        # btn_7 -> tombol log out untuk keluar dari aplikasi 
        # ------------------------------------------------------ #

        self.btn_7 = QtWidgets.QPushButton(self.widget_2)
        self.btn_7.setGeometry(QtCore.QRect(30, 560, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("QPushButton {\n"
"    background-color:rgba(249, 4, 4, 1);\n"
"    border-radius:5px;;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.btn_7.setObjectName("btn_7")

        # ------------------------------------------------------ #
        #                      Stacked widget                    #
        # ------------------------------------------------------ #
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(140, 100, 1231, 611))
        self.stackedWidget.setObjectName("stackedWidget")

        # ------------------------------------------------------ #
        #                          page_1                        #
        # ------------------------------------------------------ #

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.widget_selamatdatang = QtWidgets.QWidget(self.page_1)
        self.widget_selamatdatang.setGeometry(QtCore.QRect(0, 0, 1251, 611))
        self.widget_selamatdatang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_selamatdatang.setObjectName("widget_selamatdatang")
        self.label_5 = QtWidgets.QLabel(self.widget_selamatdatang)
        self.label_5.setGeometry(QtCore.QRect(200, 180, 811, 161))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.widget_selamatdatang)
        self.label_4.setGeometry(QtCore.QRect(200, 30, 811, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_1)

        # ------------------------------------------------------ #
        #                          page_2                        #
        # ------------------------------------------------------ #

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.widget_pinjam = QtWidgets.QWidget(self.page_2)
        self.widget_pinjam.setGeometry(QtCore.QRect(0, 0, 1231, 611))
        self.widget_pinjam.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_pinjam.setObjectName("widget_pinjam")
        self.form_pinjam = QtWidgets.QWidget(self.widget_pinjam)
        self.form_pinjam.setGeometry(QtCore.QRect(20, 20, 591, 571))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.form_pinjam.setFont(font)
        self.form_pinjam.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"")
        self.form_pinjam.setObjectName("form_pinjam")
        self.label_3 = QtWidgets.QLabel(self.form_pinjam)
        self.label_3.setGeometry(QtCore.QRect(120, 0, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_NIM = QtWidgets.QLineEdit(self.form_pinjam)
        self.lineEdit_NIM.setGeometry(QtCore.QRect(240, 90, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_NIM.setFont(font)
        self.lineEdit_NIM.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_NIM.setObjectName("lineEdit_NIM")
        self.label_6 = QtWidgets.QLabel(self.form_pinjam)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.form_pinjam)
        self.label_7.setGeometry(QtCore.QRect(40, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.form_pinjam)
        self.label_8.setGeometry(QtCore.QRect(40, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.form_pinjam)
        self.label_9.setGeometry(QtCore.QRect(40, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.form_pinjam)
        self.label_10.setGeometry(QtCore.QRect(40, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_kbuku = QtWidgets.QLineEdit(self.form_pinjam)
        self.lineEdit_kbuku.setGeometry(QtCore.QRect(240, 130, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_kbuku.setFont(font)
        self.lineEdit_kbuku.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_kbuku.setObjectName("lineEdit_kbuku")
        self.lineEdit_jbuku = QtWidgets.QLineEdit(self.form_pinjam)
        self.lineEdit_jbuku.setGeometry(QtCore.QRect(240, 170, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_jbuku.setFont(font)
        self.lineEdit_jbuku.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_jbuku.setObjectName("lineEdit_jbuku")
        self.tgl_pinjam_p2 = QtWidgets.QDateEdit(self.form_pinjam)
        self.tgl_pinjam_p2.setGeometry(QtCore.QRect(240, 210, 301, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tgl_pinjam_p2.setFont(font)
        self.tgl_pinjam_p2.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.tgl_pinjam_p2.setObjectName("tgl_pinjam_p2")
        self.tgl_kembali_p2 = QtWidgets.QDateEdit(self.form_pinjam)
        self.tgl_kembali_p2.setGeometry(QtCore.QRect(240, 250, 301, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tgl_kembali_p2.setFont(font)
        self.tgl_kembali_p2.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.tgl_kembali_p2.setObjectName("tgl_kembali_p2")
        self.simpan_p2 = QtWidgets.QPushButton(self.form_pinjam)
        self.simpan_p2.setGeometry(QtCore.QRect(470, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.simpan_p2.setFont(font)
        self.simpan_p2.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgba(81, 204, 37, 1);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.simpan_p2.setObjectName("simpan_p2")

        #menampilakan messagebox

        self.simpan_p2.clicked.connect(self.mess_simpan)
        
        self.batal_p2 = QtWidgets.QPushButton(self.form_pinjam)
        self.batal_p2.setGeometry(QtCore.QRect(370, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batal_p2.setFont(font)
        self.batal_p2.setStyleSheet("QPushButton {\n"
"    background-color:rgba(249, 4, 4, 1);\n"
"    border-radius:5px;;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.batal_p2.setObjectName("batal_p2")

        #menampilkan pesan batal

        self.batal_p2.clicked.connect(self.mess_batal)

        self.form_riwayat = QtWidgets.QWidget(self.widget_pinjam)
        self.form_riwayat.setGeometry(QtCore.QRect(630, 20, 581, 571))
        self.form_riwayat.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.form_riwayat.setObjectName("form_riwayat")
        self.label_11 = QtWidgets.QLabel(self.form_riwayat)
        self.label_11.setGeometry(QtCore.QRect(130, 0, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.form_riwayat)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 520, 420))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.page_2)
        
        #ini kode yang baru aku tambahin untuk tombol cetak data 

       
        # ------------------------------------------------------ #
        #                          page_3                        #
        # ------------------------------------------------------ #

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.widget_kembali = QtWidgets.QWidget(self.page_3)
        self.widget_kembali.setGeometry(QtCore.QRect(-1, 0, 1231, 611))
        self.widget_kembali.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_kembali.setObjectName("widget_kembali")
        self.widget_12 = QtWidgets.QWidget(self.widget_kembali)
        self.widget_12.setGeometry(QtCore.QRect(20, 20, 591, 571))
        self.widget_12.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"")
        self.widget_12.setObjectName("widget_12")
        self.label_12 = QtWidgets.QLabel(self.widget_12)
        self.label_12.setGeometry(QtCore.QRect(100, 0, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_pengembali = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_pengembali.setGeometry(QtCore.QRect(240, 90, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pengembali.setFont(font)
        self.lineEdit_pengembali.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_pengembali.setObjectName("lineEdit_pengembali")
        self.label_13 = QtWidgets.QLabel(self.widget_12)
        self.label_13.setGeometry(QtCore.QRect(40, 90, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_12)
        self.label_14.setGeometry(QtCore.QRect(40, 170, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_12)
        self.label_15.setGeometry(QtCore.QRect(40, 210, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget_12)
        self.label_16.setGeometry(QtCore.QRect(40, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.widget_12)
        self.label_17.setGeometry(QtCore.QRect(40, 290, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_kbuku_p3 = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_kbuku_p3.setGeometry(QtCore.QRect(240, 170, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_kbuku_p3.setFont(font)
        self.lineEdit_kbuku_p3.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_kbuku_p3.setObjectName("lineEdit_kbuku_p3")
        self.lineEdit_jbuku_p3 = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_jbuku_p3.setGeometry(QtCore.QRect(240, 210, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_jbuku_p3.setFont(font)
        self.lineEdit_jbuku_p3.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_jbuku_p3.setObjectName("lineEdit_jbuku_p3")
        self.tgl_kembali_p3 = QtWidgets.QDateEdit(self.widget_12)
        self.tgl_kembali_p3.setGeometry(QtCore.QRect(240, 250, 301, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tgl_kembali_p3.setFont(font)
        self.tgl_kembali_p3.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.tgl_kembali_p3.setObjectName("tgl_kembali_p3")
        self.simpan_p3 = QtWidgets.QPushButton(self.widget_12)
        self.simpan_p3.setGeometry(QtCore.QRect(470, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.simpan_p3.setFont(font)
        self.simpan_p3.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgba(81, 204, 37, 1);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.simpan_p3.setObjectName("simpan_p3")

        #Menampilkan pesan

        self.simpan_p3.clicked.connect(self.mess_simpan)

        self.batal_p3 = QtWidgets.QPushButton(self.widget_12)
        self.batal_p3.setGeometry(QtCore.QRect(380, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.batal_p3.setFont(font)
        self.batal_p3.setStyleSheet("QPushButton {\n"
"    background-color:rgba(249, 4, 4, 1);\n"
"    border-radius:5px;;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.batal_p3.setObjectName("batal_p3")

        #menampilkan pesan batal

        self.batal_p3.clicked.connect(self.mess_batal)

        self.widget_14 = QtWidgets.QWidget(self.widget_12)
        self.widget_14.setGeometry(QtCore.QRect(610, 0, 521, 571))
        self.widget_14.setObjectName("widget_14")
        self.label_19 = QtWidgets.QLabel(self.widget_12)
        self.label_19.setGeometry(QtCore.QRect(40, 130, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.lineEdit_nim_p3 = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_nim_p3.setGeometry(QtCore.QRect(240, 130, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_nim_p3.setFont(font)
        self.lineEdit_nim_p3.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_nim_p3.setObjectName("lineEdit_nim_p3")
        self.label_20 = QtWidgets.QLabel(self.widget_12)
        self.label_20.setGeometry(QtCore.QRect(40, 330, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_terlambat = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_terlambat.setGeometry(QtCore.QRect(240, 290, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_terlambat.setFont(font)
        self.lineEdit_terlambat.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_terlambat.setObjectName("lineEdit_terlambat")
        self.lineEdit_denda = QtWidgets.QLineEdit(self.widget_12)
        self.lineEdit_denda.setGeometry(QtCore.QRect(240, 330, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_denda.setFont(font)
        self.lineEdit_denda.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_denda.setObjectName("lineEdit_denda")
        self.widget_15 = QtWidgets.QWidget(self.widget_kembali)
        self.widget_15.setGeometry(QtCore.QRect(630, 20, 581, 571))
        self.widget_15.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.widget_15.setObjectName("widget_15")
        self.label_18 = QtWidgets.QLabel(self.widget_15)
        self.label_18.setGeometry(QtCore.QRect(100, 0, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget_15)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 50, 559, 509))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()

        # ------------------------------------------------------ #
        #                          page_4                        #
        # ------------------------------------------------------ #

        self.page_4.setObjectName("page_4")
        self.widget_anggota = QtWidgets.QWidget(self.page_4)
        self.widget_anggota.setGeometry(QtCore.QRect(-1, 0, 1231, 611))
        self.widget_anggota.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_anggota.setObjectName("widget_anggota")
        self.widget_16 = QtWidgets.QWidget(self.widget_anggota)
        self.widget_16.setGeometry(QtCore.QRect(20, 20, 591, 571))
        self.widget_16.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"")
        self.widget_16.setObjectName("widget_16")
        self.label_21 = QtWidgets.QLabel(self.widget_16)
        self.label_21.setGeometry(QtCore.QRect(70, 0, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.lineEdit_nama_p4 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_nama_p4.setGeometry(QtCore.QRect(260, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lineEdit_nama_p4.setFont(font)
        self.lineEdit_nama_p4.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_nama_p4.setObjectName("lineEdit_nama_p4")
        self.label_22 = QtWidgets.QLabel(self.widget_16)
        self.label_22.setGeometry(QtCore.QRect(40, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_16)
        self.label_23.setGeometry(QtCore.QRect(40, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.widget_16)
        self.label_24.setGeometry(QtCore.QRect(40, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.widget_16)
        self.label_25.setGeometry(QtCore.QRect(40, 250, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_16.setGeometry(QtCore.QRect(260, 250, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_prodi_p4 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_prodi_p4.setGeometry(QtCore.QRect(260, 210, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lineEdit_prodi_p4.setFont(font)
        self.lineEdit_prodi_p4.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_prodi_p4.setObjectName("lineEdit_prodi_p4")
        self.tgl_lahir_p4 = QtWidgets.QDateEdit(self.widget_16)
        self.tgl_lahir_p4.setGeometry(QtCore.QRect(260, 170, 281, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.tgl_lahir_p4.setFont(font)
        self.tgl_lahir_p4.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.tgl_lahir_p4.setObjectName("tgl_lahir_p4")
        self.simpan_p4 = QtWidgets.QPushButton(self.widget_16)
        self.simpan_p4.setGeometry(QtCore.QRect(470, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.simpan_p4.setFont(font)
        self.simpan_p4.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgba(81, 204, 37, 1);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.simpan_p4.setObjectName("simpan_p4")

        #Menampilkan pesan

        self.simpan_p4.clicked.connect(self.mess_simpan)

        self.batal_p4 = QtWidgets.QPushButton(self.widget_16)
        self.batal_p4.setGeometry(QtCore.QRect(380, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.batal_p4.setFont(font)
        self.batal_p4.setStyleSheet("QPushButton {\n"
"    background-color:rgba(249, 4, 4, 1);\n"
"    border-radius:5px;;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.batal_p4.setObjectName("batal_p4")

        #menampilkan pesan batal

        self.batal_p4.clicked.connect(self.mess_batal)

        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        self.widget_17.setGeometry(QtCore.QRect(610, 0, 521, 571))
        self.widget_17.setObjectName("widget_17")
        self.label_27 = QtWidgets.QLabel(self.widget_16)
        self.label_27.setGeometry(QtCore.QRect(40, 130, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_nim_p4 = QtWidgets.QLineEdit(self.widget_16)
        self.lineEdit_nim_p4.setGeometry(QtCore.QRect(260, 130, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lineEdit_nim_p4.setFont(font)
        self.lineEdit_nim_p4.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_nim_p4.setObjectName("lineEdit_nim_p4")
        self.widget_18 = QtWidgets.QWidget(self.widget_anggota)
        self.widget_18.setGeometry(QtCore.QRect(630, 20, 581, 571))
        self.widget_18.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.widget_18.setObjectName("widget_18")
        self.label_29 = QtWidgets.QLabel(self.widget_18)
        self.label_29.setGeometry(QtCore.QRect(180, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_26 = QtWidgets.QLabel(self.widget_18)
        self.label_26.setGeometry(QtCore.QRect(70, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(True)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.widget_18)
        self.label_28.setGeometry(QtCore.QRect(70, 100, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_30 = QtWidgets.QLabel(self.widget_18)
        self.label_30.setGeometry(QtCore.QRect(70, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.lineEdit_carinim_p4 = QtWidgets.QLineEdit(self.widget_18)
        self.lineEdit_carinim_p4.setGeometry(QtCore.QRect(160, 100, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_carinim_p4.setFont(font)
        self.lineEdit_carinim_p4.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_carinim_p4.setObjectName("lineEdit_carinim_p4")
        self.lineEdit_carinama_p4 = QtWidgets.QLineEdit(self.widget_18)
        self.lineEdit_carinama_p4.setGeometry(QtCore.QRect(160, 140, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_carinama_p4.setFont(font)
        self.lineEdit_carinama_p4.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_carinama_p4.setObjectName("lineEdit_carinama_p4")
        self.cari_p4 = QtWidgets.QPushButton(self.widget_18)
        self.cari_p4.setGeometry(QtCore.QRect(430, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.cari_p4.setFont(font)
        self.cari_p4.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgba(81, 204, 37, 1);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.cari_p4.setObjectName("cari_p4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.widget_18)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 250, 559, 311))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        self.stackedWidget.addWidget(self.page_4)

        # ------------------------------------------------------ #
        #                          page_5                        #
        # ------------------------------------------------------ #

        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.widget_buku = QtWidgets.QWidget(self.page_5)
        self.widget_buku.setGeometry(QtCore.QRect(-1, 0, 1231, 611))
        self.widget_buku.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_buku.setObjectName("widget_buku")
        self.widget_19 = QtWidgets.QWidget(self.widget_buku)
        self.widget_19.setGeometry(QtCore.QRect(20, 20, 591, 571))
        self.widget_19.setStyleSheet("background-color: rgb(229, 229, 229);\n"
"")
        self.widget_19.setObjectName("widget_19")
        self.label_31 = QtWidgets.QLabel(self.widget_19)
        self.label_31.setGeometry(QtCore.QRect(120, 0, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.lineEdit_jbuku_p5 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_jbuku_p5.setGeometry(QtCore.QRect(200, 90, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_jbuku_p5.setFont(font)
        self.lineEdit_jbuku_p5.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_jbuku_p5.setObjectName("lineEdit_jbuku_p5")
        self.label_32 = QtWidgets.QLabel(self.widget_19)
        self.label_32.setGeometry(QtCore.QRect(40, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.widget_19)
        self.label_33.setGeometry(QtCore.QRect(40, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.widget_19)
        self.label_34.setGeometry(QtCore.QRect(40, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.lineEdit_kbuku_p5 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_kbuku_p5.setGeometry(QtCore.QRect(200, 210, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_kbuku_p5.setFont(font)
        self.lineEdit_kbuku_p5.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_kbuku_p5.setObjectName("lineEdit_kbuku_p5")
        self.simpan_p5 = QtWidgets.QPushButton(self.widget_19)
        self.simpan_p5.setGeometry(QtCore.QRect(470, 290, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.simpan_p5.setFont(font)
        self.simpan_p5.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgba(81, 204, 37, 1);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.simpan_p5.setObjectName("simpan_p5")

        #Menampilkan pesan

        self.simpan_p5.clicked.connect(self.mess_simpan)

        self.batal_p5 = QtWidgets.QPushButton(self.widget_19)
        self.batal_p5.setGeometry(QtCore.QRect(380, 290, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.batal_p5.setFont(font)
        self.batal_p5.setStyleSheet("QPushButton {\n"
"    background-color:rgba(249, 4, 4, 1);\n"
"    border-radius:5px;;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 0);\n"
"}")
        self.batal_p5.setObjectName("batal_p5")

        #menampilkan pesan batal

        self.batal_p5.clicked.connect(self.mess_batal)

        self.widget_20 = QtWidgets.QWidget(self.widget_19)
        self.widget_20.setGeometry(QtCore.QRect(610, 0, 521, 571))
        self.widget_20.setObjectName("widget_20")
        self.label_36 = QtWidgets.QLabel(self.widget_19)
        self.label_36.setGeometry(QtCore.QRect(40, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.lineEdit_pengarang_p5 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_pengarang_p5.setGeometry(QtCore.QRect(200, 130, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_pengarang_p5.setFont(font)
        self.lineEdit_pengarang_p5.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_pengarang_p5.setObjectName("lineEdit_pengarang_p5")
        self.lineEdit_tahunterbit_p5 = QtWidgets.QLineEdit(self.widget_19)
        self.lineEdit_tahunterbit_p5.setGeometry(QtCore.QRect(200, 170, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_tahunterbit_p5.setFont(font)
        self.lineEdit_tahunterbit_p5.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_tahunterbit_p5.setObjectName("lineEdit_tahunterbit_p5")
        self.widget_21 = QtWidgets.QWidget(self.widget_buku)
        self.widget_21.setGeometry(QtCore.QRect(630, 20, 581, 571))
        self.widget_21.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.widget_21.setObjectName("widget_21")
        self.label_37 = QtWidgets.QLabel(self.widget_21)
        self.label_37.setGeometry(QtCore.QRect(200, 0, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.widget_21)
        self.label_38.setGeometry(QtCore.QRect(70, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(True)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.widget_21)
        self.label_39.setGeometry(QtCore.QRect(70, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.widget_21)
        self.label_40.setGeometry(QtCore.QRect(70, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.lineEdit_kbuku_p5_2 = QtWidgets.QLineEdit(self.widget_21)
        self.lineEdit_kbuku_p5_2.setGeometry(QtCore.QRect(200, 100, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_kbuku_p5_2.setFont(font)
        self.lineEdit_kbuku_p5_2.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_kbuku_p5_2.setObjectName("lineEdit_kbuku_p5_2")
        self.lineEdit_jbuku_p5_2 = QtWidgets.QLineEdit(self.widget_21)
        self.lineEdit_jbuku_p5_2.setGeometry(QtCore.QRect(200, 140, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_jbuku_p5_2.setFont(font)
        self.lineEdit_jbuku_p5_2.setStyleSheet("border-radius:2px;\n"
"background-color:rgba(197, 197, 197, 1);")
        self.lineEdit_jbuku_p5_2.setObjectName("lineEdit_jbuku_p5_2")
        self.cari_p5 = QtWidgets.QPushButton(self.widget_21)
        self.cari_p5.setGeometry(QtCore.QRect(430, 190, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.cari_p5.setFont(font)
        self.cari_p5.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgba(81, 204, 37, 1);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.cari_p5.setObjectName("cari_p5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.widget_21)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 250, 559, 311))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.stackedWidget.addWidget(self.page_5)
        self.cetak_peminjaman = QtWidgets.QPushButton(self.widget_21)
       

        # ------------------------------------------------------ #
        #                          page_6                        #
        # ------------------------------------------------------ #

        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.widget_9 = QtWidgets.QWidget(self.page_6)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 1231, 611))
        self.widget_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_9.setObjectName("widget_9")
        self.widget_22 = QtWidgets.QWidget(self.widget_9)
        self.widget_22.setGeometry(QtCore.QRect(20, 20, 1191, 571))
        self.widget_22.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.widget_22.setObjectName("widget_22")
        self.label_41 = QtWidgets.QLabel(self.widget_22)
        self.label_41.setGeometry(QtCore.QRect(520, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.cetak_peminjaman = QtWidgets.QPushButton(self.widget_22)
        self.cetak_peminjaman.setGeometry(QtCore.QRect(480, 110, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.cetak_peminjaman.setFont(font)
        self.cetak_peminjaman.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color: rgb(0, 177, 0);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 227, 0);\n"
"}")
        self.cetak_peminjaman.setObjectName("cetak_peminjaman")

         #Menampilkan pesan cetak laporan peminjaman

        self.cetak_peminjaman.clicked.connect(self.mess_cetak_peminjaman)

         #Menampilkan print data

        self.cetak_peminjaman.clicked.connect(self.handlePreview)

        self.cetak_pengembalian = QtWidgets.QPushButton(self.widget_22)
        self.cetak_pengembalian.setGeometry(QtCore.QRect(480, 220, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.cetak_pengembalian.setFont(font)
        self.cetak_pengembalian.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color: rgb(0, 177, 0);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 227, 0);\n"
"}")
        self.cetak_pengembalian.setObjectName("cetak_pengembalian")

         #Menampilkan pesan cetak laporan pengembalian

        self.cetak_pengembalian.clicked.connect(self.mess_cetak_pengembalian)

         #Menampilkan print data
        
        self.cetak_pengembalian.clicked.connect(self.handlePreview)

        self.cetak_laporan = QtWidgets.QPushButton(self.widget_22)
        self.cetak_laporan.setGeometry(QtCore.QRect(480, 330, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.cetak_laporan.setFont(font)
        self.cetak_laporan.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color: rgb(0, 177, 0);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 227, 0);\n"
"}")
        self.cetak_laporan.setObjectName("cetak_laporan")

         #Menampilkan pesan cetak laporan buku

        self.cetak_laporan.clicked.connect(self.mess_cetak_buku)

         #Menampilkan print data
        
        self.cetak_laporan.clicked.connect(self.handlePreview)

        self.stackedWidget.addWidget(self.page_6)
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # fungsi tombol pada widget_2

        # fungsi halaman current page
        self.stackedWidget.setCurrentWidget(self.page_1)

        # fungsi btn_1 ke page 1
        self.btn_1.clicked.connect(self.showPage_1)

        # fungsi btn_2 ke page 2
        self.btn_2.clicked.connect(self.showPage_2)

        # fungsi btn_3 ke page 3
        self.btn_3.clicked.connect(self.showPage_3)

        # fungsi btn_4 ke page 4
        self.btn_4.clicked.connect(self.showPage_4)

        # fungsi btn_5 ke page 5
        self.btn_5.clicked.connect(self.showPage_5)

        # fungsi btn_6 ke page 6
        self.btn_6.clicked.connect(self.showPage_6)
        
        # fungsi button Log Out
        self.btn_7.clicked.connect(self.showLogout)

    def showLogout(self):
        MainWindow.hide()


    def show(self):
        self.main_window.show()


    def showPage_1(self):
        self.stackedWidget.setCurrentWidget(self.page_1)

    def showPage_2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)

    def showPage_3(self):
        self.stackedWidget.setCurrentWidget(self.page_3)

    def showPage_4(self):
        self.stackedWidget.setCurrentWidget(self.page_4)

    def showPage_5(self):
        self.stackedWidget.setCurrentWidget(self.page_5)

    def showPage_6(self):
        self.stackedWidget.setCurrentWidget(self.page_6) 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "myLibKOM"))
        self.btn_1.setText(_translate("MainWindow", "Beranda"))
        self.btn_2.setText(_translate("MainWindow", "Peminjaman"))
        self.btn_3.setText(_translate("MainWindow", "Pengembalian"))
        self.btn_4.setText(_translate("MainWindow", "Anggota"))
        self.btn_5.setText(_translate("MainWindow", "Data Buku"))
        self.btn_6.setText(_translate("MainWindow", "Laporan"))
        self.btn_7.setText(_translate("MainWindow", "Log Out"))
        self.label_5.setText(_translate("MainWindow", "myLibKOM adalah aplikasi perpustakaan berbasis GUI Jurusan Ilmu Komputer. Aplikasi ini dikembangkan oleh mahasiswa program Studi Sistem Informasi angkatan 2020. Pengembang aplikasi myLibKOM diantaranya: \n"
"1. Sarmini \n"
"2. Nur Afan Syarifudin\n"
"3. Dilla Caroline Khairunnisa\n"
"4. Johan Damar Aji Rahmatulloh"))
        self.label_4.setText(_translate("MainWindow", "SELAMAT DATANG DI APLIKASI myLibKOM"))
        self.label_3.setText(_translate("MainWindow", "FORMULIR PEMINJAMAN"))
        self.label_6.setText(_translate("MainWindow", "NIM"))
        self.label_7.setText(_translate("MainWindow", "Kode Buku"))
        self.label_8.setText(_translate("MainWindow", "Judul Buku"))
        self.label_9.setText(_translate("MainWindow", "Tanggal Peminjaman"))
        self.label_10.setText(_translate("MainWindow", "Tanggal Pengembalian"))
        self.simpan_p2.setText(_translate("MainWindow", "Simpan"))
        self.batal_p2.setText(_translate("MainWindow", "Batal"))
        self.label_11.setText(_translate("MainWindow", "RIWAYAT PEMINJAMAN"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nomor"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NIM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kode Buku"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Judul Buku"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tanggal Pinjam"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tanggal Kembali"))
        self.loaddata()
        self.label_12.setText(_translate("MainWindow", "FORMULIR PENGEMBALIAN"))
        self.label_13.setText(_translate("MainWindow", "Nama Pengembali "))
        self.label_14.setText(_translate("MainWindow", "Kode Buku"))
        self.label_15.setText(_translate("MainWindow", "Judul Buku"))
        self.label_16.setText(_translate("MainWindow", "Tanggal Pengembalian"))
        self.label_17.setText(_translate("MainWindow", "Terlambat"))
        self.simpan_p3.setText(_translate("MainWindow", "Simpan"))
        self.batal_p3.setText(_translate("MainWindow", "Batal"))
        self.label_19.setText(_translate("MainWindow", "NIM"))
        self.label_20.setText(_translate("MainWindow", "Denda"))
        self.label_18.setText(_translate("MainWindow", "RIWAYAT PENGEMBALIAN"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nomor"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pengembali"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NIM"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Kode Buku"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Judul Buku"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tanggal Kembali"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Denda"))
        self.label_21.setText(_translate("MainWindow", "FORMULIR TAMBAH ANGGOTA"))
        self.label_22.setText(_translate("MainWindow", "Nama Lengkap"))
        self.label_23.setText(_translate("MainWindow", "Tanggal Lahir"))
        self.label_24.setText(_translate("MainWindow", "Program Studi"))
        self.label_25.setText(_translate("MainWindow", "Semester yang Di tempuh"))
        self.simpan_p4.setText(_translate("MainWindow", "Simpan"))
        self.batal_p4.setText(_translate("MainWindow", "Batal"))
        self.label_27.setText(_translate("MainWindow", "NIM"))
        self.label_29.setText(_translate("MainWindow", "DATA ANGGOTA"))
        self.label_26.setText(_translate("MainWindow", "Cari Anggota"))
        self.label_28.setText(_translate("MainWindow", "NIM"))
        self.label_30.setText(_translate("MainWindow", "Nama"))
        self.cari_p4.setText(_translate("MainWindow", "Cari"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nomor"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama Lengkap"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NIM"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tanggal Lahir"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Program Studi"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Semester"))
        self.label_31.setText(_translate("MainWindow", "FORMULIR TAMBAH BUKU"))
        self.label_32.setText(_translate("MainWindow", "Judul Buku"))
        self.label_33.setText(_translate("MainWindow", "Tahun Terbit"))
        self.label_34.setText(_translate("MainWindow", "Kode Buku"))
        self.simpan_p5.setText(_translate("MainWindow", "Simpan"))
        self.batal_p5.setText(_translate("MainWindow", "Batal"))
        self.label_36.setText(_translate("MainWindow", "Pengarang"))
        self.label_37.setText(_translate("MainWindow", "DATA BUKU"))
        self.label_38.setText(_translate("MainWindow", "Cari Buku"))
        self.label_39.setText(_translate("MainWindow", "Kode Buku"))
        self.label_40.setText(_translate("MainWindow", "Judul Buku"))
        self.cari_p5.setText(_translate("MainWindow", "Cari"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nomor"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pengarang"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tahun Terbit"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Judul Buku"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Kode Buku"))
        self.label_41.setText(_translate("MainWindow", "LAPORAN"))
        self.cetak_peminjaman.setText(_translate("MainWindow", "Cetak Laporan Peminjaman"))
        self.cetak_pengembalian.setText(_translate("MainWindow", "Cetak Laporan Pengembalian"))
        self.cetak_laporan.setText(_translate("MainWindow", "Cetak Laporan Buku"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
