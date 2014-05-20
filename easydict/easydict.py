# -*- coding: utf-8 -*-

import gtk 
import gobject
import time
import threading
import thread
import random
import os

import mouse
from components import Tip
from dictionary import get_result_by_keyword
from logger import logger

tip = None
text = None
clip = None
gtk.gdk.threads_init()

def get_clipboard_and_translate():
  if not text: return
  tip.content.set_content('Translating...')
  tip.reset_size()
  display = clip.get_display()
  x, y = display.get_pointer()[1:3]
  tip.move(x, y + 10)
  start_new_translation(text)


def start_new_translation(keyword):
  result = get_result_by_keyword(keyword)
  if not result: return
  content = keyword + '\n' + '-' * 80 + '\n'

  if result.get('smartResult'): 
    for rel in result['smartResult']['entries']:
      if len(rel) != 0:
        content = content + rel + '\n'
    content = content + '-' * 80 + '\n'

  if result.get('translateResult'): 
    content = content + result['translateResult'][0][0]['tgt']
    
  logger.debug('Content: %s' % content)
  tip.content.set_content(content)
  tip.present()


def listen_selection():
  status = dict(
    dirty=False,
    has_pressed=False,
    previous_release_time=0
  )

  def press():
    status['has_pressed'] = True

  def move():
    if status['has_pressed']:
      status['dirty'] = True

  def release():
    gobject.idle_add(tip.hide)
    has_selected = status['has_pressed'] and status['dirty']
    c_time = time.time()
    is_double_click = c_time - status['previous_release_time'] < 0.2
    status['previous_release_time'] = c_time
    if has_selected or is_double_click:
      gobject.idle_add(get_clipboard_and_translate)
    status['dirty'] = False
    status['has_pressed'] = False

  mouse.on('press', press)
  mouse.on('move', move)
  mouse.on('release', release)

  retrieve_selected_text()

def _clipboard_changed(clipboard, event):
  global text
  text = clipboard.wait_for_text()

def retrieve_selected_text():
  global clip
  clip = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
  clip.connect("owner-change", _clipboard_changed)  

def mouse_loop():
  listen_selection()
  mouse.run()

def run():
  global tip
  tip = Tip()
  thread_for_mouse = threading.Thread(target=mouse_loop)
  thread_for_mouse.start()
  gtk.main()

if __name__ == '__main__':
  run()
