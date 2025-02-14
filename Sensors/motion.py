from machine import Pin
import utime

#IMPORTANT! HC-SR04 runs on 5V; Connect its VCC to VBUS (pin 40)
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultra(prev_distance):
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
            signaloff = utime.ticks_us()
        #print("off")
    while echo.value() == 1:
        signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        #print()
        #print(prev_distance)
        #print(distance)
        #print()
        if abs(prev_distance - distance) > 200:
            print("motion")
        prev_distance = distance
    return prev_distance

prev_distance = 0
while True:
    prev_distance = ultra(prev_distance)
    utime.sleep(1)