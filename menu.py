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
    self.bg_color = 0x8d8282
    self.text_color = 0xFFFFFF
    self.rectangle = M5Rect(0, 0, 320, 32, self.bg_color, self.bg_color)
    self.label = M5TextBox(x=5, y=5, text="Header", font=lcd.FONT_DejaVu24, color=self.text_color, rotate=0)
    
  def setText(self, text: str):
    self.rectangle = M5Rect(0, 0, 320, 32, self.bg_color, self.bg_color)
    self.label = M5TextBox(x=5, y=5, text=text, font=lcd.FONT_DejaVu24, color=self.text_color, rotate=0)
    #self.rectangle.setBgColor(self.color)
    #self.label.setText(text)
    

header = Header()
header.setText("new")
header.setText("11")
#header.setText("0")


