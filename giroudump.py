import serial
import binascii

portname = '/dev/tty.usbserial-B001AMKI'

serialport = serial.Serial(portname, 9600, timeout=1)

def send_data(data):
    print('sending: ', str(binascii.hexlify(data)))
    serialport.write(data)
    received = serialport.read(100)
    print("received: ", str(binascii.hexlify(received)))

def send_reset():
    send_data(binascii.unhexlify('007e'))

def send_full_frame():
    send_data(binascii.unhexlify('007d'))

while True:
    data=serial.read(100)
    if data:
        print(data)