# 7 Segment display

from machine import Pin
from time import sleep

# num_0 = 0b00111111
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

class Shifter():
    

    def __init__(self):
        self.data = Pin(0, Pin.OUT)
        self.clock = Pin(1, Pin.OUT)
        self.latch = Pin(2, Pin.OUT)
        self.clr = Pin(3, Pin.OUT, Pin.PULL_UP)
        self.data.value(0)
        self.clock.value(0)
        self.latch.value(0)
        self.clr.value(0)
        self.clr.value(1)

    def tick(self):
        self.clock.low()
        self.clock.high()

    def setValue(self, value):
        for i in range(8):
            bit = value >> i & 1
            if bit == 0:
                self.data.high()
            else:
                self.data.low()
            Shifter.tick(self)
    def clear(self):
        self.clr.value(0)
        self.clr.value(1)

shifter = Shifter()        
while True:
    counter = [num_0,num_1,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,char_a,char_b,char_c,char_d,char_e,char_f]
    count = 0
    for num in counter:
        count += 1
        if count == 16:
            count = 0
        print(count)
        # clear the register
        shifter.clear()
        shifter.setValue(num)
        sleep(1)
