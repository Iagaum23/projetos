from model import Jogador
from random import choice
import os, sys

from model.enumTypes.dificuldadeEnum import DificuldadeEnum


class TickTackToe:
    
    def __init__(self:object) -> None:
        self.jogadores = []
        self.interface = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        self.limpar_terminal = lambda: os.system("cls" if os.name == "nt" else "clear")
        while True != False:
            resposta = int(input("Deseja jogar o jogo da velha?\n1)Sim\n0)Não (Sair)\nR:"))
            if resposta == 1:
                self.configurar_partida()
                self.iniciar_jogo()
                break
            elif resposta == 0:
                sys.exit(0)

    def configurar_partida(self):
        self.limpar_terminal()
        sinais = ['X', 'O']
        if int(input("1) Jogar contra Máquina\n2) Contra outro jogador\nR: ")) == 1:
            dificuldade_ia = 0
            while True:
                self.limpar_terminal()
                try:
                    dificuldade_ia = int(input("Escolha a dificuldade:\n1)Fácil\n2)Mediana\n3)Difícil:")) - 1
                    if dificuldade_ia < 3:
                        self.limpar_terminal()
                        break
                except Exception:
                    input("[Erro] Insira um número para conseguir escolher uma dificuldade:\nAperte Enter para continuar")
            self.jogadores.extend([Jogador(nome_jogador=input("Insira seu nome: "),
                                            sinal_utilizado=sinais.pop(sinais.index(choice(sinais)))), 
                                   Jogador(nome_jogador="Computador",
                                           sinal_utilizado=sinais.pop(sinais.index(choice(sinais))),
                                           inteligencia_artificial=True,
                                           nivel_dificuldade=dificuldade_ia)])
        else:
            for qtd_jogadores in range(2):
                self.jogadores.append(Jogador(nome_jogador=input(f"{qtd_jogadores + 1}º jogador - Insira seu nome: "),
                                              sinal_utilizado=sinais.pop(sinais.index(choice(sinais)))))
        self.limpar_terminal()
        print("---- Jogadores ----\n")
        tuple(map(lambda jogador: print(jogador.toString()), 
            self.jogadores))
        input("Aperte Enter para continuar\n")
    
    def iniciar_jogo(self: object) -> None:
        jogadas = 0
        for jogadas in range(9):
            self.montar_interface()
            jogador = self.jogadores[jogadas % 2]
            if not jogador.inteligencia_artificial:
                localizacao_jogada = int(input(f"Vez de: {jogador.nome_jogador}\nInsira a posição que deseja colocar:"))
            else:
                localizacao_jogada = jogador.armar_jogada(self.interface)
            if self.efetuar_jogada(localizacao_jogada, jogador):
                if jogador.checarPontos():
                    self.montar_interface()
                    print(f"A vitória vai para: {jogador.nome_jogador}")
                    sys.exit(0)
            else:
                jogadas -= 1
        self.montar_interface()
        print('Deu velha!')

    def montar_interface(self: object) -> None:
        self.limpar_terminal()
        for x in range(len(self.interface.keys())+1): 
            if x % 3 > 0:
                if self.interface.get(x) != '':
                    print(f'{self.interface.get(x)}|', end='')
                elif self.interface.get(x) == '': 
                    print(f'{x}|', end='') 
            elif x != 0:
                if self.interface.get(x) == '':
                    print(f'{x}|')
                elif self.interface.get(x) != '': 
                    print(f'{self.interface.get(x)}|')
        
    def efetuar_jogada(self: object, localizacao_jogada: int, jogador: Jogador) -> bool:
        if self.interface[localizacao_jogada] == '':
            self.interface[localizacao_jogada] = jogador.sinal_utilizado
            jogador.pontos.append(localizacao_jogada)
            return True
        print(f'O sinal {self.interface[localizacao_jogada]} está nessa posição, tente novamente.')
        input('Aperte Enter para continuar.')
        return False


if __name__ == '__main__':
    play = TickTackToe()
