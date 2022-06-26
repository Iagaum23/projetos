

class Jogador:
    
    def __init__(self: object, nome_jogador: str, sinal_utilizado: str) -> None:
        self.nome_jogador = nome_jogador
        self.sinal_utilizado = sinal_utilizado
        self.pontos = []
        
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
        
    def toString(self: object) -> str:
        return f"------\n|Nome do Jogador: {self.nome_jogador}\n|Sinal do jogador: {self.sinal_utilizado}\n------\n"