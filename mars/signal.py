import RPi.GPIO as GPIO
import threading
import time
from dictionary import *

GPIO.setmode(GPIO.BCM)

finger1 = 5
finger2 = 6
finger3 = 13
finger4 = 19
finger5 = 26

# Classe onde sera implementado a movimentacao dos motores
class Sinal:
    
    def __init__(self):
        self.pwm = [0]*5
        self.handStart()
    
    def signal(self, word):
        self.openHand()
        time.sleep(2)
        
        for angles in word:
            print("Angles:", angles, type(angles))
            f1 = threading.Thread(target=self.fingerMovement, args=(angles[0], 0))
            f1.start()

            f2 = threading.Thread(target=self.fingerMovement, args=(angles[1], 1))
            f2.start()

            f3 = threading.Thread(target=self.fingerMovement, args=(angles[2], 2))
            f3.start()

            f4 = threading.Thread(target=self.fingerMovement, args=(angles[3], 3))
            f4.start()

            f5 = threading.Thread(target=self.fingerMovement, args=(angles[4], 4))
            f5.start()

            time.sleep(angles[5])

    def closeHand(self):
        f1 = threading.Thread(target=self.fingerMovement, args=(0, 0))
        f1.start()

        f2 = threading.Thread(target=self.fingerMovement, args=(0, 1))
        f2.start()

        f3 = threading.Thread(target=self.fingerMovement, args=(0, 2))
        f3.start()

        f4 = threading.Thread(target=self.fingerMovement, args=(0, 3))
        f4.start()

        f5 = threading.Thread(target=self.fingerMovement, args=(0, 4))
        f5.start()

    def openHand(self):
        f1 = threading.Thread(target=self.fingerMovement, args=(220, 0))
        f1.start()

        f2 = threading.Thread(target=self.fingerMovement, args=(180, 1))
        f2.start()

        f3 = threading.Thread(target=self.fingerMovement, args=(180, 2))
        f3.start()

        f4 = threading.Thread(target=self.fingerMovement, args=(200, 3))
        f4.start()

        f5 = threading.Thread(target=self.fingerMovement, args=(180, 4))
        f5.start()

    def fingerMovement(self, angle, finger):
        #print("Angulo: ", angle, " Dedo: ", finger)
        duty = float(angle) / 10.0 + 2.5
        self.pwm[finger].ChangeDutyCycle(duty)

    def handStart(self):
        GPIO.setup(finger1, GPIO.OUT)
        self.pwm[0] = GPIO.PWM(finger1, 100)
        self.pwm[0].start(5)

        GPIO.setup(finger2, GPIO.OUT)
        self.pwm[1] = GPIO.PWM(finger2, 100)
        self.pwm[1].start(5)

        GPIO.setup(finger3, GPIO.OUT)
        self.pwm[2] = GPIO.PWM(finger3, 100)
        self.pwm[2].start(5)

        GPIO.setup(finger4, GPIO.OUT)
        self.pwm[3] = GPIO.PWM(finger4, 100)
        self.pwm[3].start(5)

        GPIO.setup(finger5, GPIO.OUT)
        self.pwm[4] = GPIO.PWM(finger5, 100)
        self.pwm[4].start(5)

def main():
    mao = Sinal()
    print("Iniciando a MAR2S!!!")
    mao.openHand()

    while True:
        op = input("1- Digitar algo\n2- Entrada manual dos angulos\n")
        opcao = int(op)
        if(opcao == 1):
            palavra = input("Digite algo: ")
            print("Palavra:", palavra, type(palavra))
            mao.signal(dictionary[palavra])
            continue
        if(opcao == 2):
            print("Digite o angulo: ")
            angulo = input();
            print("Digite o dedo: ")
            dedo = input();
            mao.fingerMovement(int(angulo), int(dedo))
            continue

if __name__ == "__main__":
	main()