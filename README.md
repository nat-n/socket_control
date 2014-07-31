socket_control
--------------

A tiny web app to run on a Raspberry Pi with a
[pimote](https://energenie4u.co.uk/index.php/catalogue/product/ENER002-2PI) to
control two energenie RC power sockets, from a mobile friendly web interface.

## Contents

- **index.html** provides a simple touch friendly control interface
- **pimote.py** provides an API for sending signals via GPIO pins to control
  the sockets
- **app.py** is a [bottle](http://bottlepy.org/docs/dev/index.html) web app
  which serves the index page and provides some endpoints for managing the state
  of the sockets

## Usage

Follow these instructions to get started with the energenie RC sockets and
Pimote Raspberry Pi Extension.

    sudo apt-get install python-rpi.gpio
    pip install bottle
    git clone https://github.com/nat-n/socket_control.git
    cd socket_control
    sudo ./app.py

Once the app has started, in your web browser visit port 8080 on your raspbery
pi (and *Add to home screen* if you're on IOS).

Voilà!

![screenshot](https://raw.githubusercontent.com/nat-n/socket_control/master/screenshot.PNG)
