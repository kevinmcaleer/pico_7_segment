from machine import Pin, SPI
from time import sleep

data_pin = Pin(0, Pin.OUT)
clock_pin = Pin(1, Pin.OUT)
latch_pin = Pin(2, Pin.OUT)
data_pin.value(0)
clock_pin.value(0)
latch_pin.value(0)

num_0 = 0b00000001
num_1 = 0b00000010
num_2 = 0b00000011
num_3 = 0b00000100
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

delay = 0.20

count = 0

def shifter(value):
    latch_pin.low()
    for x in range(8):
        data_pin.value(value >> x & 1)
        clock_pin.low()
        clock_pin.high()
        # clock_pin.high()
    # latch_pin.high()
    latch_pin.high()

# while True:
#     count += 1
#     print("writing data", count)
#     write_bit(num_0)
#     write_bit(num_1)
#     write_bit(num_2)
#     write_bit(num_3)
#     sleep(1)
    
for x in range(255):
    shifter(x)
    print(x)
    sleep(1)