# -*- coding: utf-8 -*-

import gtk 
import time
from threading import Thread

import mouse
from components import Tip
from dictionary import get_result_by_keyword
from logger import logger

tip = None

def get_clipboard_and_translate():
  clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
  text = clipboard.wait_for_text() or ''
  text = text.strip()
  start_to_translate(text, clipboard)


def start_to_translate(text, clipboard):
  # buf = tip.content.get_buffer()

  prefix = 'Translating...'
  # buf.set_text(prefix)

  # tip.reset_size()
  display = clipboard.get_display()
  x, y = display.get_pointer()[1:3]
  # tip.move(x, y + 10)

  start_new_translation(text)
  # tip.show_all()


def start_new_translation(keyword):
  result = get_result_by_keyword(keyword)
  content = keyword + '\n' + '-' * 80 + '\n'

  if result.get('smartResult'): 
    for rel in result['smartResult']['entries']:
      if len(rel) != 0:
        content = content + rel + '\n'
    content = content + '-' * 80 + '\n'

  if result.get('translateResult'): 
    content = content + result['translateResult'][0][0]['tgt']
    
  print content
  # tip.content.set_content(content)


def listen_selection():
  status = dict(
    dirty=False,
    has_pressed=False,
    previous_release_time=0
  )

  def press():
    # tip.hide()
    status['has_pressed'] = True

  def move():
    if status['has_pressed']:
      status['dirty'] = True

  def release():
    has_selected = status['has_pressed'] and status['dirty']
    c_time = time.time()
    is_double_click = c_time - status['previous_release_time'] < 0.5
    status['previous_release_time'] = c_time
    if has_selected or is_double_click:
      get_clipboard_and_translate()
    status['dirty'] = False
    status['has_pressed'] = False

  mouse.on('press', press)
  mouse.on('move', move)
  mouse.on('release', release)


def run():
  global tip
  tip = Tip()
  tip.content.set_content('fuck')
  tip.show_all()
  listen_selection()
  mouse.run()


if __name__ == '__main__':
  run()
  gtk.main()
