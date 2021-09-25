from random import choice
import os, sys


class TickTackToe:
    pontos_p_vitoria = 0
    pontos_p_vitoria1 = 0
    def __init__(self:object) -> None:
        self.valores = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

    def jogar(self: object) -> None:
        while True != False:
            resp = int(input("\nDeseja jogar o jogo da velha?\n1)Sim\n0)Não (Sair)\nR:"))
            if resp != 1:
                sys.exit(1)
            break
        os.system('cls')
        first_player = choice(('X', '0'))
        second_player = None
        if first_player == 'X':
            second_player = '0'
        else:
            second_player = 'X'
        jogador = 1
        jogadas = 1
        while jogadas <= 9:
            os.system('cls')
            self.interface()
            indice = int(input(f"{jogador}º jogador\nInsira a posição que deseja colocar:"))
            if jogador == 1:
                
                if self.valores_alterar(indice, first_player):
                    jogadas += 1
                    jogador += 1    
                    self.condicao(first_player)
                else:
                    pass
            else:
                if self.valores_alterar(indice, second_player):
                    jogadas += 1
                    jogador = 1
                    self.condicao(second_player)
        self.interface()
        print('Deu velha!')

    def interface(self: object) -> None:
        for x in range(len(self.valores.keys())+1): 
            if x % 3 > 0:
                if self.valores.get(x) == '':
                    print(f'{x}|', end='')
                elif self.valores.get(x) != '': 
                    print(f'{self.valores.get(x)}|', end='')
            else:
                if x != 0:
                    if self.valores.get(x) == '':
                        print(f'{x}|')
                    elif self.valores.get(x) != '': 
                        print(f'{self.valores.get(x)}|')
                else:
                    pass

    def valores_alterar(self: object, index: int, forma: str) -> bool:
        if self.valores[index] == '':
            if forma == 'X':
                self.valores[index] = 'X'
            else:
                self.valores[index] = '0'
            return True
        else:
            print('Já colocaram aí, tente novamente.')
            input('Aperte Enter para continuar.')
            return False

    def condicao(self: object, jogador: str):
        pontos = 0
        for x in range(1, 4):
            if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(4, 7):
            if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(7, 10):
            if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(1, 9, 3):
            if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(2, 9, 3):
            if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(1, 8, 3):
            if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(3, 10, 3):
           if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        for x in range(1, 10, 4):
           if self.valores[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(1)
        pontos = 0
        if self.valores[3] == jogador and self.valores[5] == jogador and self.valores[7] == jogador:
            print(f"{jogador} Wins!!") 
            sys.exit(1)


play = TickTackToe()
play.jogar()
