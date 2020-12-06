from flask import Flask, render_template, request
import logging
from signal import Sinal
from dictionary import *

app = Flask(__name__)

nome = Sinal()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':                   
        
        #nome.rola(request.form['palavra'])
        nome.rola(words["rola"])
    return render_template ('index.html')

def main():
    logging.basicConfig(level=logging.CRITICAL)
    app.logger.disable = True
    app.run(host='192.168.100.84', port = 443, debug=False)

if __name__ == "__main__":
    main()