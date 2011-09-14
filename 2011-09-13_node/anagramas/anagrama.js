var fat = require('./fatorial');

function randOrd(){
    return (Math.round(Math.random())-0.5); 
}

function contem(elemento, vetor) {
  for(i in vetor) {
    if(elemento == vetor[i])
        return true
  }
  
  return false
}

function embaralhaPalavra(palavra) {
    return palavra.split('').sort(randOrd).join('')
}

exports.anagrama = function( palavra ) {  
    
    var max_anagramas = fat.calcula(palavra.length);
    var anagramas = [];
    while (anagramas.length < max_anagramas){
        palavra = embaralhaPalavra(palavra)
        if (! contem(palavra, anagramas)){
            anagramas.push(palavra)
        }    
    }
    return anagramas.sort()
}
