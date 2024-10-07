from machine import Pin, PWM
import time,random
# import perlin

import array

import waveform
WAVEFORM = waveform.WAVEFORM


def pulse(l: PWM, t:int):
    for i in range(len(WAVEFORM)):
        l.duty_u16(WAVEFORM[i])
        print (f"{i} : {WAVEFORM[i]}")
        time.sleep_ms(t)

led_pin = Pin("LED", Pin.OUT)
candle  = PWM(led_pin,32768)
candle.freq(10000) # 1Hz
print("LED starts flashing...")
for i in range(10):
    try :   
        pulse(candle, 50  )
    except KeyboardInterrupt:
        break   
candle.duty_u16(0)
print("Finished.")
