# -*- coding: utf-8 -*-

import gtk 

class Content(gtk.TextView):

  def __init__(self):
    super(Content, self).__init__(None)
    self._draw()

  def _draw(self):
    self.set_editable(False)
    MARGIN = 10
    self.set_left_margin(MARGIN)
    self.set_right_margin(MARGIN)
    self.set_pixels_above_lines(3)
    self.set_pixels_below_lines(3)
    self.set_wrap_mode(gtk.WRAP_WORD)

  def set_content(self, content):
    buf = gtk.TextBuffer()
    buf.set_text(content)
    self.set_buffer(buf)


class Tip(gtk.Window):

  def __init__(self):
    super(Tip, self).__init__(gtk.WINDOW_TOPLEVEL)
    self._draw()
    self._add_content()
    self._hide_when_blur()
    # The way how to show window without focusing
    # URL: http://stackoverflow.com/questions/2143152/open-a-pygtk-program-but-do-not-activate-it
    self.set_accept_focus(False)

  def _draw(self):
    self.set_decorated(False)
    self.stick()
    self.set_keep_above(True)
    self.reset_size()
    self.set_border_width(2)
    self.set_geometry_hints(max_height=500, max_width=300)
    self.move(100, 100)

  def _add_content(self):
    self.content = Content()
    self.content.show()
    self.add(self.content)

  def _hide_when_blur(self):
    self.connect('focus_out_event', lambda w, e: self.hide())

  def reset_size(self):
    self.resize(500, 100)

if __name__ == '__main__':
  import time, thread, gtk, gobject
  gtk.gdk.threads_init()
  tip = Tip()
  tip.show_all()
  count = [1]

  # The modification of GTK GUI must be in the main loop.
  # http://unpythonic.blogspot.com/2007/08/using-threads-in-pygtk.html
  def modify():
    tip.content.set_content(str(count[0]))

  def fuck():
    while count[0] < 100:
      print count[0]
      count[0] += 1
      time.sleep(1)
      gobject.idle_add(modify)    

  thread.start_new_thread(fuck, ())  
  gtk.main()
