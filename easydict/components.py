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
    buf = self.get_buffer()
    buf.set_text(content)

    

class Tip(gtk.Window):

  def __init__(self):
    super(Tip, self).__init__(gtk.WINDOW_TOPLEVEL)
    self._draw()
    self._add_content()
    self._hide_when_blur()

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
  tip = Tip()
  tip.show_all()
  tip.content.set_content('fuckyou')
