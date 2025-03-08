from time import sleep
from picodfplayer import DFPlayer

# Initialization DFPlayer (UART, TX pin, RX pin, busy pin)
player = DFPlayer(0, 16, 17, 18)
sleep(1)
player.setVolume(15) # Set volume: 0 to 30

# Title counter
count = 1

print('Play:', count)
# Directory: 01 / File: 001 (/01/001)
player.playTrack(1,1)

# Repetition: Endless loop
while True:
    sleep(5)
    # When the title is finished
    count += 1
    if count < 5:
        print('Next title:', count)
        player.nextTrack()
    else:
        player.pause()