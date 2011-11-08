from jogador import jogador

class partida_tenis:
    pontos = {0: 0, 1:15, 2: 30, 3: 40}    
    
    def __init__(self, nomeJogador1, nomeJogador2):
        self.jogador1 = jogador(nomeJogador1)
        self.jogador2 = jogador(nomeJogador2)
        self.placar = {nomeJogador1: 0, nomeJogador2: 0}
        self.vencedor = None
        
    def pontuar(self, jogador):
        if self.get_placar() == [40, 40]:
            self.set_vantagem(jogador)
        else:
            if self.get_pontos(jogador.nome) == 40 or jogador.vantagem:
                self.vencedor = jogador
            else:
                self.placar[jogador.nome] +=1
            
    def get_placar(self):
        return [self.get_pontos(self.jogador1.nome), self.get_pontos(self.jogador2.nome)]
    
    def get_pontos(self, key): 
        return self.pontos.get(self.placar.get(key))

    def set_vantagem(self, jogador):
        self.jogador1.vantagem = False
        self.jogador2.vantagem = False
        jogador.vantagem = True