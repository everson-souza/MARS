from flask import Flask, render_template, request
import logging
from signal import Sinal
from dictionary import *

app = Flask(__name__)

sinal = Sinal()

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':                   
        
        #sinal.rola(request.form['palavra'])
        error = True
        sinal.rola(words["rola"])
    return render_template('index.html', error = error, words = list(words.keys()))

def main():
    logging.basicConfig(level=logging.CRITICAL)
    app.logger.disable = True
    app.run(host='192.168.100.84', port = 443, debug=False)

if __name__ == "__main__":
    main()