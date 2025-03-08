from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
from EPD_2in9_B_V4_Portrait import EPD_2in9_B_V4_Portrait
import bme280 

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)    #initializing the I2C method
player=DFPlayer(0, 16, 17, 18) #player for the speakers
keypad = Keypad()
bme = bme280.BME280(i2c=i2c)
epd = EPD_2in9_B_V4_Portrait()

#captures the temperature and displays the data on the e-paper
def printInDisplay(text):
    epd.Clear()
    
    epd.imageblack.fill(0xff)
    epd.imageblack.text(text, 0, 10, 0x00)
    epd.display()
    epd.delay_ms(20000)
    
    print("sleep")
    epd.sleep()
    
def play_track(track_num):
    player.playTrack(key,1)
    sleep(5)
    player.pause()
    
def activate_client():
    text = "Temp: " + bme.values[0]
    print(text)
    printInDisplay(text)
    
def activate_visitor(key):    
    play_track(key)
    
def main():
    while True:
        detected = pir.value() 
        if detected == 1:
            print('Motion Detected ',n)
            activate_client()
        key = keypad.get_key()
        if key != None:
            activate_visitor(key)
            key = None
        time.sleep(1) #is activated for 7 seconds
        detected = 0
        