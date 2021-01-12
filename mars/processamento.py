# -*- coding: utf-8 -*-

import re
from dicionario import *

# Classe onde será implementado a movimentação dos motores
class Processamento:
    
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

    def conferirDicionario(self, palavras, erro, erros):    
        for p in palavras:
            if p not in list(dicionario.keys()):
                erro = True
                erros.append(p)
        return erro