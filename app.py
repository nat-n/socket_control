#!/usr/bin/python

import os
import pimote
from bottle import route, run, static_file


# Setup

pimote.init()
pimote.switch('all-off')

ROOT_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

STATE = {
    1: False,
    2: False,
    3: False,
    4: False,
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
    STATE[1] = not pimote.switch('1-off')
    return STATE


@route('/1/1')
def socket2off():
    STATE[1] = pimote.switch('1-on')
    return STATE


@route('/2/0')
def socket1on():
    STATE[2] = not pimote.switch('2-off')
    return STATE


@route('/2/1')
def socket2off():
    STATE[2] = pimote.switch('2-on')
    return STATE


@route('/3/0')
def socket1on():
    STATE[3] = not pimote.switch('3-off')
    return STATE


@route('/3/1')
def socket2off():
    STATE[3] = pimote.switch('3-on')
    return STATE


@route('/4/0')
def socket1on():
    STATE[4] = not pimote.switch('4-off')
    return STATE


@route('/4/1')
def socket2off():
    STATE[4] = pimote.switch('4-on')
    return STATE


# Run server
run(host='0.0.0.0', port=8080)

# Clean up
pimote.term()
