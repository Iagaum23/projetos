from .enumTypes.dificuldadeEnum import DificuldadeEnum
from typing import Literal


class Jogador:
    
    def __init__(self: object, nome_jogador: str, sinal_utilizado: Literal['X', '0'],
                 inteligencia_artificial: bool = False, nivel_dificuldade: DificuldadeEnum = DificuldadeEnum.jogador) -> None:
        self.nome_jogador: str = nome_jogador
        self.sinal_utilizado: Literal['X', '0'] = sinal_utilizado
        self.pontos: list = []
        self.inteligencia_artificial: bool = inteligencia_artificial
        self.nivel_dificuldade: DificuldadeEnum = nivel_dificuldade
        
    def checarPontos(self: object) -> bool:
        pontos_p_vitoria = 0
        condicao_para_vitoria = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                                 (1, 4, 7), (2, 5, 8), (3, 6, 9),
                                 (1, 5, 9), (3, 5, 7))
        for pontos_condicionais in condicao_para_vitoria:
            for pontos in self.pontos:
                if pontos in pontos_condicionais:
                    pontos_p_vitoria += 1
            if pontos_p_vitoria == 3:
                break
            pontos_p_vitoria = 0
        if pontos_p_vitoria == 3:
            return True
        return False

    def armar_jogada(self:object, jogadas: dict) -> int:
        if self.nivel_dificuldade == DificuldadeEnum.facil.value:
            localizacao_jogada_oponente = tuple(filter(lambda jogada: jogada[1] != self.sinal_utilizado and jogada[1] != '' , jogadas.items()))
            menor_jogada = min(localizacao_jogada_oponente)[0]
            maior_jogada = max(localizacao_jogada_oponente)[0]
            # jogadas_futuras = tuple(jogada if menor_jogada != maior_jogada else maior_jogada for jogada in range(menor_jogada, maior_jogada + 1))
            condicao_para_vitoria = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                                (1, 4, 7), (2, 5, 8), (3, 6, 9),
                                (1, 5, 9), (3, 5, 7))
            possiveis_jogadas = []
            for pontos_condicionais in condicao_para_vitoria:
                for pontos in localizacao_jogada_oponente:
                    if pontos in pontos_condicionais:
                        pontos_p_vitoria += 1
                    if pontos_p_vitoria >= 2:
                        possiveis_jogadas.append(pontos)
                pontos_p_vitoria = 0
            if len(possiveis_jogadas) > 1:
                pass
            else:
                pass
                    
        elif self.nivel_dificuldade == DificuldadeEnum.mediano.value:
            pass
        else:
            pass
    
    def toString(self: object) -> str:
        return f"------\n|Nome do Jogador: {self.nome_jogador}\n|Sinal do jogador: {self.sinal_utilizado}\n------\n"
    