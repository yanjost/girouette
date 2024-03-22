import binascii
import time
import datetime
import serial
from PIL import Image
from protocol import *
import art

# change this value to the serial port of your device
portname = '/dev/tty.usbserial-B001AMKI'

# a faster timeout will help the program run faster
# but you may overflow the input buffer of the display
serialport = serial.Serial(portname, 9600, timeout=.1)


def send_data(data):
    """Send data over serial port and print the received data."""
    data_length = len(data)
    print(f'sending {data_length} bytes: ', str(binascii.hexlify(data)))
    serialport.write(data)
    received = serialport.read(100)
    data_length = len(received)
    print(f"received {data_length} bytes: ", str(binascii.hexlify(received)))


# resets the screen
def send_reset():
    """Send a reset command to the display."""
    send_data(binascii.unhexlify('007e'))


# makes all pixels white
def send_full_frame():
    """Send a command to make all pixels white."""
    send_data(binascii.unhexlify('007d'))


# convert ascii hex representation to binary
def to_bin(data: str):
    """Convert ascii hex representation to binary."""
    return binascii.unhexlify(data.replace('\n', '').replace(' ', ''))


# sends a simple ping message
def send_ping():
    """Send a ping message to the display."""
    send_data(binascii.unhexlify('0004014141'))


data_john_1_ok = """
00 04 0b FF 00 00 08 00 00 FF FF 00 00 00 00 FF FF 00 00 F7 00
"""

data_john_2 = """
00 04 E3 FF 00 00 E0 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 88 88 44 44 22 22 11 11 1F 00
"""

data_john_3 = """
00 04 0b FF 08 08 00 00 FF FF 00 00 00 00 FF FF 00 00 FF 00
"""

data_4 = """
00 04 E3 FF 00 00 E0 A0 00 00 E0 00 00 E0 00 00 E0 60 F8 FE FB FF FD FF FF FF FF FF FD FF F9 FF F0 FE E3 FC F7 FC E1 80 20 00 00 E0 00 00 F0 00 00 10 00 00 F8 00 00 F8 00 00 0C 00 00 F8 00 00 F0 00 00 F0 00 00 F8 00 00 0C 00 00 F8 00 00 78 00 00 10 00 00 F0 00 00 E0 00 00 A0 00 00 E0 00 00 E0 00 00 E0 60 F8 FE FB FF FD FF FF FF FF FF FD FF F9 FF F0 FE E3 FC F7 FC E1 80 20 00 00 E0 00 00 F0 00 00 10 00 00 F8 00 00 F8 00 00 0C 00 00 F8 00 00 F0 00 00 F0 00 00 F8 00 00 0C 00 00 F8 00 00 78 00 00 10 00 00 F0 00 00 E0 00 00 A0 00 00 E0 00 00 E0 00 00 E0 60 F8 FE FB FF FD FF FF FF FF FF FD FF F9 FF F0 FE E3 FC F7 FC E1 80 20 00 00 E0 00 00 F0 00 00 10 00 00 F8 00 00 F8 00 00 0C 00 00 F8 00 00 F0 00 00 F0 00 00 F8 00 00 0C 00 00 F8 00 00 78 00 00 10 00 00 F0 00 00 E0 00 00 A0 00 00 E0 00 00 E0 00 00 E0 60 F8 FE FB FF FD FF FF FF FF FF FD FF F9 FF F0 FE E3 FC F7 FC E1 80 20 00 00 80
"""

data_john = data_john_2

send_reset()

str_to_send = """
``'-.,_,.-'``'-.,_,.='``
 ``'-.,_,.-'``'-.,_,.='``
  ``'-.,_,.-'``'-.,_,.='``
   ``'-.,_,.-'``'-.,_,.='``
    ``'-.,_,.-'``'-.,_,.='``
     ``'-.,_,.-'``'-.,_,.='``
      ``'-.,_,.-'``'-.,_,.='``
       ``'-.,_,.-'``'-.,_,.='``
"""


# for str_to_send in str_to_send.split('\n'):
#     send_data(compute_text_frame(0x04, str_to_send))
#     send_ping()
#     time.sleep(1)

# str_to_send = art.text2art('''HackSXB  
# is 
# the
# best''', font="wizard") # Multi-line print

# for str_to_send in str_to_send.split('\n'):
#     send_data(compute_text_frame(0x04, str_to_send))
#     send_ping()
#     time.sleep(0.5)

def send_wave(data, loops=10):
    """Make some text display scrolling. Note: not very efficient. There is a built-in function for that in the display."""
    len_data = len(data)
    for i in range(loops):
        for j in range(len_data):
            data_to_send = data[j:] + data[:j]
            send_data(compute_text_frame(0x04, data_to_send))
            send_ping()
            time.sleep(0.2)


def show_wave():
    """Display a wave on the screen."""
    send_wave("""``'-._.-""")


def show_message_loop():
    """Display a message on the screen with a scrolling effect."""
    send_wave('HackSXB #121')


def show_clock():
    """Show a clock on the screen."""
    while True:
        dt = datetime.datetime.now()
        send_data(compute_text_frame(0x04, str(dt.timestamp()), spacing=2))
        send_ping()
        time.sleep(0.250)


# send_data(compute_text_frame(0x04, "data 1"))
# time.sleep(0.5)
# send_reset()
# send_data(to_bin(data_john_1_ok))
# time.sleep(0.5)
# send_ping()
# time.sleep(1)
# send_data(compute_text_frame(0x04, "data 2"))
# send_reset()
# time.sleep(0.5)
# send_data(to_bin(data_john_3))
# time.sleep(0.5)
# send_ping()
# time.sleep(1)
# send_data(compute_text_frame(0x04, "end"))
# send_ping()
# show_message_loop()

# send_data(compute_text_frame(0x04, "Liberi este"))
# send_ping()

# open file logo.png and convert it to monochrome with Pillow
# then store the raw bytes in the data variable

# import pygame 
# import pygame.camera
# pygame.camera.init() 
# cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(640,480))
# cam.start() 

img = Image.open('image_noir_blanc.png').convert('1')


def img_to_buffer(img: "PIL.Image"):
    """Convert an image to a pixel stream that the display can show."""
    width, height = img.size
    data = bytes()

    for x in range(width):
        col_value = 0

        for y in range(height):
            value = img.getpixel((x, y))
            bin_value = 1 if value < 128 else 0
            col_value += bin_value << (y)

        data += col_value.to_bytes(2, byteorder='big')

    return data


def escape_buffer(data):
    """Escape the 0x00 bytes in the buffer."""
    escaped = bytes()
    for byte in data:
        if byte == 0x00:
            escaped += bytes([0x00, 0x00])
        else:
            escaped += bytes([byte])
    return escaped


def img_payload(img):
    """Build an image display payload."""
    print('image size: ', img.size)
    buffer = bytes()
    width, _ = img.size
    data = img_to_buffer(img)
    buffer += bytes([0xff, int((122 - width) / 2), len(data)]) + data
    length = len(buffer)
    buffer += bytes([checksum(buffer)])
    payload_to_send = bytes([0x00, 0x04, length, ]) + escape_buffer(buffer) + bytes([0x00])
    return payload_to_send


buf = img_payload(img)

# send_data(compute_text_frame(0x04, "data 1"))
# time.sleep(0.5)
# send_reset()
# send_data(buf)
# time.sleep(0.5)
# send_ping()
# send_ping()
# time.sleep(1)

send_data(compute_text_frame(0x04, "Hello Walid"))
send_reset()

time.sleep(0.5)
