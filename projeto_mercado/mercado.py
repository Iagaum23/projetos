from models.produtos import Produtos


def cadastro_produto():
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
            

if __name__ == "__main__":
    main()