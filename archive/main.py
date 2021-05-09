from time import sleep
from machine import Pin

data_pin = Pin(0, Pin.OUT)
clock_pin = Pin(1, Pin.OUT)
latch_pin = Pin(2, Pin.OUT)

data_pin.low()
latch_pin.low()
clock_pin.low()

delay = 1

def set_num_lights(value):
    global num_lights, back_bytes
    num_lights = value
    back_bytes = [0 for pos in range(num_lights // 8)]

def latch():
    latch_pin.high()
    latch_pin.low()

def clock():
    clock_pin.high()
    clock_pin.low()

def shift_byte(value):
    bit = 1
    for step in range(8):
        if value & bit != 0:
            data_pin.high()
        else:
            data_pin.low()
        clock()
        bit = bit << 1

def show_bits():
    for pos in range(len(back_bytes)):
        shift_byte(back_bytes[pos])
    latch()

set_num_lights(2)
show_bits()