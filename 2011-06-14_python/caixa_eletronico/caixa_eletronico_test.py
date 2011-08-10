import unittest
from caixa_eletronico import sacar

class CaixaEletronicoTest(unittest.TestCase):
    
    def test_sacar_10_reais_sem_nota_disponivel(self):
        self.assertEquals([], sacar(10))
        
    def test_sacar_30_reais_sem_nota_disponivel(self):
        self.assertEquals([], sacar(30))
        
    def test_sacar_20_reais_tendo_apenas_nota_20_disponivel(self):
        self.assertEquals([20], sacar(20,{20:1}))
    
    def test_sacar_20_reais_tendo_apenas_nota_10_disponivel(self):
        self.assertEquals([10,10], sacar(20,{10:2}))
        
    def test_sacar_50_reais_tendo_apenas_nota_10_e_20_disponivel(self):
        self.assertEquals([20, 20, 10], sacar(50,{20:2, 10:2}))
        
        
        
        
        
unittest.main()
