# Keyboard Simulator for AidaFruit 12 pad Capacitative Hat MPR121
# by Christian G Ullloa (christiangulloa@gmail.com)

# Required libraries:
	# apt-get install kbd
	# pip install pynput

# import pynput keyboard module and controller
from pynput.keyboard import Key, Controller
# import MPR121 module.
import adafruit_mpr121

# import other requiered libraries
import time
import board
import busio




# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)

# Note you can optionally change the address of the device:
#mpr121 = adafruit_mpr121.MPR121(i2c, address=0x91)

#Initiate Keyboard Controller
keyboard = Controller()

# Loop forever testing each input and printing when they're touched.
while True:
    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # Call is_touched and pass it then number of the input(numbers 1-12).  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121[i].value:
		keyboard.press(i+1)
		keyboard.release(i+1)
		time.sleep(0.25)  # Small delay to keep from spamming output messages.
