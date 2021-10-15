
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import resources_rc
from chatMain import *
import img


class guan(QtWidgets.QMainWindow):
    def __init__(self):
        super(guan,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 403)
        MainWindow.setWindowIcon(QIcon(":/img/logo.jpg"))
        MainWindow.setWindowFlags(QtCore.Qt.Tool)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(335, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 451, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 90, 411, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 130, 261, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 360, 261, 16))
        self.label_7.setObjectName("label_7")
        copyright = '''
        <div style="text-align:center;font-size: 12px;font-family: 'Arial'; color:#616161;"><b> Copyright © 2021 daiguoxi.All Rights Reserved.</b></div>
        '''
        self.label_7.setText(copyright)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 160, 461, 16))
        self.label_8.setObjectName("label_8")
        shuoming = '''
        <div style="text-align:center;font-size: 12px;font-family: 'Arial'; color:red;"><b>警告：请勿用于非法用途，一切非法使用所造成的后果由使用者个人承担！</b></div>
        '''
        self.label_8.setText(shuoming)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 190, 131, 121))
        self.widget.setStyleSheet("border-image: url(:/img/gzh.jpg);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(390, 190, 131, 121))
        self.widget_2.setStyleSheet("border-image: url(:/img/wx.jpg);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 330, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 330, 51, 20))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "关于"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">关于</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>作者：DGX||软件名：哔哩哔哩群发信息||开发语言：Python||时间：2021/7/17</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>微信公众号\\B站\\YouTube：DGX杂学，有什么疑问和建议，请在以上平台留言</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>邮箱：<a href=\"daiguoxi22@163.com\"><span style=\" text-decoration: underline; color:#0000ff;\">daiguoxi22@163.com</span></a></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>微信公众号</p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>作者微信</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = guan()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
