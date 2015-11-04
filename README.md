socket_control
--------------

A tiny web app to run on a Raspberry Pi with a
[pimote](https://energenie4u.co.uk/index.php/catalogue/product/ENER002-2PI) to
seperately control up to four energenie4u RC power sockets, from a mobile
friendly web interface, or using a google calendar (or any other ics feed) to
schedule sockets.

## Usage

Follow these instructions to get started with the energenie RC sockets and
Pimote Raspberry Pi Extension.

    # fetch dependencies
    sudo apt-get install python-rpi.gpio
    sudo apt-get install python-pip
    pip install bottle pytz ics

    # get socket_control
    git clone https://github.com/nat-n/socket_control.git
    cd socket_control

    # run it (as root because GPIO requires it)
    sudo ./app.py

### Calendar based scheduling

To schedule events via a calendar then set `ICAL_URL` in config.py to the
private ICAL URL (should end with .ics) for your calendar and and create events
in that calendar named after the number of the socket they should schedule.

### Web/Mobile frontend

Once the app has started, open your web browser and visit port 8080 at your
raspbery pi's IP address (and *Add to home screen* if you're on IOS). Labels
displayed in the web front end can be edited in **config.py**.

### From another app

You can also access the API directly from the command line in a script or
crontab task using curl like:

    curl http://<socket_control_host>/1/1  # turn socket one on
    curl http://<socket_control_host>/1/0  # turn socket one off

Sample Screenshot of the

![screenshot](https://raw.githubusercontent.com/nat-n/socket_control/master/screenshot.png)
