from m5stack import *
from m5ui import *
from uiflow import *


setScreenColor(lcd.BLACK)


def buttonA_wasPressed():
  setScreenColor(0x123456)
  lcd.print('A', 0, 0)


def buttonB_wasPressed():
  setScreenColor(0x234567)
  lcd.print('B')


def buttonC_wasPressed():
  setScreenColor(0x345678)
  lcd.print('C')
  
  speaker.setVolume(0.01)
  speaker.tone(180, 20)
  wait_ms(200)
  speaker.tone(150, 20)
  wait_ms(200)
  wait_ms(2)


btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)
btnC.wasPressed(buttonC_wasPressed)
