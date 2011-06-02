import static org.junit.Assert.*;
import junit.framework.TestCase 


class MundoPequenoTests extends TestCase {

	def amigos = [
		new Amigo(1,2,4),
		new Amigo(2,3,6),
		new Amigo(3,4,4),
		new Amigo(4,5,5),
		new Amigo(5,7,6)
	]
	
	
	//alt + shit + a
	void testBusca3AmigosProximosAoAmigo5(){		
		def atual = amigos[4]
		def res = atual.encontrarAmigosProximos(amigos)
		
		assert([2,3,4]==res)
	}
	
	void testBusca3AmigosProximosAoAmigo1() {
		def atual = amigos[0]
		def res = atual.encontrarAmigosProximos(amigos)
		
		assert([2,3,4]==res)
	}
	
	void testBusca3AmigosProximosAoAmigo2() {
		def atual = amigos[1]
		def res = atual.encontrarAmigosProximos(amigos)
		
		assert([1,3,4]==res)
	}
	
	void testBusca3AmigosProximosAoAmigo3() {
		def atual = amigos[2]
		def res = atual.encontrarAmigosProximos(amigos)
		
		assert([1,2,4]==res)
	}
	
	void testBusca3AmigosProximosAoAmigo4() {
		def atual = amigos[3]
		def res = atual.encontrarAmigosProximos(amigos)
		
		assert([2,3,5]==res)
	}
	
	void testComparaDuasDistancias() {
		def atual = amigos[1]
		def res = atual.comparaDistancia(amigos[1]);
		assert(0==res)
	}
	
}
