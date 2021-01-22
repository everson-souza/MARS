# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import logging
from maorobotica import MaoRobotica
from dicionario import *
import re
from processamento import Processamento
import unicodedata

app = Flask(__name__)

#sinal = Sinal()
processamento = Processamento()
maorobotica = MaoRobotica()

@app.route('/', methods=['GET', 'POST'])
def index():
    erro = None
    erros = []
    palavras = []

    dicLetras = []
    dicNumeros = []
    dicPalavras = []
    dicExpressoes = []

    processamento.montarDicionario(dicLetras, dicNumeros, dicPalavras, dicExpressoes)

    if request.method == 'POST':                           
        entrada = processamento.processaEntrada(request.form['palavra'])
        
        palavras = entrada.split()
        palavras = ([p.lower() for p in palavras])
        
        processamento.separarPalavras(palavras)

        erro = False
        erro = processamento.conferirDicionario(palavras, erro, erros)
        if not erro:
            for p in palavras:
                terminou = False
                terminou = maorobotica.representarSinal(dicionario[p])
                print(p)                
        
        
    return render_template('index.html', letras = dicLetras, numeros = dicNumeros, palavras = dicPalavras, expressoes = dicExpressoes, erro = erro, erros = erros)

def main():
    logging.basicConfig(level=logging.CRITICAL)
    app.logger.disable = True
    app.run(host='192.168.100.84', port = 443, debug=False)

if __name__ == "__main__":
    main()