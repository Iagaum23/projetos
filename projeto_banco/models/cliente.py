from datetime import date
from utils.helper import date_para_str, str_para_date, imprime_cpf

class Cliente:
    
    contador = 100
    
    def __init__(self, nome: str , sobrenome: str, email: str, cpf: str, nascimento: str) -> None:
        self.__nome: str = nome
        self.__sobrenome: str = sobrenome
        self.__email: str = email
        self.__cpf: str = imprime_cpf(cpf)
        self.__id: int = Cliente.contador + 1
        self.__nascimento: date = str_para_date(nascimento)
        self.__data_cadastro: date = date.today()

    @property
    def id_conta(self: object) -> int:
        return self.__id

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def sobrenome(self: object) -> str:
        return self.__sobrenome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def nascimento(self: object) -> str:
        return self.date_para_str(self.__nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return self.date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'Código: {self.id_conta}\nNome: {self.nome}\nSobrenome: {self.sobrenome}\n'\
               f'E-mail: {self.email}\nCPF: {self.cpf}\nNascimento: {self.nascimento}\n'\
               f'Data de Cadastro: {self.data_cadastro}\n'
    