# Load libraries
from machine import Pin
from time import sleep

# Initialization of the PIR module
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)


# Repetition (endless loop)
while True:
    # Wait 1 second
    sleep(1)
    # Read PIR sensor state
    pir_value = pir.value()
    # Output value
    print(pir_value)