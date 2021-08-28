from models.produtos import Produtos
from typing import List
from os import system
from time import sleep
import sys

produtos: List[Produtos] = []

def cadastro_produto() -> None:
    while True:
        nome_produto: str = input('Insira o nome do produto:')
        valor_compra_produto: float = input('Insira o valor de compra do produto:')
        valor_venda_produto: float = input('Insira o valor de venda do produto:')
        if opcao:= int(input(f'O produto: \nNome:{nome_produto}'/
                             f'Valor de compra:{valor_compra_produto}\n'/
                             f'Valor de compra:{valor_venda_produto}'/ 
                             f'\nSerá adicionado, confirmação:\n1)Sim\n2)Não')) == 1:
            break
    produto = Produtos(nome=nome_produto, valor_compra=valor_compra_produto, valor_venda=valor_venda_produto)
    produtos.append(produto)


def venda() -> None:
    while True:
        id_produto = int(input('Insira o ID do Produto:'))
        produto_comprar = achar_produto(id_produto)
        quantidade = int(input('Insira a quantidade do produto:'))
        produto_comprar(quantidade)
        


def achar_produto(id_produto_recebido: int) -> Produtos:
    for produto in produtos:
        if produto.id_produto == id_produto_recebido:
            pass_produto = produto
            return pass_produto
    print('Nenhum produto foi encontrado.')
    main()


def main() -> None:
    print('------------------ Mercado do Rosário ------------------\n')
    opcao = int(input('1)Adicionar Produto\n2)Atualizar Produto:\n3)Realizar Venda\n4)Sair\nR:'))
    if opcao == 1:
        print('Você está sendo direcionado para a tela de cadastro de produtos.\nInsira qualquer tecla para'\
              'Continuar.')
        sleep(1.5)
        system('cls')
        cadastro_produto()
    if opcao == 2:
        id_produto = int(input('Insira o ID do produto:'))
        sleep(1.5)
        system('cls')
        produto: Produtos = achar_produto(id_produto)
        produto.att_produto()
    if opcao == 3:
        venda()
    if opcao == 4:
        sys.exit(0)


if __name__ == "__main__":
    main()
