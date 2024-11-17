from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

from template.cadastrar import Ui_cadastrar  # Certifique-se de que o arquivo está configurado corretamente
from db.query import sqlite_db  # Certifique-se de que o módulo sqlite_db está implementado

class Cadastrar(QDialog):
    def __init__(self, *args, **kwargs):
        super(Cadastrar, self).__init__(*args, **kwargs)
        self.ui = Ui_cadastrar()
        self.ui.setupUi(self)

        # Conectando botões às funções
        self.ui.btnadd.clicked.connect(self.add)
        self.ui.btnc.clicked.connect(self.cancelar)
        self.ui.btn1.clicked.connect(self.limpar)

    def add(self):
        """Adiciona um registro ao banco de dados."""
        db = sqlite_db("manager.db")  # Inicializa o banco de dados

        # Coleta dados dos campos de entrada
        name = self.ui.inputnome.text()
        ender = self.ui.inputend.text()
        rgst = self.ui.inputrgst.text()
        iden = self.ui.inputiden.text()
        str = self.ui.inputstr.text()

        # Validação de campos vazios
        if not name or not ender or not rgst or not iden or not str:
            QMessageBox.information(self, "OPA PA", "Preencha todos os campos!")
            return

        # Validação de rgst como número
        if not rgst.isdigit():
            QMessageBox.information(self, "OPA PA", "O campo 'Registro' deve conter apenas números!")
            return

        rgst = int(rgst)  # Converte para número inteiro

        # Insere os dados no banco de dados
        query = "INSERT INTO funcionarios (nome, endereco, registro, identidade, status) VALUES (?, ?, ?, ?, ?)"
        db.inserir_apaga_atualiza(query, (name, ender, rgst, iden, str))
        QMessageBox.information(self, "OPA PA", "DADOS GRAVADOS COM SUCESSO!")

    def cancelar(self):
        """Fecha a janela de cadastro."""
        self.close()

    def limpar(self):
        """Limpa os campos de entrada."""
        self.ui.inputnome.clear()
        self.ui.inputend.clear()
        self.ui.inputrgst.clear()
        self.ui.inputiden.clear()
        self.ui.inputstr.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cadastrar()
    window.show()
    sys.exit(app.exec_())
