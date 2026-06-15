import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow_fix_1 import Ui_MainWindow


class Ui_Form(object):
    def MainPage (self):
        user = self.username.text()
        password = self.password.text()

        if len(user)==0 or len(password)==0:
            self.login_notif.setText("Username atau Password Tidak Boleh Kosong!")
        else:
            conn = sqlite3.connect("login_data.db")
            cursor = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\''+user+"\'"
            cursor.execute(query)
            result_pass = cursor.fetchone()[0]
            if result_pass == password:
                self.MainWindow_fix_1 = QtWidgets.QWidget()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.MainWindow_fix_1)
                Form.hide()
                self.MainWindow_fix_1.show()

            else:
                self.login_notif.setText("Username atau Password Salah!")

        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 30, 370, 480))
        self.widget.setStyleSheet("background-color:rgba(255,255,255,1);\n"
"border-radius:10px;\n"
"\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.judul_1 = QtWidgets.QLabel(self.widget)
        self.judul_1.setGeometry(QtCore.QRect(100, 20, 151, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.judul_1.setFont(font)
        self.judul_1.setStyleSheet("background-color:transparent;\n"
"")
        self.judul_1.setObjectName("judul_1")
        self.judul_2 = QtWidgets.QLabel(self.widget)
        self.judul_2.setGeometry(QtCore.QRect(70, 60, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        self.judul_2.setFont(font)
        self.judul_2.setStyleSheet("background-color:transparent;")
        self.judul_2.setAlignment(QtCore.Qt.AlignCenter)
        self.judul_2.setObjectName("judul_2")

        # username

        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(40, 140, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.username.setFont(font)
        self.username.setStyleSheet("border-radius:5px;\n"
"background-color:rgba(220, 234, 233, 1);\n"
"color: rgb(72, 72, 72);\n"
"")
        self.username.setObjectName("username")

        # password

        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(40, 210, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius:5px;\n"
"background-color:rgba(220, 234, 233, 1);\n"
"color: rgb(72, 72, 72);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setReadOnly(False)
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")

        # push button login

        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setGeometry(QtCore.QRect(40, 290, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(10, 196, 221, 1);\n"
"    border-radius:5px;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(42, 126, 126);\n"
"}\n"
"")
        self.login_btn.setObjectName("login_btn")

        # fungsi push button login
        
        self.login_btn.clicked.connect(self.MainPage)


        self.label_kelompok = QtWidgets.QLabel(self.widget)
        self.label_kelompok.setGeometry(QtCore.QRect(120, 440, 121, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        font.setKerning(True)
        self.label_kelompok.setFont(font)
        self.label_kelompok.setAutoFillBackground(False)
        self.label_kelompok.setStyleSheet("background-color:transparent;")
        self.label_kelompok.setObjectName("label_kelompok")
        self.login_notif = QtWidgets.QLabel(self.widget)
        self.login_notif.setGeometry(QtCore.QRect(40, 260, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setItalic(False)

        # login notif 

        self.login_notif.setFont(font)
        self.login_notif.setStyleSheet("color: rgb(255, 0, 0);")
        self.login_notif.setText("")
        self.login_notif.setWordWrap(True)
        self.login_notif.setObjectName("login_notif")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.judul_1.setText(_translate("Form", "myLibKOM"))
        self.judul_2.setText(_translate("Form", "Aplikasi Perpustakaan Berbasis GUI\n"
"Jurusan Ilmu Komputer"))
        self.username.setPlaceholderText(_translate("Form", "Username"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.login_btn.setText(_translate("Form", "Log In"))
        self.label_kelompok.setText(_translate("Form", "Copyright Kelompok 2"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
