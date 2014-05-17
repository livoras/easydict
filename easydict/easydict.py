# -*- coding: utf-8 -*-

import gtk 

from components import Tip
from dictionary import get_result_by_keyword
from logger import logger

tip = None

def _clipboard_changed(clipboard, event):
  text = clipboard.wait_for_text()
  if not text or len(text) > 1000: 
    return
  start_to_translate(text, clipboard)


def start_to_translate(text, clipboard):
  buf = tip.content.get_buffer()

  prefix = 'Translating...'
  buf.set_text(prefix)

  tip.reset_size()
  display = clipboard.get_display()
  x, y = display.get_pointer()[1:3]
  tip.move(x, y + 10)

  start_new_translation(text)
  tip.show_all()
  tip.get_focus()


def start_new_translation(keyword):
  result = get_result_by_keyword(keyword)
  content = keyword + '\n' + '-' * 80 + '\n'
  if result.get('smartResult'): 
    for rel in result['smartResult']['entries']:
      if len(rel) != 0:
        content = content + rel + '\n'
    content = content + '-' * 80 + '\n'
  content = content + result['translateResult'][0][0]['tgt']
  tip.content.set_content(content)


def listen_selection():
  clip = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
  clip.connect("owner-change", _clipboard_changed)


def run():
  global tip
  tip = Tip()
  listen_selection()
  gtk.main()

if __name__ == '__main__':
  run()
