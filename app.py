#!/usr/bin/env python

import os, json
from lib.socket_controller import SocketController
from bottle import route, run, static_file
import config

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = ROOT_PATH + '/client'

sc = SocketController(config)


@route('/')
def index():
    return static_file('index.html', root=STATIC_PATH)


@route('/<filename:re:.*\.(html|js|css)>')
def index(filename):
    return static_file(filename, root=STATIC_PATH)


@route('/manifest.appcache')
def manifest():
    return static_file('manifest.appcache', root=STATIC_PATH, mimetype='text/cache-manifest')


@route('/status')
def status():
    return sc.state


@route('/sockets')
def status():
    return {
        1: config.SOCKET_NAMES[0],
        2: config.SOCKET_NAMES[1],
        3: config.SOCKET_NAMES[2],
        4: config.SOCKET_NAMES[3],
    }


@route('/<socket:re:([1234]|all)>/<state:re:[01]>')
def switch_socket(socket, state):
    """
    define catch all endpoint for sending signals to sockets like:
    /1/1  => turn_1_on
    /1/0  => turn_1_off
    """
    method = "switch_%s_%s" % (socket, ('on' if state == '1' else 'off'))
    getattr(sc, method)()
    return sc.state


if __name__ == "__main__":
    # Init SocketController and Run server
    sc.start()
    run(host='0.0.0.0', port=8080)

    # Clean up
    sc.stop()
