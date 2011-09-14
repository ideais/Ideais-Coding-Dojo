exports.calcula = function(numero) {
    if(numero <= 2) {
        return numero;        
    }
    
    return numero * exports.calcula( numero -1 )
    
}
