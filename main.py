import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con
import subprocess
import signal
import psutil
import sip

class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui\login.ui", self)
        self.loginbutton.clicked.connect(self.open_website_blocker)
        self.password_tb.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.registerbutton.clicked.connect(self.go_to_create)

    def loginfunction(self):
        mainWindow = MainWindow()
        widget.addWidget(mainWindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def open_website_blocker(self):
        username = self.username_tb.text()
        password = self.password_tb.text()
        if(username.__eq__("admin") and password.__eq__("admin")):
            QApplication.exit()
            subprocess.Popen(['python' , 'website_blocker.py'])
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Username or Password incorrect')
            msg.setWindowTitle("Error")
            msg.exec_()
        

        

    # def go_to_create(self):
    #     register = Register()
    #     widget.addWidget(register)
    #     widget.setCurrentIndex(widget.currentIndex()+1)


# class Register(QDialog):
#     def __init__(self):
#         super(Register, self).__init__()
#         loadUi("ui\\register.ui", self)
#         self.registerbutton.clicked.connect(self.registerfunction)
#         self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.back_to_login_button.clicked.connect(self.show_login)

#     def registerfunction(self):
#         username = self.username_reg.text()
#         if self.password_reg.text() == self.confirmpassword.text():
#             password = self.password_reg.text()
#             print("You are succsessfully signed up")

#     def show_login(self):
#         widget.setCurrentIndex(0)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("ui\\main-page.ui", self)
        self.populate_table()
        self.startBtn.clicked.connect(self.send_ping)
        self.stopBtn.clicked.connect(self.stop_ping)
        self.blockAllBtn.clicked.connect(self.block_all)

    def populate_table(self):
        items = [
            {"destIpAddress": "192.168.1.1", "destMask": "255.255.255.0",
                "destPort": "8080", "sourceIp": "192222", "sourceMask": "2555"},
            {"destIpAddress": "192.168.1.1", "destMask": "255.255.255.0",
                "destPort": "8080", "sourceIp": "192222", "sourceMask": "2555"},
            {"destIpAddress": "192.168.1.1", "destMask": "255.255.255.0",
                "destPort": "8080", "sourceIp": "192222", "sourceMask": "2555"}
        ]

        row = 0
        self.tableWidget.setRowCount(len(items))
        for item in items:
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(item["destIpAddress"]))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(item["destMask"]))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(item["destPort"]))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(item["sourceIp"]))
            self.tableWidget.setItem(
                row, 4, QtWidgets.QTableWidgetItem(item["sourceMask"]))
            row += 1

    def send_ping(self):
        self.p = subprocess.Popen(["ping", "192.168.1.1"], shell=True)

    def stop_ping(self):
        subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.p.pid))

    def block_all(self):
        return 0


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(780)
widget.setFixedHeight(560)
widget.show()
app.exec_()