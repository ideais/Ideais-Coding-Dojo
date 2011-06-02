
class Amigo {	
	def id
	def coordenada
	
	def Amigo(id, x , y) {
		this.id = id
		coordenada = new Coordenada(x:x, y:y)
	}
	
	def comparaDistancia(amigo){
		((coordenada.x- amigo.coordenada.x)**2 + (coordenada.y - amigo.coordenada.y)**2)**0.5
	}
	
	def encontrarAmigosProximos(amigos){		
		def res = amigos.findAll{
			it.id != this.id
		}.collect{ amigo ->
			[id:amigo.id, dist: comparaDistancia(amigo)]
		}
		
		res.sort{
			it.dist
		}
		
		[ res[0].id, res[1].id ,res[2].id ].sort()
	}
}
