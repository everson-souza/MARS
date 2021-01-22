# -*- coding: utf-8 -*-

import re
from dicionario import *
import unicodedata

# Classe onde será implementado a movimentação dos motores
class Processamento:
    
    def __init__(self):        
        print ('lalala')
    
    def montarDicionario(self, letras, numeros, palavras, expressoes):
        for key in dicionario:        
            if (dicionario[key][0] == 0):
                letras.append(key)
            elif (dicionario[key][0] == 1):
                numeros.append(key)
            elif (dicionario[key][0] == 2):
                palavras.append(key)
            elif (dicionario[key][0] == 3):
                expressoes.append(key)
        letras.sort()
        numeros.sort()
        palavras.sort()
        expressoes.sort()

    def processaEntrada(self, entrada):            
        #remove acentuação
        texto = ''.join(ch for ch in unicodedata.normalize('NFKD', entrada) 
                            if not unicodedata.combining(ch))
        
        #remove pontuação
        texto = re.sub(r'[^\w\s^-^\[^\]]','', texto)
        print (texto)
        return texto

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