import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QGridLayout, QPushButton, QLineEdit, QSizePolicy, QPlainTextEdit, QLabel
from PyQt5 import QtCore, QtWidgets, Qt


class Interface(QMainWindow):

    def __init__(self: object, parent=None) -> None:
        super().__init__(parent)
        
    def add_btn(self: object, btn: QPushButton, row: int, col: int, rowspan: int, colspan: int, funcao=None, style=None) -> bool:
        self.grid.addWidget(btn, row, col, colspan, rowspan)
        btn.clicked.connect(lambda: funcao.show())
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding) 
        return True

    def janela(self, x: int, y: int) -> None:
        self.setWindowTitle('Projeto Banco. V.1.0')
        self.setFixedSize(x, y)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)


    def deploy_texto(self: object, texto: str, col: int, row: int, colspan: int, rowspan: int) -> None:
        self.display = QLabel(texto)
        self.display.setAlignment(QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.display, row, col, rowspan, colspan)
        self.display.setStyleSheet('*{background: #f3f1f1; color: black; font-weight: 700; font-size:30px}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def insere_texto(self: object, col: int, row: int, colspan: int, rowspan: int) -> None:
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()
        self.grid.addWidget(self.display, row, col, rowspan, colspan)
        self.display.setStyleSheet('*{background: white; color: 000; font-weight: 700; font-size:30px}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setCentralWidget(self.cw)

class JanelaPrincipal(Interface):

    def __init__(self: object) -> None:
        super().__init__()
        self.janela(800, 600)
        display = self.deploy_texto('ATM\nBanco Origin', 0, 0, 7, 5)
        logar = self.add_btn(QPushButton('Logar'), 5, 1, 2, 2, funcao=JanelaLogin(), style='background: gray; color: #fff; font-weight:500; font-size:24')
        criar = self.add_btn(QPushButton('Criar'), 5, 4, 2, 2, funcao=JanelaCadastro(), style='background: gray; color: #fff; font-weight:500; font-size:24')


class JanelaLogin(Interface):
    
    def __init__(self: object):
        super().__init__()
        self.janela(800, 600)
        nome_usuario = self.insere_texto(1, 1, 0, 2)
        display = self.deploy_texto('Digite seu nome', 0, 0, 0, 2)
        email = self.insere_texto(3, 1, 0, 2)
        display1 = self.deploy_texto('Digite seu email', 2, 0, 0, 2)
        senha = self.insere_texto(5, 1, 0, 2)
        display2 = self.deploy_texto('Digite sua senha', 4, 0, 0, 2)
        cpf = self.insere_texto(4, 1, 1, 2)
        display = self.deploy_texto('Digite seu CPF e sua data de nascimento', 5, 0, 0, 2)
        nascimento = self.insere_texto(5, 3, 1, 2)
        
        

    



class JanelaCadastro(Interface):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aplication = JanelaPrincipal()
    aplication.show()
    app.exec_()