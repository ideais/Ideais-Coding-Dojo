import unittest
from partida_tenis import partida_tenis

class partida_tenis_test(unittest.TestCase):
    
    def setUp(self):
        self.partida = partida_tenis("Jogador 1", "Jogador 2")
    
    def test_partida_tem_2_jogadores(self):        
        assert self.partida.jogador1 != None
        assert self.partida.jogador2 != None
        
    def test_nome_jogador(self):        
        assert self.partida.jogador1.nome == "Jogador 1"
        assert self.partida.jogador2.nome == "Jogador 2"
        
    def test_se_a_pontuacao_inicial_e_zero(self):        
        assert self.partida.get_placar() == [0, 0]
            
    def test_placar_vai_pra_15(self):        
        self.partida.pontuar(self.partida.jogador1)
        assert self.partida.get_placar() == [15,0] 
        
    def test_placar_vai_pra_30_pontuando_duas_vezes(self):
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        assert self.partida.get_placar() == [30,0]
        
    def test_jogador_2_pontua_e_vai_pra_15(self):
        self.partida.pontuar(self.partida.jogador2)        
        assert self.partida.get_placar() == [0,15]
        
    def test_empate(self):
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        
        assert self.partida.vencedor == None
        
    def test_dois_pontuam(self):
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador2)
        assert self.partida.get_placar() == [30,30]
    
    def test_jogador_2_vantagem(self):
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
 
        assert self.partida.jogador2.vantagem
        
    def test_jogador_troca_vantagem_apos_empate(self):        
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
        self.partida.pontuar(self.partida.jogador2)
 
        assert self.partida.jogador2.vantagem
 
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
 
        assert not self.partida.jogador2.vantagem
        assert self.partida.jogador1.vantagem
        
    def test_jogador1_ganhou(self):
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        self.partida.pontuar(self.partida.jogador1)
        
        assert self.partida.vencedor == self.partida.jogador1 
        
if __name__ == "__main__":
    unittest.main()
    