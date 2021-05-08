from machine import Pin, SPI
from time import sleep

dp = Pin(0, Pin.OUT)
cl = Pin(1, Pin.OUT)
la = Pin(2, Pin.OUT)
clr = Pin(3, Pin.OUT, Pin.PULL_UP)
dp.value(0)
cl.value(0)
la.value(0)


def clear():
    clr.low()
    clr.high()

clear()

def tick():
    cl.low()
    cl.high()

def latch():
    la.high()
    la.low()

def counter():
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

# write 10101010 into the register

dp.high() #1
tick()
dp.low() #2
tick()
dp.low() #3
tick()
dp.high() #4
tick()
dp.low() #5
tick()
dp.high() #6
tick()
dp.low() #7
tick()
dp.high() #8
tick()
latch()
clear()

counter()