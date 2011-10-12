var permArr = [], letrasUsadas = []

function removeLixo(array, tamanho) {
  var arrayLimpo = []
  for(indice in array) {
    if(array[indice].length == tamanho) arrayLimpo.push(array[indice])
  }

  return arrayLimpo
}

function permutacoes(palavra) {
  var letras = palavra.split('')
  var tamanho = letras.length
  var ch = ''
  for (var letra = 0; letra < (letras.length); letra++) {
    ch = letras.splice(letra, 1)
    letrasUsadas.push(ch)
    if (letras.length == 0) permArr[permArr.length] = letrasUsadas.join('')
    permutacoes(letras.join(''))
    letras.splice(letra, 0, ch)
    letrasUsadas.pop()
  }

  return permArr
}

exports.anagrama = function( palavra ) {
  var anagr = permutacoes(palavra)
  return removeLixo(anagr, palavra.length).sort()
}

