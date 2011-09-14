class Palavras

    def is_primo(palavra)
        true
    end    
    
    private
    
    def valor_palavra(palavra) 
        valor = 0
        palavra.each_char do |letra|
            valor += valor_letra(letra)
        end
    end
    
    def valor_letra(letra_recebida)
        ('a'..'z').each_with_index do |letra, index|
            if (letra ==  letra_recebida)
                index + 1
            end
        end
        ('A'..'Z').each_with_index do |letra, index|
            if(letra ==  letra_recebida)
                index + 27
            end
        end
    end
    
    
end

class Fixnum
    
    def is_prime?
       
       (2...self).each do |number| 
          if self % number == 0             
              true         
          end
       end
       
    end
end
