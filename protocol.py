def compute_text_command(str_to_send, spacing=2):
    """Compute a text display payload"""
    payload = bytes([0x00, 0x01, 0x01, spacing, 0x02, 0x02, 0x00, 0x00])
    payload += bytes([len(str_to_send)])
    payload += str_to_send.encode('ascii')
    return payload


def xor(a, b):
    """XOR two bytes"""
    return a ^ b


def checksum(payload):
    """Compute the checksum of a payload"""
    checksum = 0
    for byte in payload:
        checksum = xor(checksum, byte)
    return checksum


def compute_text_frame(address, text_data, spacing=2):
    """Compute a text display frame message"""
    payload = compute_text_command(text_data, spacing=spacing)
    payload_length = len(payload)

    message = bytes([0x00, address, payload_length, 0x00]) + payload
    # compute checksum by xoring all bytes
    checksum = 0
    for byte in payload:
        checksum = xor(checksum, byte)
    message += bytes([checksum])
    message += bytes([0x00])
    return message


def parse_text_frame(frame):
    """Parse a text frame to a python dictionary"""
    address = frame[1]
    payload_length = frame[2]
    payload = frame[4:4 + payload_length]
    checksum = frame[4 + payload_length]
    return {
        'address': address,
        'payload_length': payload_length,
        'payload': payload,
        'checksum': checksum
    }


print(compute_text_frame(0x02, 'Hack SXB'))
