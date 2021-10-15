# -*- coding: utf-8 -*-
import re
import subprocess
from lxml import etree
from login import *
import requests
import configparser
from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode
from threading import Thread
import time
import requests
from io import BytesIO
import http.cookiejar as cookielib
from PIL import Image
import os
import threading
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from bq import *
from guanyu import *
import webbrowser
import img
import subprocess

#说明，7/18改了图片路径就登录不了了
class chatMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):

        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 547)
        MainWindow.setWindowTitle("哔哩哔哩群发信息")
        MainWindow.setWindowIcon(QIcon(":/img/Blogo.png"))
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        MainWindow.setStyleSheet(
            "    background-color: rgba(234, 234, 234, 100%);\n"
            )


        config = configparser.ConfigParser() # 类实例化
        config = configparser.ConfigParser() # 类实例化
        config.read('config.ini') # 首先添加一个新的section
        self.desktopWidth = QApplication.desktop().width()  # 获取当前桌面的宽
        self.desktopHeight = QApplication.desktop().height()  # 获取当前桌面的高

        self.is_switching = False
        self.is_pause = True
        self.visitFlag = False
        self.is_switching2 = False
        self.is_pause2 = True
        self.visitFlag2 = False
        self.message = ""
        self.status =""
        url = 'https://blog.csdn.net/dgxl22/article/details/119023891'
        url2 = "https://www.cnblogs.com/yeu4h3uh2/p/15048133.html"
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',}

        response = requests.get(url=url,headers=headers)
        response2 = requests.get(url=url2,headers = headers)
        if response.status_code == 200 or response2.status_code== 200:
            html = etree.HTML(response.text)
            html2 = etree.HTML(response2.text)
            ips = html.xpath('//*[@id="content_views"]/blockquote[2]/p/text()')
            ips2 = html2.xpath('//*[@id="cnblogs_post_body"]/blockquote[2]/p/text()')
            message = str(ips[0])
            message2 = str(ips2[0])
            if message == "1" or message == "1":
                self.status = "1"
            else:
                self.status =="0"
                pass
        else:
            self.status="0"
            pass
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setStyleSheet(            "border-radius: 10px;")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 131, 501))
        self.frame_5.setStyleSheet("background-color: gray;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")


        self.pushButtonTui = QtWidgets.QPushButton(self.frame_5)
        self.pushButtonTui.setGeometry(QtCore.QRect(30, 140, 75, 23))
        self.pushButtonTui.setObjectName("pushButton")
        self.pushButtonTui.setText("退出")
        self.pushButtonTui.setStyleSheet("QPushButton{\n"
"    border:1px solid red;\n"
"border-bottom: 1px solid red;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    font-family:Helvetica, Arial, sans-serif;\n"

"}\n"
"QPushButton:hover{\n"

"       border-left: 4px solid red;" 
"  font-weight: 700;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(655, 20, 25, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("")
        #self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    max-width: 20px;\n"
"min-width: 20px;\n"
"    max-height: 20px;\n"
"    min-height: 20px;\n"
"    background-color: #F76677;\n"
"    border-radius: 10px;\n"

"}\n"
"QPushButton:hover{\n"

"    background-color: red;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(625, 20, 25, 22))
        self.pushButton_8.setObjectName("pushButton_7")
        self.pushButton_8.setText("")
        #self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    max-width: 20px;\n"
"min-width: 20px;\n"
"    max-height: 20px;\n"
"    min-height: 20px;\n"
"    background-color: #6DDF6D;\n"
"    border-radius: 10px;\n"

"}\n"
"QPushButton:hover{\n"

"    background-color: green;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(595, 20, 25, 22))
        self.pushButton_9.setObjectName("pushButton_7")
        self.pushButton_9.setText("")
        #self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    max-width: 20px;\n"
"min-width: 20px;\n"
"    max-height: 20px;\n"
"    min-height: 20px;\n"
"    background-color: #F7D674;\n"
"    border-radius: 10px;\n"

"}\n"
"QPushButton:hover{\n"

"    background-color: yellow;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        config = configparser.ConfigParser() # 类实例化
        config.read('config.ini') # 首先添加一个新的section
        # while 1:
        if config.has_section("login"):
            self.pushButton.setText("退出")
        else:
            self.pushButton.setText("登录")
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:1px solid red;\n"
"border-bottom: 1px solid red;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    font-family:Helvetica, Arial, sans-serif;\n"

"}\n"
"QPushButton:hover{\n"

"       border-left: 4px solid red;" 
"  font-weight: 700;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 465, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{\n"

"border-radius: 2px;\n"
"background-color:#00a1d6;\n"
"    font-family: '微软雅黑';\n"
"    color: #fff;\n"
"    font-size: 13px;\n"

"}\n"
"QPushButton:hover{\n"

"    background:#c8c8c8\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(40, 110, 81, 16))
        self.label.setObjectName("label")
        if config.has_section("login"):
            self.label.setText(config.get("login","username"))
        else:
            self.label.setText("未登录")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 0, 21, 501))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(130, 490, 491, 30))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(610, 70, 20, 431))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 128, 481, 211))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("border-radius: 10px;"
            "background-color: rgba(255, 255, 255, 100%);"
            
            )
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 60, 490, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 90, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 90, 21, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 370, 481, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet("border-radius: 10px;"
            
            )
        self.textEdit_2.setPlaceholderText("请在这里输入信息")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 30, 161, 21))
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 71, 71))
        self.frame.setStyleSheet("border-image: url(./img/logo.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        if os.path.exists("./img/logo.jpg"):
            self.frame.setStyleSheet(
                "border-image: url(./img/logo.jpg);"
                "max-width: 80px;"
                "min-width: 80px;"
                "max-height: 80px;"
                "min-height: 80px;"
                "border-radius: 40px;"
                )
        else:
            self.frame.setStyleSheet(
                "border-image: url(:/img/addlogo.png);"
                "max-width: 80px;"
                "min-width: 80px;"
                "max-height: 80px;"
                "min-height: 80px;"
                "border-radius: 40px;"
                )
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 280, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("反馈与帮助")
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"border-bottom: 1px solid blue;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"    font-family:Helvetica, Arial, sans-serif;\n"

"}\n"
"QPushButton:hover{\n"

"       border-left: 4px solid red;" 
"  font-weight: 700;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 380, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"border-bottom: 1px solid blue;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"    font-family:Helvetica, Arial, sans-serif;\n"

"}\n"
"QPushButton:hover{\n"

"       border-left: 4px solid red;" 
"  font-weight: 700;\n"
"}\n"
"QPushButton:pressed{\n"

"    background:#7e7e7e\n"
"}")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(420, 15, 41, 41))
        self.frame_2.setStyleSheet("border-image: url(:/img/feiji.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(200, 15, 41, 41))
        self.frame_6.setStyleSheet("border-image: url(:/img/Blogo.png);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(140, 340, 30, 30))
        #self.frame_3.setStyleSheet("background-color: rgb(58, 255, 64);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(175, 340, 30, 30))
        #self.frame_4.setStyleSheet("background-color: rgb(110, 255, 43);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("border-image: url(:/img/addimg.png);")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("border-image: url(:/img/addbq.png);")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("请输入开始uid")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("border-bottom: 1px solid blue;")
        self.lineEdit_2.setPlaceholderText("请输入结束uid")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(190, 230, 171, 110))
        self.frame_6.setStyleSheet("background-color: #e4e5e6;"
            "border-radius: 10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.hide()

        self.frame_21 = QtWidgets.QFrame(self.frame_6)
        self.frame_21.setGeometry(QtCore.QRect(20, 60, 31, 31))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_21.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.setStyleSheet("border-image: url(:/img/[doge].png);")
        self.pushButton_21.clicked.connect(self.doge)
        self.frame_31 = QtWidgets.QFrame(self.frame_6)
        self.frame_31.setGeometry(QtCore.QRect(70, 20, 31, 31))
        #self.frame_31.setStyleSheet("background-color: rgb(49, 255, 83);")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_31.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_31.setStyleSheet("border-image: url(:/img/[tv_doge].png);")
        self.pushButton_31.clicked.connect(self.tv_doge)
        self.frame_51 = QtWidgets.QFrame(self.frame_6)
        self.frame_51.setGeometry(QtCore.QRect(120, 20, 31, 31))
        #self.frame_51.setStyleSheet("background-color: rgb(49, 255, 83);")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_51)
        self.pushButton_41.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_41.setStyleSheet("border-image: url(:/img/[打call].png);")
        self.pushButton_41.clicked.connect(self.dacall)
        self.frame_41 = QtWidgets.QFrame(self.frame_6)
        self.frame_41.setGeometry(QtCore.QRect(70, 60, 31, 31))
        #self.frame_41.setStyleSheet("background-color: rgb(49, 255, 83);")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.pushButton_61 = QtWidgets.QPushButton(self.frame_41)
        self.pushButton_61.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_61.setStyleSheet("border-image: url(:/img/[tv_点赞].png);")
        self.pushButton_61.clicked.connect(self.tv_good)
        self.frame_61 = QtWidgets.QFrame(self.frame_6)
        self.frame_61.setGeometry(QtCore.QRect(20, 20, 31, 31))
        #self.frame_61.setStyleSheet("background-color: rgb(49, 255, 83);")
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.pushButton1 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton1.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton1.setText("")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("border-image: url(:/img/[支持].png);")
        self.pushButton1.clicked.connect(self.zhichi)
        self.frame_71 = QtWidgets.QFrame(self.frame_6)
        self.frame_71.setGeometry(QtCore.QRect(120, 60, 31, 31))
        #self.frame_71.setStyleSheet("background-color: rgb(49, 255, 83);")
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.pushButton_51 = QtWidgets.QPushButton(self.frame_71)
        self.pushButton_51.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.setStyleSheet("border-image: url(:/img/[tv_大哭].png);")
        self.pushButton_51.clicked.connect(self.tv_daku)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.play)
        self.pushButton.clicked.connect(self.showchat)
        self.pushButton_2.clicked.connect(self.saveMessage)
        self.pushButton_2.clicked.connect(self.sendMessage)
        self.pushButton_7.clicked.connect(self.winclose)
        self.pushButton_3.clicked.connect(self.help)
        self.pushButton_4.clicked.connect(self.about)
        self.pushButton_5.clicked.connect(self.demo)
        self.pushButton_6.clicked.connect(self.addphiz)
        self.pushButton_8.clicked.connect(self.winmin)
        self.pushButton_9.clicked.connect(self.visitWindow)
        self.pushButtonTui.clicked.connect(self.tui)

        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def tv_doge(self):
        self.textEdit_2.append("[tv_doge]")
    def doge(self):
        self.textEdit_2.append("[doge]")
    def tv_daku(self):
        self.textEdit_2.append("[tv_大哭]")
    def tv_good(self):
        self.textEdit_2.append("[tv_点赞]")
    def dacall(self):
        self.textEdit_2.append("[打call]")
    def zhichi(self):
        self.textEdit_2.append("[支持]")
    def addphiz(self):
        if self.is_pause2 or self.is_switching2:
            #self.player.play()
            #self.textEdit.append("运行中...")
            self.is_pause2 = False
            self.frame_6.show()
        elif (not self.is_pause2) and (not self.is_switching2):
            #self.player.pause()
            #self.textEdit.append("暂停中...")
            self.is_pause2 = True
            self.frame_6.hide()


    def tui(self):
        my_file = './bzcookies.txt' # 文件路径
        if os.path.exists(my_file): # 如果文件存在
            #删除文件，可使用以下两种方法。
            os.remove(my_file) # 则删除
            #os.unlink(my_file)
        else:
            pass

        my_file2 = './config.ini' # 文件路径
        if os.path.exists(my_file2): # 如果文件存在
            #删除文件，可使用以下两种方法。
            os.remove(my_file2) # 则删除
            #os.unlink(my_file)
        else:
            pass
        my_file3 = './img/logo.jpg' # 文件路径
        if os.path.exists(my_file3): # 如果文件存在
            #删除文件，可使用以下两种方法。
            os.remove(my_file3) # 则删除
            #os.unlink(my_file)
        else:
            pass
        my_file4 = './img/login.png' # 文件路径
        if os.path.exists(my_file4): # 如果文件存在
            #删除文件，可使用以下两种方法。
            os.remove(my_file4) # 则删除
            #os.unlink(my_file)
        else:
            pass

        ui.close()
        ui2.close()
        try:
            kill_command = 'taskkill /f /t /im 哔哩哔哩群发信息.exe'
            cc = subprocess.Popen(kill_command,shell=True)
        except:
            pass
    def demo(self):
        print("add img")
    def visitWindow(self):
        '''
        visit按钮对应的全屏or还原窗口大小
        '''
        if self.visitFlag == False:
            # self.showFullScreen()
            # self.showMaximized()
            self.lastWidth = self.width()
            self.lastHeight = self.height()
            self.resize(self.desktopWidth, self.desktopHeight)
            x = (self.desktopWidth - self.width()) // 2
            y = (self.desktopHeight - self.height()) // 2
            self.move(x, y)
            # print('max')
            self.visitFlag = True
        else:
            self.resize(self.lastWidth, self.lastHeight)
            x = (self.desktopWidth - self.width()) // 2
            y = (self.desktopHeight - self.height()) // 2
            self.move(x, y)
            # print('origin')
            self.visitFlag = False
    def help(self):
        webbrowser.open('https://space.bilibili.com/449154488')
    def about(self):
        ui4.show()
    def winclose(self):
        ui.close()
        try:
            kill_command = 'taskkill /f /t /im 哔哩哔哩群发信息.exe'
            cc = subprocess.Popen(kill_command,shell=True)
        except:
            pass
    def winmin(self):
        self.showMinimized()
    def showlogin(self):
        ui2.show()
    def showchat(self):
        def chat():
            config = configparser.ConfigParser() # 类实例化
            config.read('config.ini') # 首先添加一个新的section
            # while 1:
            if config.has_section("login"):
                self.frame.setStyleSheet(
        "border-image: url(./img/logo.jpg);"
        "max-width: 80px;"
        "min-width: 80px;"
        "max-height: 80px;"
        "min-height: 80px;"
        "border-radius: 40px;"
        )
                self.label.setText(config.get("login","username"))
                #print(config.get("login","username"))
                my_file = './bzcookies.txt' # 文件路径

                #     break
                # else:
                #     pass
                    
                    
                    
        t2 = threading.Thread(target = chat)
        t2.start()

    def play(self):
 
        if self.is_pause or self.is_switching:
            #self.player.play()
            #self.textEdit.append("运行中...")
            self.is_pause = False
            self.pushButton.setText('刷新')
            ui2.show()
        elif (not self.is_pause) and (not self.is_switching):
            #self.player.pause()
            #self.textEdit.append("暂停中...")
            self.is_pause = True
            self.pushButton.setText('退出')
            self.pushButton.close()
    def saveMessage(self):
        self.message = self.textEdit_2.toPlainText()

    def sendMessage(self):

        if self.status=="1":

            if os.path.exists("./config.ini"):
                def send():
                    if self.textEdit_2.toPlainText()!="":
                        f = open("bzcookies.txt","r",encoding='utf-8')
                        data = f.readlines()
                        f.close()
                        data = str(data)
                        resual = re.compile('Set-Cookie3:(.*?)path=').findall(data)
                        bzcookie = '{}'.format(resual[0])+'{}'.format(resual[1])+'{}'.format(resual[2])+'{}'.format(resual[3])+'{}'.format(resual[4])+'{}'.format(resual[-1])

                        # if int(self.lineEdit.text())>0 and int(self.lineEdit_2.text()>0):

                        n=int(self.lineEdit_2.text())-int(self.lineEdit.text())
                        for i in range(n):
                            try:
                                csrf_token=resual[3].replace(' bili_jct=','')
                                csrf = csrf_token.replace('; ','')
                                mid = resual[0].replace(' DedeUserID=','')
                                mid2 = mid.replace('; ','')
                                content = "{\"content\""+":"+"\""+self.message+"\"}"
                                headers = {
                                    'authority': 'api.vc.bilibili.com',
                                    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                                    'accept': 'application/json, text/plain, */*',
                                    'sec-ch-ua-mobile': '?0',
                                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
                                    'content-type': 'application/x-www-form-urlencoded',
                                    'origin': 'https://message.bilibili.com',
                                    'sec-fetch-site': 'same-site',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-dest': 'empty',
                                    'referer': 'https://message.bilibili.com/',
                                    'accept-language': 'zh-CN,zh;q=0.9',
                                    'cookie':'{}'.format(bzcookie.replace(' ','')),
                                }
                                data = {
                                  'msg[sender_uid]': '{}'.format(int(mid2)),
                                  'msg[receiver_id]': '{}'.format(int(self.lineEdit.text())+i),
                                  'msg[receiver_type]': '1',
                                  'msg[msg_type]': '1',
                                  'msg[msg_status]': '0',
                                  'msg[content]': '{}'.format(content),
                                  'msg[timestamp]': int(time.time()),
                                  'msg[new_face_version]': '0',
                                  'msg[dev_id]': 'e',
                                  'from_firework': '0',
                                  'build': '0',
                                  'mobi_app': 'web',
                                  'csrf_token': '{}'.format(csrf),
                                  'csrf': '{}'.format(csrf)
                                }

                                response = requests.post('https://api.vc.bilibili.com/web_im/v1/web_im/send_msg', headers=headers, data=data)
                                #print(response.text)
                            except:
                                self.textEdit.append("出现未知错误，请反馈给开发者")
                                pass
                    else:
                        self.textEdit.append("信息不能为空")
                s = threading.Thread(target=send)
                s.start()
            else:
                self.textEdit.append("请登录再发送信息")
                pass
            self.textEdit.append("[群发信息]"+self.textEdit_2.toPlainText())
            self.textEdit_2.setText("")
        else:
            self.textEdit.append("error 404!")
            self.textEdit.append("可能出错原因")
            self.textEdit.append("1、你自己网络问题")
            self.textEdit.append("2、软件可能被作者暂停服务")
            self.textEdit.append("请访问以下链接了解情况")
            self.textEdit.append("https://blog.csdn.net/dgxl22/article/details/119023891")
            self.textEdit.append("https://www.cnblogs.com/yeu4h3uh2/p/15048133.html")
    # 无边框的拖动
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)
 
    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())
 
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "哔哩哔哩群发信息"))
        #self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "发送"))
        #self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "设置参数："))
        self.label_3.setText(_translate("MainWindow", "UID:"))
        self.label_4.setText(_translate("MainWindow", "到"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">哔哩哔哩群发信息</span></p></body></html>"))

        self.pushButton_4.setText(_translate("MainWindow", "关于"))
        # self.pushButton_5.setText(_translate("MainWindow", "图片"))
        # self.pushButton_6.setText(_translate("MainWindow", "表情包"))

