import binascii

fulldata=bytes()
f=open('data.hex')
for line in f:
    line = line[1:].strip()
    fulldata+=binascii.unhexlify(line)

f2=open('data.bin','wb')
f2.write(fulldata)