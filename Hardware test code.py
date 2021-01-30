import RPi.GPIO as GPIO
import time 
import I2C_LCD_driver
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
pwm = GPIO.PWM(38,50)
def cfa(y):
    return y/18 + 2
pwm.start(5)
pwm.ChangeDutyCycle(cfa(89))

mylcd = I2C_LCD_driver.lcd()
GPIO.setup(36,GPIO.OUT)#reward
pwm3 = GPIO.PWM(36,50)
pwm3.start(5)
pwm3.ChangeDutyCycle(2)


GPIO.setup(40,GPIO.OUT)#lid
pwm2 = GPIO.PWM(40,50)
pwm2.start(5)
pwm2.ChangeDutyCycle(2)



def cfa(y):
    return y/18 + 2
n = 0
def openAndCloseLid():
    print("open LID")

    pwm3.ChangeDutyCycle(cfa(90))
    time.sleep(1)
    print("open LID")

    pwm3.ChangeDutyCycle(cfa(0))
# input()
# 1.7
def turnBin(x):
    for i in range(x):
        pwm.ChangeDutyCycle(cfa(80))
        time.sleep(0.7)
        pwm.ChangeDutyCycle(cfa(89))
def show(s):
    mylcd.lcd_display_string(s,1)
while(1):
    show("Place waste on lid")
    # Place waste
    x=int(input())
    show("Processing...")

    if(x<=4):
        # Turning
        turnBin(x)
        x=x-1
    print("open LID")
    openAndCloseLid()
    time.sleep(1)
    turnBin(4-x)

    pwm2.ChangeDutyCycle(cfa(90))
    time.sleep(1)
    pwm2.ChangeDutyCycle(cfa(0))
