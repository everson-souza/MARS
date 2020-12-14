import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)

finger1 = 16
finger2 = 18
finger3 = 13
finger4 = 19
finger5 = 22

# Classe onde será implementado a movimentação dos motores
class Sinal:
    
    def __init__(self):

        print ('lalala')
    
    def signal(self, word):
        for angles in word:
            f1 = threading.Thread(target=fingerMovement, args=(angles[0], finger1))
            f1.start()

            f2 = threading.Thread(target=fingerMovement, args=(angles[1], finger2))
            f2.start()

            f3 = threading.Thread(target=fingerMovement, args=(angles[2], finger3))
            f3.start()

            f4 = threading.Thread(target=fingerMovement, args=(angles[3], finger4))
            f4.start()

            f5 = threading.Thread(target=fingerMovement, args=(angles[4], finger5))
            f5.start()


    def fingerMovement(self, angle, pin):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

    def handStart(self):
        GPIO.setup(finger1, GPIO.OUT)
        pwm = GPIO.PWM(finger1, 100)
        pwm.start(5)

        GPIO.setup(finger2, GPIO.OUT)
        pwm = GPIO.PWM(finger2, 100)
        pwm.start(5)

        GPIO.setup(finger3, GPIO.OUT)
        pwm = GPIO.PWM(finger3, 100)
        pwm.start(5)

        GPIO.setup(finger4, GPIO.OUT)
        pwm = GPIO.PWM(finger4, 100)
        pwm.start(5)

        GPIO.setup(finger5, GPIO.OUT)
        pwm = GPIO.PWM(finger5, 100)
        pwm.start(5)
