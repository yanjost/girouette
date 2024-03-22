"""Dump all data coming from the serial port"""
import binascii
import serial

PORT_NAME = '/dev/tty.usbserial-B001AMKI'

serialport = serial.Serial(PORT_NAME, 9600, timeout=1)


def send_data(data: bytes):
    """Send data to the serial port and print the received data."""
    print('sending: ', str(binascii.hexlify(data)))
    serialport.write(data)
    received = serialport.read(100)
    print("received: ", str(binascii.hexlify(received)))


def send_reset():
    """Send a reset command to the display."""
    send_data(binascii.unhexlify('007e'))


def send_full_frame():
    """Send a command to make all pixels white."""
    send_data(binascii.unhexlify('007d'))


while True:
    data_serial = serialport.read(100)
    if data_serial:
        print(data_serial)
