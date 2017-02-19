(function (document, $, bindTap) {
  'use strict';

  // State tracking, should mirror the backend
  var state = [],
      controlCount = 4;

  function cacheDOMElements() {
    var control, elems = {};
    for (var i = 1; i <= controlCount; i += 1) {
      control         = document.getElementById('control-' + i);
      elems[i]        = {};
      elems[i].on     = control.getElementsByClassName('on')[0];
      elems[i].off    = control.getElementsByClassName('off')[0];
      elems[i].toggle = control;
      elems[i].label  = control.getElementsByClassName('socket-name')[0];
    }

    return elems;
  }
  var elems = cacheDOMElements();

  $.get('/sockets', function (socketNames) {
    for (var i = 1; i <= controlCount; i += 1) {
      if (socketNames[i]) {
        elems[i].label.innerText = i + '. ' + socketNames[i];
      }
    }
  });

  // Updates state and display, in response to updates from the backend
  function statusCallback(response) {
    for (var i = 1; i <= controlCount; i += 1) {
      state[i] = response[i];
      if (state[i]) {
        elems[i].on.classList.add('btn-success');
        elems[i].off.classList.remove('btn-danger');
      } else {
        elems[i].on.classList.remove('btn-success');
        elems[i].off.classList.add('btn-danger');
      }
    }
  }

  // Initialise state
  $.get('/status', null, statusCallback);

  // Request the server set a socket to on or off
  function set(number, on) {
    if (number === parseInt(number, 10) &&
        number >= 1 &&
        number <= controlCount) {
      if (on) {
        $.get('/' + number + '/1', null, statusCallback);
      } else {
        $.get('/' + number + '/0', null, statusCallback);
      }
    }
  }

  // Request the server set a socket to the opposite of its last known state
  function toggle(number) {
    set(number, !state[number]);
  }

  // Bind interaction listeners to controls
  function bindControls(i) {
    bindTap(elems[i].on, function (event) {
      event.preventDefault();
      event.stopPropagation();
      set(i, 1);
      this.blur();
    });
    bindTap(elems[i].off, function (event) {
      event.preventDefault();
      event.stopPropagation();
      set(i, 0);
      this.blur();
    });
    bindTap(elems[i].toggle, function (event) {
      event.preventDefault();
      event.stopPropagation();
      toggle(i);
    });
  }
  for (var i = 1; i <= controlCount; i += 1) {
    bindControls(i);
  }

}(document, Zepto, bindTap));
