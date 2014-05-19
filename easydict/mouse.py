# -*- coding: utf-8 -*-
from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input
from Xlib.ext import record
from Xlib.protocol import rq

_display = Display(None)
_ctx = _display.record_create_context(0, [record.AllClients], [{
  'core_requests': (0, 0),
  'core_replies': (0, 0),
  'ext_requests': (0, 0, 0, 0),
  'ext_replies': (0, 0, 0, 0),
  'delivered_events': (0, 0),
  'device_events': (X.ButtonPressMask, X.ButtonReleaseMask),
  'errors': (0, 0),
  'client_started': False,
  'client_died': False,
}])

_press_events = []
_release_events = []
_move_events = []

def _handler(reply):
  data = reply.data
  while len(data):
    event, data = rq.EventField(None).parse_binary_value(data, _display.display, None, None)

    # Ignore all scroll event
    if event.detail in (5, 4):
      return

    if event.type == X.ButtonPress:
      for callback in _press_events:
        callback()
    elif event.type == X.ButtonRelease:
      for callback in _release_events:
        callback()
    elif event.type == X.MotionNotify:
      for callback in _move_events:
        callback()

def on(event_type, callback):
  if event_type == 'press':
    _press_events.append(callback)
  elif event_type == 'release':  
    _release_events.append(callback)
  elif event_type == 'move':  
    _move_events.append(callback)
  else:  
    raise ValueError(('%s event type not found') % event_type)


def run():
  _display.record_enable_context(_ctx, _handler)
