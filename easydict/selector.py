# -*- coding: utf-8 -*-

import gtk

def _clipboard_changed(clipboard, event):
  text = clipboard.wait_for_text()
  print text

def listen_selection():
  clip = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY)
  clip.connect("owner-change", _clipboard_changed)
  gtk.main()
