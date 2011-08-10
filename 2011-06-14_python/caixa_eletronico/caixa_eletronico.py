def sacar(valor, notas_disponiveis = {100:0, 50:0, 20:0, 10:0}):
    retorno = []
    notas_disponiveis.each { qtd ->
     
    }
    for qtd in notas_disponiveis.items() :
        print nota        
        if nota <= valor:
            div = valor / nota
            if (div <= qtd) :                
                retorno.extend([nota] * div)
                valor = valor - (nota * div)
                notas_disponiveis[nota] -= div 
    
    return retorno    

