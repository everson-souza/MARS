import re
from dictionary import *

# Classe onde será implementado a movimentação dos motores
class Processing:
    
    def __init__(self):        
        print ('lalala')
    
    def separarPalavras(self, palavras):             
        for i in range(len(palavras)):               
            if palavras[i].startswith('[') and palavras[i].endswith(']'):                
                palavras[i] = re.sub(r"[\[\]]+", '', palavras[i])
                j = 1
                for letra in palavras[i]:
                    palavras.insert(i+j, letra)
                    j+=1
                palavras.remove(palavras[i])

    def conferirDicionario(self, palavras, error, erros):    
        for p in palavras:
            if p not in list(dictionary.keys()):
                error = True
                erros.append(p)
        return error