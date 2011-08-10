class Intervalos
    
    def get_intervalo(lista_numeros)
        lista_numeros.sort!
        
        if lista_numeros.size <= 1
            return [lista_numeros]
        end
        
        if is_intervalo? lista_numeros
            return [ [lista_numeros.first, lista_numeros.last] ]
        else
            return monta_sub_intervalo lista_numeros
        end
        
        #[lista_numeros]        
    end
    
    private
    
        def is_intervalo?(lista_numeros)
            if lista_numeros.size <= 1
                return false
            end
            
            if lista_numeros[0] + (lista_numeros.size - 1) == 
            lista_numeros[lista_numeros.size-1]
                true
            end
        end
        
        def monta_sub_intervalo(lista_numeros)
            listas = []
            interval = []
            lista_numeros.each_with_index do | item, index |
                if index == (lista_numeros.size -1)
                    if is_intervalo? [interval.last, item]
                        interval.push item
                    else
                        listas << [interval.first,interval.last]
                        interval = [item]                        
                    end
                    
                    listas << [interval.first,interval.last]
                    
                elsi f item != (lista_numeros[index + 1] - 1)
                    interval.push item
                    listas << [interval.first, interval.last]
                    interval = []
                else
                   interval.push item 
                end                
            end
            
            listas
        end
end
