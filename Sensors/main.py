from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
from EPD_2in9_B_V4_Portrait import EPD_2in9_B_V4_Portrait
import bme280 

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)    #initializing the I2C method 

#captures the temperature and displays the data on the e-paper
def show_temperature():
    bme = bme280.BME280(i2c=i2c)
    epd = EPD_2in9_B_V4_Portrait()
    epd.Clear()
    
    text = "Temp: " + bme.values[0]
    print(text)
    epd.imageblack.fill(0xff)
    epd.imageblack.text(text, 0, 10, 0x00)
    epd.display()
    epd.delay_ms(20000)
    
    print("sleep")
    epd.sleep()
    

show_temperature()