var dezenas = new Array()    
    dezenas[10] = "dez"    
    dezenas[20] = "vinte"
    dezenas[30] = "trinta"
    dezenas[40] = "quarenta"
    dezenas[50] = "cinquenta"
    dezenas[60] = "sessenta"
    dezenas[70] = "setenta"
    dezenas[80] = "oitenta"
    dezenas[90] = "noventa" 

unidade = function(valor_por_extenso) {
    for(var u = 0; u < unidades.length; ++u){
        if (valor_por_extenso.indexOf(unidades[u])>=0){
           return u;
        }              
    }
    return 0;
}

retira_dezena = function(valor_por_extenso){
    for(var d = 10; d < dezenas.length; d+=10 ) {        
        if (valor_por_extenso.indexOf(dezenas[d]) == 0){            
            return valor_por_extenso.substr(
                dezenas[d].length + 3
            )
       }
    }
    return valor_por_extenso;
}

dezena = function(valor_por_extenso){
    for(var d = 10; d < dezenas.length; d+=10 ) {        
        if (valor_por_extenso.indexOf(dezenas[d]) == 0){            
            valor_por_extenso = valor_por_extenso.substr(
                dezenas[d].length + 3
            )                   
            return d
       }
    }
    return 0;
}

exports.ler = function(valor_por_extenso) {
    unidades = new Array()
    unidades[0] = "zero"
    unidades[1] = "um"
    unidades[2] = "dois"
    unidades[3] = "três"
    unidades[4] = "quatro"
    unidades[5] = "cinco"
    unidades[6] = "seis"
    unidades[7] = "sete"
    unidades[8] = "oito"
    unidades[9] = "nove"

    if(valor_por_extenso == "um real"){
        return 1
    }
    
    valor = dezena(valor_por_extenso) + unidade(retira_dezena(valor_por_extenso))
    
    valor = valor / 100
    return parseFloat(valor.toFixed(2))
    
}
