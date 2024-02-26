"""Convert data.hex to data.bin"""
import binascii

with open('data.hex', encoding='ascii') as f:
    fulldata=bytes()

    for line in f:
        line = line[1:].strip()
        fulldata+=binascii.unhexlify(line)
        
    with open('data.bin','wb') as f2:
        f2.write(fulldata)
        print('data.bin written')