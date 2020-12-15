import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)

finger1 = 5
finger2 = 6
finger3 = 13
finger4 = 19
finger5 = 26

# Classe onde será implementado a movimentação dos motores
class Sinal:
    
    def __init__(self):
        self.pwm = []
        self.handStart()
        print ('lalala')
    
    def signal(self, word):
        for angles in word:
            f1 = threading.Thread(target=fingerMovement, args=(angles[0], 0))
            f1.start()

            f2 = threading.Thread(target=fingerMovement, args=(angles[1], 1))
            f2.start()

            f3 = threading.Thread(target=fingerMovement, args=(angles[2], 2))
            f3.start()

            f4 = threading.Thread(target=fingerMovement, args=(angles[3], 3))
            f4.start()

            f5 = threading.Thread(target=fingerMovement, args=(angles[4], 4))
            f5.start()

            sleep(angles[5])


    def fingerMovement(self, angle, finger):
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
