import unittest
from look_and_say import *

# http://dojopuzzles.com/problemas/exibe/sequencia-look-and-say/

class LookAndSayTest(unittest.TestCase):
    
    def test_menor_numero(self):
        self.assertEquals(11, look_and_say(1))
    
    def test_segundo_menor_numero(self):
        self.assertEquals(12, look_and_say(2))
        
    def test_menor_dezena(self):
        self.assertEquals(1110, look_and_say(10))
    
    def test_com_dezena(self):
        self.assertEquals(1112, look_and_say(12))
    
    def test_com_segunda_dezena(self):
        self.assertEquals(1210, look_and_say(20))
    
    def test_com_outra_terceira_dezena(self):
        self.assertEquals(1310, look_and_say(30))
        
    def test_dezena_com_unidade_diferente_de_zero(self):    
        self.assertEquals(1915, look_and_say(95))
    
    def test_dois_algarismos_iguais(self):
        self.assertEquals(21, look_and_say(11))
    
    def test_centena_sem_repetir(self):
        self.assertEquals(111213, look_and_say(123))
    
    def test_centena_repetindo_unidade_e_dezena(self):
        self.assertEquals(1122, look_and_say(122))
    
    def test_centena_repetindo_centena_e_dezena(self):
        self.assertEquals(2112, look_and_say(112))
    
    def test_centena_repetindo_tudo(self):
        self.assertEquals(31, look_and_say(111))
                
unittest.main()