requests.packages.urllib3.disable_warnings()

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", 'Referer': "https://www.bilibili.com/"}
headerss = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",  'Host': 'passport.bilibili.com','Referer': "https://passport.bilibili.com/login"}


# def chatshow():    
#     config = ConfigParser.ConfigParser()
#     config.read('config.ini', encoding="utf-8")
#     if not config.has_option("login", "uname"):  # 检查是否存在该option
#         chatshow()
#     else:
#         chatMain.show()
#         MainWindow.close()
#         ui2.close()
#         MainWindow.show()

def islogin(session):
    try:
        session.cookies.load(ignore_discard=True)
    except Exception:
        pass
    loginurl = session.get("https://api.bilibili.com/x/web-interface/nav", verify=False, headers=headers).json()
    if loginurl['code'] == 0:
        print('Cookies值有效，',loginurl['data']['uname'],'，已登录！')
        #获取用户名
        config = configparser.ConfigParser() # 类实例化
        config.add_section('login') # 首先添加一个新的section
        config.set('login','username',loginurl['data']['uname'])  # 写入数据
        config.write(open('config.ini','w'))            #保存数据
        # 定义文件路径
        
        #保存用户头像
        r = requests.get(loginurl['data']['face'])
        with open('img/logo.jpg', 'wb') as f:
            f.write(r.content) 
        uname = loginurl['data']['uname']
        config.set('login','username',loginurl['data']['uname'])  # 写入数据
        config.write(open('config.ini','w'))  
        print(uname)
        # print(loginurl)
        # MainWindow.close()
        #print("ini由第一个创建")
        

        return session, True
    else:
        print('Cookies值已经失效，请重新扫码登录！')
        return session, False


