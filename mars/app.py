# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import logging
from maorobotica import MaoRobotica
from dicionario import *
import re
from processamento import Processamento

app = Flask(__name__)

#sinal = Sinal()
processamento = Processamento()
maorobotica = MaoRobotica()

@app.route('/', methods=['GET', 'POST'])
def index():
    erro = None
    erros = []
    words = []
    if request.method == 'POST':                           
        palavras = re.sub(r"[^a-zA-ZzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \[\]]+", ' ', request.form['palavra']).split()
        palavras = ([p.lower() for p in palavras])
        
        processamento.separarPalavras(palavras)

        erro = False
        erro = processamento.conferirDicionario(palavras, erro, erros)
        if not erro:
            for p in palavras:
                terminou = False
                terminou = maorobotica.representarSinal(dicionario[p])
                print(p)
                print(terminou)
        
        
    return render_template('index.html', dicionario = list(dicionario.keys()), erro = erro, erros = erros)

def main():
    logging.basicConfig(level=logging.CRITICAL)
    app.logger.disable = True
    app.run(host='192.168.100.51', port = 8080, debug=False)

if __name__ == "__main__":
    main()