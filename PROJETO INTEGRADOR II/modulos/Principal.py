from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import Qt
from PyQt5 import pyqtSlot
from PyQt5.QtCore import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from template.tela import Ui_MainWindow
from modulos import cadastrar


class TelaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.abrir_cadastrar)

    def add(self):
        add = cadastrar()
        add.exec_()







