from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta
from utils.helper import verif_cpf, str_para_date
from os import system
import sys


contas: List[Conta] = []


def menu() -> None:
    escolha = int(input('\nMenu de Opções:\n1)Extrato\n2)Depositar\n3)Transferência\n4)Saque\n5)Retornar\nEscolha:'))    
    if escolha == 1:
        retirar_extrato()
    elif escolha == 2:
        efetuar_deposito()
    elif escolha == 3:
        efetuar_transferencia()
    elif escolha == 4:
        efetuar_saque()
    elif escolha == 5:
        main()

    
def criar_conta() -> None:
    nome: str = input('Insira seu nome: ')
    sobrenome: str = input('Insira seu sobrenome: ')
    email: str = input('Insira seu email: ')
    senha: str = input('Insira sua senha: ')
    cpf: str = input('Insira seu CPF: ')
    while verif_cpf(cpf) == False:
        cpf: str = input('CPF inválido!.\nReinsira seu CPF: ')
    nascimento: str = input('Insira sua data de nascimento (dia/mes/ano):')
    while str_para_date(nascimento) == False:
        nascimento: str = input('A data inserida é invalida.\nReinsira sua data de nascimento (dia/mes/ano):')
    nome: Cliente = Cliente(nome=nome, sobrenome=sobrenome, email=email, cpf=cpf, nascimento=nascimento)
    conta = 'conta'+str(Conta.contador)
    conta: Conta = Conta(cliente = nome, senha=senha)
    contas.append(conta)
    print(f'Dados da conta: {conta}')
    input('Aperte Enter para continuar:')


def logar_conta() -> Conta:
    id = int(input('\nInsira o ID da sua conta: '))
    senha = input('Insira sua senha: ')
    try:
        for conta in contas:
            if  conta.numero_conta == id and conta.senha == senha:
                return conta
    except StopIteration:
        print('Conta não existente')    
    

def efetuar_saque() -> None:
    conta = logar_conta()
    valor = float(input('\nInsira o quanto você quer sacar:'))
    print(conta.saque(valor))
    sleep(1)
    system('cls')
    menu()


def efetuar_deposito() -> None:
    conta = logar_conta()
    valor = float(input('\nInsira o quanto você quer depositar:'))
    print(conta.depositar(valor))
    sleep(1)
    system('cls')
    menu()


def efetuar_transferencia() -> None:
    conta = logar_conta()
    valor = float(input('\nInsira o quanto você quer transferir:'))
    conta_final = int(input('Insira o Número da conta para qual você quer efetuar a transferência'))
    print(conta.transferir(buscar_conta_por_numero(conta_final), valor))
    sleep(1)
    system('cls')
    menu()

def retirar_extrato() -> dict:
    conta = logar_conta()
    conta.extrato
    sleep(1)
    system('cls')
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        for conta in contas:
            print(conta.name)
            print('-------------------------------------------------\n')
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Cliente:
    for conta in contas:
        if numero == conta.numero_conta:
            pass_conta =  conta
            return pass_conta
    print('A conta não está cadastrada. Sendo redirecionado')
    menu()


def main() -> None:
    while True:
        print('--------------Banco Origin--------------\n\n--------------Menu de Opções--------------\n')
        escolha = int(input('1)Acessar Conta\n2)Criar conta\n3)Listar todas as contas\n4)Sair\nEscolha:   '))
        if escolha == 2:
            criar_conta()
        elif escolha == 3:
            listar_contas()
        elif escolha == 4:
            exit(1)
        else:
            break
        system('cls')
    menu()


if __name__ == '__main__':
    main()
    