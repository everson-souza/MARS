import RPi.GPIO as GPIO
import threading
import time
from dicionario import *

GPIO.setmode(GPIO.BCM)

dedo1 = 5
dedo2 = 6
dedo3 = 13
dedo4 = 19
dedo5 = 26

# Classe onde sera implementado a movimentacao dos motores
class MaoRobotica:
    
    def __init__(self):
        self.pwmServos = [0]*5
        self.iniciarMao()
    
    def representarSinal(self, parametrosSinal):
        self.abrirMao()
        time.sleep(1)
        
        for parametros in parametrosSinal:
            # print("Angles:", angles, type(angles))
            d1 = threading.Thread(target=self.movimentoDedo, args=(parametros[0], 0))
            d1.start()

            d2 = threading.Thread(target=self.movimentoDedo, args=(parametros[1], 1))
            d2.start()

            d3 = threading.Thread(target=self.movimentoDedo, args=(parametros[2], 2))
            d3.start()

            d4 = threading.Thread(target=self.movimentoDedo, args=(parametros[3], 3))
            d4.start()

            d5 = threading.Thread(target=self.movimentoDedo, args=(parametros[4], 4))
            d5.start()

            time.sleep(parametros[5])

        time.sleep(2)
        return True

    def fecharMao(self):
        d1 = threading.Thread(target=self.movimentoDedo, args=(0, 0))
        d1.start()

        d2 = threading.Thread(target=self.movimentoDedo, args=(0, 1))
        d2.start()

        d3 = threading.Thread(target=self.movimentoDedo, args=(0, 2))
        d3.start()

        d4 = threading.Thread(target=self.movimentoDedo, args=(0, 3))
        d4.start()

        d5 = threading.Thread(target=self.movimentoDedo, args=(0, 4))
        d5.start()

    def abrirMao(self):
        d1 = threading.Thread(target=self.movimentoDedo, args=(220, 0))
        d1.start()

        d2 = threading.Thread(target=self.movimentoDedo, args=(180, 1))
        d2.start()

        d3 = threading.Thread(target=self.movimentoDedo, args=(180, 2))
        d3.start()

        d4 = threading.Thread(target=self.movimentoDedo, args=(200, 3))
        d4.start()

        d5 = threading.Thread(target=self.movimentoDedo, args=(180, 4))
        d5.start()

    def movimentoDedo(self, angulo, dedo):
        #print("Angulo: ", angle, " Dedo: ", finger)
        duty = float(angulo) / 10.0 + 2.5
        self.pwmServos[dedo].ChangeDutyCycle(duty)

    def iniciarMao(self):
        GPIO.setup(dedo1, GPIO.OUT)
        self.pwmServos[0] = GPIO.PWM(dedo1, 100)
        self.pwmServos[0].start(5)

        GPIO.setup(dedo2, GPIO.OUT)
        self.pwmServos[1] = GPIO.PWM(dedo2, 100)
        self.pwmServos[1].start(5)

        GPIO.setup(dedo3, GPIO.OUT)
        self.pwmServos[2] = GPIO.PWM(dedo3, 100)
        self.pwmServos[2].start(5)

        GPIO.setup(dedo4, GPIO.OUT)
        self.pwmServos[3] = GPIO.PWM(dedo4, 100)
        self.pwmServos[3].start(5)

        GPIO.setup(dedo5, GPIO.OUT)
        self.pwmServos[4] = GPIO.PWM(dedo5, 100)
        self.pwmServos[4].start(5)

def main():
    mao = MaoRobotica()
    print("Iniciando a MAR2S!!!")
    mao.abrirMao()

    while True:
        op = input("1- Digitar algo\n2- Entrada manual dos angulos\n")
        opcao = int(op)
        if(opcao == 1):
            palavra = input("Digite algo: ")
            print("Palavra:", palavra, type(palavra))
            mao.representarSinal(dicionario[palavra])
            continue
        if(opcao == 2):
            print("Digite o angulo: ")
            angulo = input();
            print("Digite o dedo: ")
            dedo = input();
            mao.movimentoDedo(int(angulo), int(dedo))
            continue

if __name__ == "__main__":
	main()