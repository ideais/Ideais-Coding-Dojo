CENTENA = -3
DEZENA = -2
UNIDADE = -1
  
def look_and_say(num):
    
    if num < 10:
        return int("1" + str(num))
        
    if num < 100:
        if dezena_igual_unidade(num):
            return int("2" + str(num)[DEZENA])
        else:
            return int("1" + str(num)[DEZENA] + "1" + str(num)[UNIDADE])

    if num < 1000:
        if centena_igual_dezena(num):
            return int("2" + str(num)[CENTENA] +
                       "1" + str(num)[UNIDADE])
                       
        if dezena_igual_unidade(num):
            return int("1" + str(num)[CENTENA] +
                       "2" + str(num)[UNIDADE])
                       
        return int("1" + str(num)[CENTENA] +
                   "1" + str(num)[DEZENA] +
                   "1" + str(num)[UNIDADE])
    
   
    
    
def centena_igual_dezena(num):
    return str(num)[DEZENA] == str(num)[CENTENA]

def dezena_igual_unidade(num):
    return str(num)[DEZENA] == str(num)[UNIDADE]
