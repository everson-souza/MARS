from flask import Flask, render_template, request
import logging
#from signal import Sinal
from dictionary import *
import re
from processing import Processing

app = Flask(__name__)

#sinal = Sinal()
processing = Processing()

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    erros = []
    words = []
    if request.method == 'POST':                           
        palavras = re.sub(r"[^a-zA-ZzáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ \[\]]+", ' ', request.form['palavra']).split()

        words = palavras

        processing.separarPalavras(palavras)
        
        error = False
        error = processing.conferirDicionario(palavras, error, erros)
        print (error)
        
        
    return render_template('index.html', dictionary = list(dictionary.keys()), error = error, erros = erros)

def main():
    logging.basicConfig(level=logging.CRITICAL)
    app.logger.disable = True
    app.run(host='192.168.100.84', port = 443, debug=False)

if __name__ == "__main__":
    main()