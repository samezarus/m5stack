"""
W: 320 px
H: 320 px ?
"""

from m5stack import *
from m5ui import *
from uiflow import *


bg_color = 0x000000
setScreenColor(bg_color)


class Header:
  def __init__(self):
    self.rectangle0 = M5Rect(0, 0, 320, 32, 0x8d8282, 0x8d8282)
    self.label = M5TextBox(5, 5, "Header", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
    
  def setText(self, text: str):
    self.label.setText(text)




header = Header()
header.setText("new text")
