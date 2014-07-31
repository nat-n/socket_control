#!/usr/bin/python

import os
import pimote
from bottle import route, run, static_file


# Setup

pimote.init()
pimote.both_off()

ROOT_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

STATE = {
    'socket1': False,
    'socket2': False
}


# Declare Endpoints

@route('/')
def index():
    return static_file("index.html", root=ROOT_PATH)


@route('/status')
def status():
    return STATE


@route('/1/0')
def socket1on():
    print STATE
    STATE['socket1'] = not pimote.one_off()
    print STATE
    return STATE


@route('/1/1')
def socket2off():
    print STATE
    STATE['socket1'] = pimote.one_on()
    print STATE
    return STATE


@route('/2/0')
def socket1on():
    print STATE
    STATE['socket2'] = not pimote.two_off()
    print STATE
    return STATE


@route('/2/1')
def socket2off():
    print STATE
    STATE['socket2'] = pimote.two_on()
    print STATE
    return STATE


# Run server
run(host='0.0.0.0', port=8080)

# Clean up
pimote.term()
