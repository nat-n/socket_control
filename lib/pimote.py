import RPi.GPIO as GPIO
import time
from sys import stdout
from datetime import datetime, timedelta
import pytz

"""
This module provides a minimalistic abstraction around the GPIO control
interface for the pimote.
"""

CODES = {
    '1-on':    [1, 1, 1, 1],  # 7
    '1-off':   [0, 1, 1, 1],
    '2-on':    [1, 1, 1, 0],  # 6
    '2-off':   [0, 1, 1, 0],
    '3-on':    [1, 1, 0, 1],  # 5
    '3-off':   [0, 1, 0, 1],
    '4-on':    [1, 1, 0, 0],  # 4
    '4-off':   [0, 1, 0, 0],
    'all-on':  [1, 0, 1, 1],  # 3
    'all-off': [0, 0, 1, 1],
}


def init():
    # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)
    # # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    # # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)
    # # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)
    # # Disable the modulator by setting CE pin lo
    GPIO.output(22, False)
    # # Set the modulator to ASK for On Off Keying
    # # by setting MODSEL pin lo
    GPIO.output(18, False)
    # # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(13, False)
    pass


def term():
    GPIO.cleanup()
    pass


def switch(code):
    a, b, c, d = [bool(c) for c in CODES[code]]
    t = datetime.utcnow().replace(tzinfo = pytz.utc)
    stdout.write('%s : Sending code %d%d%d%d\n' %
                 (t.isoformat(), int(a), int(b), int(c), int(d)))
    try:
        GPIO.output(11, d)
        GPIO.output(15, c)
        GPIO.output(16, b)
        GPIO.output(13, a)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        return True
    except:
        return False
