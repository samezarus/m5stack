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
    
    self.r_x = 0
    self.r_y = 0
    self.r_w = 320
    self.r_h = 32
    self.rectangle = M5Rect(self.r_x, self.r_y, self.r_w, self.r_h, self.bg_color, self.bg_color)
    
    self.l_x = 5
    self.l_y = 5
    self.label = M5TextBox(self.l_x, self.l_y, text="Header", font=lcd.FONT_DejaVu24, color=self.text_color, rotate=0)
    
  def setText(self, text: str):
    self.rectangle = M5Rect(self.r_x, self.r_y, self.r_w, self.r_h, self.bg_color, self.bg_color)
    self.label = M5TextBox(self.l_x, self.l_y, text=text, font=lcd.FONT_DejaVu24, color=self.text_color, rotate=0)
    #self.rectangle.setBgColor(self.color)
    #self.label.setText(text)
    

header = Header()
header.setText("/")
#header.setText("0")
