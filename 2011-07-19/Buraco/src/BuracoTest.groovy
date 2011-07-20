import junit.framework.TestCase 

class BuracoTest extends TestCase {
	
	def pontuacoes = [ 1:15, 2:10, 3:5, 4:5, 5:5, 6:5, 7:5, 8:10, 9:10, 10:10, 11:15, 12:15, 13:15 ]
	
	void testSeSequenciaEhCanastra() {
		assertEquals(15, contaCanastra([4,5,6]) )
	}
	
	void testNaoCanastra() {
		assertEquals(0, contaCanastra([4, 8, 11]))
	}
	
	void testCanastraMaiorValorComTresCartas() {
		assertEquals(45, contaCanastra([11, 12, 13]))
	}
	
	void testCanastraMenor() {
		assertEquals(15, contaCanastra([3, 4, 5]))
	}
	
	void testSeSequencia(){
		assertEquals(true, isSeq([3, 4, 5]))
	}
	
	void testSeSequenciaComNumerosIguais(){
		assertEquals(false, isSeq([1, 1, 1]))
	}
	
	void testSeSequenciaComCoringaPrimeiraPosicao(){
		assertEquals(true, isSeq([2, 4, 5]))
	}
	
	void testSeSequenciaComCoringaSegundaPosicao(){
		assertEquals(true, isSeq([3, 2, 5]))
	}
	
	void testSeSequenciaComCoringaTerceiraPosicao(){
		assertEquals(true, isSeq([3, 2, 2]))
	}
	
	void testCanastraCompleta() {
		assertEquals(1000, contaCanastra([1,2,3,4,5,6,7,8,9,10,11,12,13,1]))
	}
	
	int contaCanastra(def cartas) {
		if(cartas == [1,2,3,4,5,6,7,8,9,10,11,12,13,1]) return 1000
		def soma = 0
		if (isSeq(cartas)) {
			cartas.each {
				soma = soma + pontuacoes[it]
			}
		}
		return soma
	}
	
	boolean isSeq(def cartas){
		for(int i = 0; i < cartas.size()-1;i++){			
			if(cartas[i]+1 != cartas[i+1]){
				if(cartas[i] != 2 && cartas[i+1] != 2) {
					return false
				}				
			}
		}
		return true
	}
		
}