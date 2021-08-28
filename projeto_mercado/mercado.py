from models.produtos import Produtos
from utils.helper import float_para_moeda
from typing import List
from os import system
from time import sleep
import sys

produtos: List[Produtos] = []


def cadastro_produto() -> None:
    while True:
        while True:
            nome_produto: str = input('Insira o nome do produto:')
            valor_compra_produto: float = float(input('Insira o valor de compra do produto:'))
            valor_venda_produto: float = float(input('Insira o valor de venda do produto:'))
            quantidade_produto: int = int(input('Insira quantas quantidades tem no estoque:'))
            sleep(0.5)
            system('cls')
            opcao = int(input(f'O produto: \nNome:{nome_produto}\nValor de compra:{valor_compra_produto}\n'\
                            f'Valor de compra:{valor_venda_produto}\nSerá adicionado, confirmação:\n\n1)Sim\n2)Não\nR:'))
            if opcao == 1:
                produto = Produtos(nome=nome_produto, valor_compra=valor_compra_produto,
                                   valor_venda=valor_venda_produto, unidades_lotes=quantidade_produto)
                produtos.append(produto)
                break
        sleep(0.5)
        system('cls')
        opc = int(input('Deseja continuar adicionando produtos?\n1)Sim\n2)Não\nR:'))
        sleep(0.5)
        system('cls')
        if opc == 2:
            break
    

def venda() -> None:
    carrinho: dict = {}
    while True:
        id_produto = int(input('Insira o ID do Produto:'))
        produto_comprar = achar_produto(id_produto)
        print(f'\nInformações do Produto:\nNome:{produto_comprar.nome}\n'\
              f'Preço:{float_para_moeda(produto_comprar.valor_venda)}\n')
        quantidade = int(input('Insira a quantidade do produto:'))
        valor_produto: float = produto_comprar.venda_produto(quantidade)
        carrinho[produto_comprar.nome] = float(valor_produto)
        opcao = int(input('\nDeseja continuar adicionando produtos:\n1)Sim\n2)Não\nR:'))
        sleep(0.5)
        system('cls')
        if opcao == 2:
            break
    cpf = input('Deseja colocar CPF na nota? (Digite o CPF caso queira)\nCPF:')
    system('cls')
    for produto, valor in carrinho.items():
        print(f'Todos os produtos com os valores equivalentes:\nProduto:{produto}|Valor:{float_para_moeda(valor)}')
    print(f'Valor total: {float_para_moeda(sum(carrinho.values()))}\nCPF:{cpf}')
    input('Para continuar, pressione enter:')
    sleep(0.5)
    system('cls')
    

def achar_produto(id_produto_recebido: int) -> Produtos:
    for produto in produtos:
        if produto.id_produto == id_produto_recebido:
            pass_produto = produto
            return pass_produto
    print('Nenhum produto foi encontrado.')
    main()


def main() -> None:
    while True:
        print('------------------ Mercado do Rosário ------------------\n')
        opcao = int(input('1)Adicionar Produto\n2)Atualizar Produto:\n3)Realizar Venda\n4)Verificar Produtos Cadastrados'\
                          '\n5)Sair\nR:'))
        if opcao == 1:
            print('\nVocê está sendo direcionado para a tela de cadastro de produtos.')
            sleep(1.0)
            system('cls')
            cadastro_produto()
            system('cls')
        if opcao == 2:
            id_produto = int(input('Insira o ID do produto:'))
            sleep(1.5)
            system('cls')
            produto: Produtos = achar_produto(id_produto)
            produto.att_produto()
        if opcao == 3:
            print('\nSendo redirecionado para a área de vendas:')
            sleep(1.5)
            system('cls')
            venda()
        if opcao == 4:
            sleep(1.5)
            system('cls')
            for produto in produtos:
                print(produto)
            input('Pressione uma tecla para retornar ao menu inicial.')
        if opcao == 5:
            print('\nVocê está saindo do programa!')
            sleep(1.5)
            system('cls')
            sys.exit(0)


if __name__ == "__main__":
    main()
