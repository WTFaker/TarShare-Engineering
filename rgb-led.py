import RPi.GPIO as GPIO
import sys, time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

while True:
   GPIO.output(23,1)
   time.sleep(1)
   GPIO.output(23,0)
   time.sleep(1)
   GPIO.output(24,1)
   time.sleep(1)
   GPIO.output(24,0)
   time.sleep(1)
   GPIO.output(25,1)
   time.sleep(1)
   GPIO.output(25,1)
   time.sleep(1)


