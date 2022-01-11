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
    self.color = 0x8d8282
    self.rectangle = M5Rect(0, 0, 320, 32, self.color, self.color)
    self.label = M5TextBox(x=5, y=5, text="Header", font=lcd.FONT_DejaVu24, color=0xFFFFFF, rotate=0)
    
  def setText(self, text: str):
    self.rectangle.setBgColor(self.color)
    self.label.setText(text)
    

header = Header()
header.setText("new")
header.setText("11")
