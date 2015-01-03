socket_control
--------------

A tiny web app to run on a Raspberry Pi with a
[pimote](https://energenie4u.co.uk/index.php/catalogue/product/ENER002-2PI) to
seperately control up to four energenie4u RC power sockets, from a mobile friendly
web interface.

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

    # fetch dependencies
    sudo apt-get install python-rpi.gpio
    sudo apt-get install python-pip
    pip install bottle

    # get socket_control
    git clone https://github.com/nat-n/socket_control.git
    cd socket_control

    # run it (as root because GPIO requires it)
    sudo ./app.py

## Crontab

 Create simple crontab jobs to change socket status i.e
 - **40 15 * * * wget http://<ip>/1/1 --delete-after #turn socket one on 3.40**
 - **40 15 * * * wget http://<ip>/1/0 --delete-after #turn socket one off 3.40**

Once the app has started, open your web browser and visit port 8080 at your
raspbery pi's IP address (and *Add to home screen* if you're on IOS).

Voilà!

![screenshot](https://raw.githubusercontent.com/nat-n/socket_control/master/screenshot.png)
