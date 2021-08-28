from datetime import datetime, date
from utils.helper import float_para_moeda, date_para_str, str_para_date

class Produtos:

    produtos_cadastrados: int = 1

    def __init__(self, *,  nome: str, unidades_lotes: int, valor_compra: float, valor_venda: float):
        self.__nome: str = nome
        self.__unidades_lotes: int = unidades_lotes
        self.__valor_compra: float = valor_compra
        self.__valor_venda: float = valor_venda
        self.__horario_de_att: date = datetime.now()
        self.__id_produto: int = Produtos.produtos_cadastrados
        Produtos.produtos_cadastrados = self.id_produto + 1
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def id_produto(self: object) -> int:
        return self.__id_produto

    @property
    def valor_compra(self: object) -> float:
        return self.__valor_compra

    @property
    def valor_venda(self: object) -> float:
        return self.__valor_venda
    
    @property
    def unidades_lotes(self: object) -> int:
        return self.__unidades_lotes
    
    def att_produto(self: object) -> None:
        while True:
            opcao = int(input('O que será atualizado no produto\n1) Preço:   2)Quantidade\n'))
            if opcao == 1:
                novo_valor = float(input(f'Valor atual:{self.valor_venda}\nNovo valor:'))
                self.__valor_venda = novo_valor
                self.__horario_de_att = datetime.now()
            if opcao == 2:
                novo_valor = float(input(f'Valor atual:{self.unidades_lotes}\nNovo valor:'))
                self.__unidades_lotes = novo_valor
                self.__horario_de_att = datetime.now()
            if cont:= int(input('Deseja continuar a fazer alterações no produto?\n1) Sim\n2) Não ')) == 2:
                break
    
    def venda_produto(self: object, qtd: int) -> float:
        self.__unidades_lotes = self.unidades_lotes - qtd
        return float(self.valor_venda)
    
    def __len__(self: object) -> int:
        return Produtos.produtos_cadastrados

    def __str__(self: object) -> str:
        return f'Nome do produto:{self.nome} | Preço de venda do produto:{float_para_moeda(self.valor_venda)}'\
               f'\n|Preço de compra do produto:{float_para_moeda(self.valor_compra)}'\
               f'\nUnidades totais do Produto:{self.unidades_lotes}\nHorário de atualização:{self.__horario_de_att}'
        