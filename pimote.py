import RPi.GPIO as GPIO
import time


def init():
    # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output(22, False)

    # Set the modulator to ASK for On Off Keying
    # by setting MODSEL pin lo
    GPIO.output(18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(13, False)


def term():
    GPIO.cleanup()


def one_on():
    try:
        print "sending code 1111 socket 1 on"
        GPIO.output(11, True)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, True)
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


def one_off():
    try:
        print "sending code 0111 Socket 1 off"
        GPIO.output(11, True)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, False)
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


def two_on():
    try:
        print "sending code 1110 socket 2 on"
        GPIO.output(11, False)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, True)
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


def two_off():
    try:
        print "sending code 0110 socket 2 off"
        GPIO.output(11, False)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, False)
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


def both_on():
    try:
        print "sending code 1011 ALL on"
        GPIO.output(11, True)
        GPIO.output(15, True)
        GPIO.output(16, False)
        GPIO.output(13, True)
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


def both_off():
    try:
        print "sending code 0011 All off"
        GPIO.output(11, True)
        GPIO.output(15, True)
        GPIO.output(16, False)
        GPIO.output(13, False)
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
