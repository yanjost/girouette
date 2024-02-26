def compute_payload(str_to_send, spacing=2):
    payload = bytes([0x00, 0x01, 0x01, spacing, 0x02, 0x02, 0x00, 0x00])
    payload += bytes([len(str_to_send)])
    payload += str_to_send.encode('ascii')
    return payload

def xor(a,b):
    return a^b

def checksum(payload):
    checksum = 0
    for byte in payload:
        checksum = xor(checksum, byte)
    return checksum

def compute_text_frame(address, text_data, spacing=2):
    payload = compute_payload(text_data, spacing=spacing)
    payload_length = len(payload)

    message = bytes([0x00, address, payload_length, 0x00])+payload
    # compute checksum by xoring all bytes
    checksum = 0
    for byte in payload:
        checksum = xor(checksum, byte)
    message += bytes([checksum])
    message += bytes([0x00])
    return message

print(compute_text_frame(0x02, 'Hack SXB'))

