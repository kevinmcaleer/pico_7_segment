# A simply binary counter program using the 74HC595 shift register, a Raspberry Pi Pico and some LEDs

from machine import Pin, SPI
from time import sleep

dp = Pin(0, Pin.OUT)
cl = Pin(1, Pin.OUT)
la = Pin(2, Pin.OUT)
clr = Pin(3, Pin.OUT, Pin.PULL_UP)
dp.value(0)
cl.value(0)
la.value(0)

num_0 = 0b11000000
num_1 = 0b00000110
num_2 = 0b01011011
num_3 = 0b01001111
num_4 = 0b01100110
num_5 = 0b01101101
num_6 = 0b01111101
num_7 = 0b00000111
num_8 = 0b01111111
num_9 = 0b01100111
char_a =0b01110111
char_b =0b01111100
char_c =0b00011100
char_d =0b01011110
char_e =0b01111001
char_f =0b01110001

def clear():
    # clear the shift register
    clr.low()
    clr.high()

clear()

def tick():
    # tick the clock pin
    cl.low()
    cl.high()

def latch():
    # flip the latch pin
    la.high()
    la.low()

def write(value):
    # write the values to the shift register
    for i in range(8):
        data = value >> i & 1
        print("data is", data)
        if data == 0:
            dp.high()
        else:
            dp.low()
        tick()
    latch()
    print(value)
    sleep(0.5)

def counter():
    # a simple binary counter using the 74HC595 shift register and some LEDs
    for x in range(256):
        for i in range(8):
            data = x >> i & 1
            print("data is", data)
            if data == 0:
                dp.low()
            else:
                dp.high()
            tick()
        latch()
        print(x)
        sleep(0.5)

# clear the register
clear()

# start the binary counter
counter()