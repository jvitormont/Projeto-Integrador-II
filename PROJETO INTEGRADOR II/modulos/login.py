from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtWidgets
import sys
import sqlite3

from template.tela import Ui_MainWindow
from template.login import Ui_login
from template.cadastrar import Ui_cadastrar


class sqlite_db:
    def __init__(self, banco=None):
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão criada com sucesso!")
        except sqlite3.Error as e:
            print("Não foi possível estabelecer conexão!")

    def criar_tabelas(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            acesso INTEGER
        )""")

    def inserir_apaga_atualiza(self, query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def pega_dados(self, query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()


# Inicializa o banco de dados
db = sqlite_db("manager.db")
db.criar_tabelas()





class Cadastrar(QDialog):
    def __init__(self, *args, **argvs):
        super(Cadastrar, self).__init__(*args, **argvs)
        self.ui = Ui_cadastrar()
        self.ui.setupUi(self)
        self.ui.btnADD.clicked.connect(self.add)
        self.ui.btnC.clicked.connect(self.limpar)

    def add(self):
        db = sqlite_db("manager.db")
        name = self.ui.inputNOME.text().strip()
        docu = self.ui.inputCPF.text().strip()
        end = self.ui.inputENDERECO.text().strip()
        id = self.ui.inputID.text().strip()
        set = self.ui.inputSETOR.text().strip()
        adm = 1

        if not name or not docu or not end or not id or not set:
            QMessageBox.information(self, "OPA PA", "Preencha todos os campos!")
            return

        try:
            db.inserir_apaga_atualiza(
                "INSERT INTO funcs (id, nome, documento, endereco, setor, admin) VALUES (?, ?, ?, ?, ?, ?)",
                (id, name, docu, end, set, adm)
            )
            QMessageBox.information(self, "OPA PA", "DADOS GRAVADOS COM SUCESSO!")
            self.limpar()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao inserir os dados: {e}")

    def limpar(self):
        self.ui.inputNOME.setText("")
        self.ui.inputCPF.setText("")
        self.ui.inputENDERECO.setText("")
        self.ui.inputID.setText("")
        self.ui.inputSETOR.setText("")




class TelaPrincipal(QMainWindow):
    def __init__(self, *args, **argvs):
        super(TelaPrincipal, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.abrir_cadastrar)

    
    def abrir_cadastrar(self):
        # Abre a tela de cadastro
        self.cadastro_window = Cadastrar()
        self.cadastro_window.exec_()  # exec_() bloqueia a tela principal até que a de cadastro seja fechada

    



class Login(QDialog):
    def __init__(self, *args, **argvs):
        super(Login, self).__init__(*args, **argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)

        # Conecta o botão de login ao método de validação
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        user = self.ui.lineEdit_3.text()  # Campo para o login (usuário)
        passwd = self.ui.lineEdit_2.text()  # Campo para a senha

        if user == "" or passwd == "":
            QMessageBox.warning(self, "Alerta!", "Preencha todos os campos!")
        else:
            dados = db.pega_dados(f"SELECT acesso FROM user WHERE username = '{user}' and password = '{passwd}'")
            if dados:
                QMessageBox.information(self, "Login realizado!", "ENTROU COM SUCESSO!")
                self.abrir_tela_principal()
            else:
                QMessageBox.warning(self, "Login errado!", "NÃO ENTROU COM SUCESSO!")

    def abrir_tela_principal(self):
        # Fecha a janela de login e abre a tela principal
        self.accept()  # Fecha o QDialog de login com status "aceito"
        self.tela_principal = TelaPrincipal()
        self.tela_principal.show()


# Inicialização da aplicação
app = QApplication(sys.argv)

# Cria a janela de login como a janela inicial
window = Login()
if window.exec_() == QDialog.Accepted:
    sys.exit(app.exec_())
