from models.cliente import Cliente
from utils.helper import str_para_date, float_para_moeda, date_para_str
from csv import DictReader, DictWriter
from datetime import datetime



class Conta:

    contador = 1

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.contador
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        self.__extrato: dict = {}
        Conta.contador = self.__numero + 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero_conta}\nCliente: {self.cliente.nome}\n'\
               f'Saldo total: {self.saldo_total}\nLimite: {self.limite}'
    
    @property
    def numero_conta(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def cliente_nome(self: object) -> object:
        return self.__cliente.nome

    @property
    def saldo(self: object):
        return self.__saldo
    
    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor
    @property
    def limite(self: object):
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self:object):
        return self.__saldo_total

    @property
    def extrato(self: object) -> None:
        print('|--------Extrato--------|\n')
        for indice, valor in self.__extrato.items():
            print(f'|Data da operação:{indice}---|{valor}\n')

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> str:
        self.__extrato[date_para_str(datetime.now())] = (f'Conta no nome de: {self.cliente.nome}|Saldo anterior:{self.saldo}'\
                                                                  f'|Saldo depois do deposito:{self.saldo+valor}')
        self.saldo = self.saldo + valor 
        return f'O valor de R${valor} foi depositado na conta com sucesso.'

    def sacar(self: object, valor: float) -> str:
        if self.saldo < valor:
            return 'Saldo menor que o valor de saque.'
        self.__extrato[date_para_str(datetime.now())] = (f'Conta no nome de: {self.cliente.nome}|Saldo anterior:{self.saldo}'\
                                                                  f'|Saldo depois do saque:{self.saldo - valor}')
        self.saldo = self.saldo - valor 
        return f'O valor de R${valor} foi depositado na conta com sucesso.'
    
    def transferir(self: object, conta_final: object, valor: float) -> str:
        transf_taxa = 1.10 
        if self.saldo < valor:
            return 'Saldo menor que o valor de da transferência.'
        self.__extrato[date_para_str(datetime.now())] = (f'Conta no nome de: {self.cliente.nome}|Saldo anterior:{self.saldo}|'\
                                                                  f'|Saldo depois da transferência:{self.saldo - valor}|'\
                                                                  f'Conta do beneficiário: {conta_final.cliente.nome}')
        self.saldo = self.saldo - (valor * transf_taxa)
        conta_final.__extrato[date_para_str(datetime.now())] = (f'Conta no nome de: {conta_final.cliente.nome}|Saldo anterior:{conta_final.saldo}'\
                                                          f'|Saldo depois da transferência:{conta_final.saldo + valor}'\
                                                          f'|Conta do beneficiário: {self.cliente.nome}')
        conta_final.saldo += valor 
        return f'O valor de R${valor} foi transferido com sucesso.'
