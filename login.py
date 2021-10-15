# -*- coding: utf-8 -*-
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
from chatMain import *
import configparser
#待筛选
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import img
class login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 334)
        MainWindow.setWindowIcon(QIcon(":/img/addlogo.png"))
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        MainWindow.setStyleSheet(

"    background-color: gray;\n"




)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet( 
            "border-radius: 10px;")
        # pat2 = QPainter(self.centralwidget)
        # pat2.setRenderHint(pat2.Antialiasing) # 抗锯齿
        # pat2.setBrush(Qt.white)
        # pat2.setPen(Qt.transparent)
        # rect = self.rect()
        # rect.setLeft(19)
        # rect.setTop(19)
        # rect.setWidth(rect.width()-9)
        # rect.setHeight(rect.height()-9)
        # pat2.drawRoundedRect(rect, 4, 4)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(365, 10, 25, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("")
        #self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 280, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 230, 71, 31))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 70, 151, 141))
        self.frame.setStyleSheet("border-image: url(./img/login.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(160, 230, 31, 31))
        self.frame_2.setStyleSheet("border-image: url(:/img/shua.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #self.main_layout.setSpacing(0)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "登录账号"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">请使用哔哩哔哩客户端扫码登录</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">刷新二维码</span></p></body></html>"))

# requests.packages.urllib3.disable_warnings()

# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", 'Referer': "https://www.bilibili.com/"}
# headerss = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",  'Host': 'passport.bilibili.com','Referer': "https://passport.bilibili.com/login"}


# def chatshow():    
#     config = ConfigParser.ConfigParser()
#     config.read('config.ini', encoding="utf-8")
#     if not config.has_option("login", "uname"):  # 检查是否存在该option
#         chatshow()
#     else:
#         chatMain.show()
#         MainWindow.close()

# def islogin(session):
#     try:
#         session.cookies.load(ignore_discard=True)
#     except Exception:
#         pass
#     loginurl = session.get("https://api.bilibili.com/x/web-interface/nav", verify=False, headers=headers).json()
#     if loginurl['code'] == 0:
#         print('Cookies值有效，',loginurl['data']['uname'],'，已登录！')
#         #获取用户名
#         config = configparser.ConfigParser() # 类实例化
#         config.add_section('login') # 首先添加一个新的section
#         config.set('login','username',loginurl['data']['uname'])  # 写入数据
#         config.write(open('config.ini','w'))            #保存数据
#         # 定义文件路径
        
#         #保存用户头像
#         r = requests.get(loginurl['data']['face'])
#         with open('img/logo.jpg', 'wb') as f:
#             f.write(r.content) 
#         uname = loginurl['data']['uname']
#         print(uname)
#         # print(loginurl)
#         # MainWindow.close()
#         print("ini由第一个创建")
        

#         return session, True
#     else:
#         print('Cookies值已经失效，请重新扫码登录！')
#         return session, False


# def bzlogin():
#     if not os.path.exists('bzcookies.txt'):
#         with open("bzcookies.txt", 'w') as f:
#             f.write("")
#     session = requests.session()
#     session.cookies = cookielib.LWPCookieJar(filename='bzcookies.txt')
#     session, status = islogin(session)
#     if not status:
#         getlogin = session.get('https://passport.bilibili.com/qrcode/getLoginUrl', headers=headers).json()
#         loginurl = requests.get(getlogin['data']['url'], headers=headers).url
#         oauthKey = getlogin['data']['oauthKey']
#         qr = qrcode.QRCode()
#         qr.add_data(loginurl)
#         img = qr.make_image()
#         a = BytesIO()
#         img.save("./img/login.png")
#         # img.save(a, 'png')
#         # png = a.getvalue()
#         # a.close()
#         # t = showpng(png)
#         # t.start()
#         tokenurl = 'https://passport.bilibili.com/qrcode/getLoginInfo'
    
#         while True:
#             qrcodedata = session.post(tokenurl, data={'oauthKey': oauthKey, 'gourl': 'https://www.bilibili.com/'}, headers=headerss).json()
#             print(qrcodedata)
#             if '-4' in str(qrcodedata['data']):
#                 print('二维码未失效，请扫码！')
#             elif '-5' in str(qrcodedata['data']):
#                 print('已扫码，请确认！')
#             elif '-2' in str(qrcodedata['data']):
#                 print('二维码已失效，请重新运行！')
#             elif 'True' in str(qrcodedata['status']):
#                 print('已确认，登入成功！')
#                 session.get(qrcodedata['data']['url'], headers=headers)
#                 try:
#                     session.cookies.load(ignore_discard=True)
#                 except Exception:
#                     pass
#                 loginurl = session.get("https://api.bilibili.com/x/web-interface/nav", verify=False, headers=headers).json()
#                 if loginurl['code'] == 0:
#                     print('Cookies值有效，',loginurl['data']['uname'],'，已登录！')
#                     #获取用户名
#                     config = configparser.ConfigParser() # 类实例化
#                     config.add_section('login') # 首先添加一个新的section
#                     config.set('login','username',loginurl['data']['uname'])  # 写入数据
#                     config.write(open('config.ini','w'))            #保存数据
#                     # 定义文件路径
#                     print("ini由第二个创建")
                    
#                     #保存用户头像
#                     r = requests.get(loginurl['data']['face'])
#                     with open('/img/logo.jpg', 'wb') as f:
#                         f.write(r.content) 
#                     uname = loginurl['data']['uname']

#                     # print(loginurl)

#                 break
#             else:
#                 print('其他：', qrcodedata)
#             time.sleep(2)
            

#         session.cookies.save()
#         MainWindow.close()
#     return session


# if __name__ == "__main__":
#     t = threading.Thread(target=bzlogin)
#     t.start()
#     time.sleep(1)
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = login()
#     ui.setupUi(MainWindow)
#     ui2 = chatMain()
#     MainWindow.show()
#     # def chat():
#     #     while 1:
#     #         config = configparser.ConfigParser()
#     #         config.read('config.ini')  
#     #         if not config.has_section("login"):
#     #             pass
#     #         else:
#     #             ui2.show()
#     #             break
#     # t2 = threading.Thread(target = chat)
#     # t2.start()


#     sys.exit(app.exec_())