def bzlogin():
    if not os.path.exists('bzcookies.txt'):
        with open("bzcookies.txt", 'w') as f:
            f.write("")
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='bzcookies.txt')
    session, status = islogin(session)
    if not status:
        getlogin = session.get('https://passport.bilibili.com/qrcode/getLoginUrl', headers=headers).json()
        loginurl = requests.get(getlogin['data']['url'], headers=headers).url
        oauthKey = getlogin['data']['oauthKey']
        qr = qrcode.QRCode()
        qr.add_data(loginurl)
        if os.path.exists('./img'):
            pass
        else:
            os.mkdir('./img')
        img = qr.make_image()
        a = BytesIO()
        img.save("./img/login.png")
        # img.save(a, 'png')
        # png = a.getvalue()
        # a.close()
        # t = showpng(png)
        # t.start()
        tokenurl = 'https://passport.bilibili.com/qrcode/getLoginInfo'
    
        while True:
            qrcodedata = session.post(tokenurl, data={'oauthKey': oauthKey, 'gourl': 'https://www.bilibili.com/'}, headers=headerss).json()
            print(qrcodedata)
            if '-4' in str(qrcodedata['data']):
                print('二维码未失效，请扫码！')
            elif '-5' in str(qrcodedata['data']):
                print('已扫码，请确认！')
            elif '-2' in str(qrcodedata['data']):
                print('二维码已失效，请重新运行！')
            elif 'True' in str(qrcodedata['status']):
                print('已确认，登入成功！')
                session.get(qrcodedata['data']['url'], headers=headers)
                try:
                    session.cookies.load(ignore_discard=True)
                except Exception:
                    pass
                loginurl = session.get("https://api.bilibili.com/x/web-interface/nav", verify=False, headers=headers).json()
                if loginurl['code'] == 0:
                    print('Cookies值有效，',loginurl['data']['uname'],'，已登录！')
                    #获取用户名
                    config = configparser.ConfigParser() # 类实例化
                    config.add_section('login') # 首先添加一个新的section
                    config.set('login','username',loginurl['data']['uname'])  # 写入数据
                    config.write(open('config.ini','w'))            #保存数据
                    # 定义文件路径
                    print("ini由第二个创建")

                    
                    #保存用户头像
                    r = requests.get(loginurl['data']['face'])
                    with open('img/logo.jpg', 'wb') as f:
                        f.write(r.content) 
                    uname = loginurl['data']['uname']
                    config.set('login','username',loginurl['data']['uname'])  # 写入数据
                    config.write(open('config.ini','w'))  

                    # print(loginurl)

                break
            else:
                print('其他：', qrcodedata)
            time.sleep(2)
            

        session.cookies.save()
        ui2.close()

    return session






if __name__ == "__main__":
    import sys
    t = threading.Thread(target=bzlogin)
    t.start()
    time.sleep(1)
    app = QtWidgets.QApplication(sys.argv)
    ui = chatMain()
    ui2 = login()
    ui3 = bq()
    ui4 = guan()
    ui.show()
    ui2.pushButton.clicked.connect(ui2.close)
    sys.exit(app.exec_())

