# Load libraries
from machine import Pin
import time
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)
n = 0
 
print('Starting up the PIR Module')
time.sleep(1)
print('Ready')
 
while True:
    detected = pir.value() 
    if detected == 1:
        n = n+1
        print('Motion Detected ',n)
        time.sleep(6)
    time.sleep(1) #is activated for 7 seconds
    detected = 0