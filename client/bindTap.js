// This saves on having to load jquery mobile or some other bloat
window.bindTap = (function() {
  /* The bindTap function watches for a tap gesture or click action on the given
   * element and fires the given callback when one OR the other occurs.
   * A tap gesture is defined as a touch start followed by a touch end without
   * the touch being canceled or moving more than 25px from the initial position
   * horizontally or vertically. If a tap gesture is detected then click
   * handler will ignore all clicks for the next 500ms.
   */

  // Register that a tap has started
  function startTap(event) {
    this.touchStartLocation = [event.touches[0].clientX,
                               event.touches[0].clientY];
  }

  // Cancel the tap if the touch has moved too far from the start
  function touchMove(event) {
    if (this.touchStartLocation &&
      (Math.abs(this.touchStartLocation[0] - event.touches[0].clientX) > 25 ||
       Math.abs(this.touchStartLocation[1] - event.touches[0].clientY) > 25)) {
      this.cancelTap();
    }
  }

  // Cancel tap
  function cancelTap() {
    this.touchStartLocation = null;
  }

  function completeTap() {
    if (this.touchStartLocation) {
      this.callback.apply(this.element, arguments);
      // Remember that there was a Tap gesture in this area for the next second.
      this.recentTaps += 1;
      setTimeout(this.forgetTap, 500);
      this.touchStartLocation = null;
    }
  }

  function forgetTap() {
    this.recentTaps -= 1;
  }

  function handleClick() {
    // Block clicks when there has recently been a tap gesture
    if (this.recentTaps === 0) {
      this.callback.apply(this.element, arguments);
    }
  }

  function handleEvent(event) {
    switch (event.type) {
      case 'touchstart' : this.startTap(event);    break;
      case 'touchmove'  : this.touchMove(event);   break;
      case 'touchcancel': this.cancelTap();        break;
      case 'touchend'   : this.completeTap(event); break;
      case 'click'      : this.handleClick(event); break;
    }
  }

  function bindTap(element, callback, useCapture) {
    this.element            = element;
    this.callback           = callback;
    this.useCapture         = !!useCapture;
    this.touchStartLocation = null;
    this.recentTaps         = 0;

    this.startTap    = startTap;
    this.touchMove   = touchMove;
    this.cancelTap   = cancelTap;
    this.completeTap = completeTap;
    this.forgetTap   = forgetTap;
    this.handleClick = handleClick;
    this.handleEvent = handleEvent;

    element.addEventListener("touchstart",  this, this.useCapture);
    element.addEventListener("touchmove",   this, this.useCapture);
    element.addEventListener("touchcancel", this, this.useCapture);
    element.addEventListener("touchend",    this, this.useCapture);
    element.addEventListener("click",       this, this.useCapture);
  }

  return function(element, callback, useCapture) {
    return new bindTap(element, callback, useCapture)
  }
}());