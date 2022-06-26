from random import choice
import os, sys


class TickTackToe:
    
    pontos_p_vitoria = 0
    pontos_p_vitoria1 = 0
    
    def __init__(self:object) -> None:
        self.posicoes_para_jogar = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        while True != False:
            resposta = int(input("\nDeseja jogar o jogo da velha?\n1)Sim\n0)Não (Sair)\nR:"))
            if resposta == 1:
                self.iniciar_jogo()
                break
            elif resposta == 0:
                sys.exit(0)

    def iniciar_jogo(self: object) -> None:
        os.system('cls')
        first_player = choice(('X', '0'))
        second_player = 'X' if first_player == '0' else '0'
        jogador = 1
        jogadas = 1
        while jogadas <= 9:
            os.system('cls')
            self.interface()
            indice = int(input(f"{jogador}º jogador\nInsira a posição que deseja colocar:"))
            if jogador == 1:
                if self.posicoes_para_jogar_alterar(indice, first_player):
                    jogadas += 1
                    jogador += 1    
                    self.condicao(first_player)
                else:
                    pass
            else:
                if self.posicoes_para_jogar_alterar(indice, second_player):
                    jogadas += 1
                    jogador = 1
                    self.condicao(second_player)
        self.interface()
        print('Deu velha!')

    def interface(self: object) -> None:
        for x in range(len(self.posicoes_para_jogar.keys())+1): 
            if x % 3 > 0:
                if self.posicoes_para_jogar.get(x) == '':
                    print(f'{x}|', end='')
                elif self.posicoes_para_jogar.get(x) != '': 
                    print(f'{self.posicoes_para_jogar.get(x)}|', end='')
            else:
                if x != 0:
                    if self.posicoes_para_jogar.get(x) == '':
                        print(f'{x}|')
                    elif self.posicoes_para_jogar.get(x) != '': 
                        print(f'{self.posicoes_para_jogar.get(x)}|')

    def interface_jogador_alterar(self: object, index: int, forma: str) -> bool:
        if self.posicoes_para_jogar[index] == '':
            if forma == 'X':
                self.posicoes_para_jogar[index] = 'X'
            else:
                self.posicoes_para_jogar[index] = '0'
            return True
        else:
            print('Já colocaram aí, tente novamente.')
            input('Aperte Enter para continuar.')
            return False

    def condicao(self: object, jogador: str):
        pontos = 0
        for x in range(1, 4):
            if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(4, 7):
            if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(7, 10):
            if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(1, 9, 3):
            if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(2, 9, 3):
            if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(1, 8, 3):
            if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(3, 10, 3):
           if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        for x in range(1, 10, 4):
           if self.posicoes_para_jogar[x] == jogador:
                pontos += 1
        if pontos == 3:
            print(f'{jogador} Wins!!')
            sys.exit(0)
        pontos = 0
        if self.posicoes_para_jogar[3] == jogador and self.posicoes_para_jogar[5] == jogador and self.posicoes_para_jogar[7] == jogador:
            print(f"{jogador} Wins!!") 
            sys.exit(0)


if __name__ == '__main__':
    play = TickTackToe()
