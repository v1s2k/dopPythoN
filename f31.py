import struct

CS = 2 + 2 + 1 + 8 + 4 + 4 + 2 + 4
DS = 2 + 8 + 4 + 8 + 1 + 1
BS = 16


def parse_b(offset, bytes):
    b = bytes[offset:offset + BS]
    rez = struct.unpack('<QQ', b)
    return {'B1': rez[0], 'B2': rez[1]}


def parse_d(offset, bytes):
    d = bytes[offset:offset + DS]
    rez = struct.unpack('<HqIQBb', d)
    return {'D1': rez[0], 'D2': rez[1], 'D3': rez[2], 'D4': rez[3], 'D5': rez[4], 'D6': rez[5]}


def parse_c(offset, bytes):
    c = bytes[offset:offset + CS]
    rez = struct.unpack('<HHbQIIHI', c)
    c1_b = bytes[rez[1]:rez[1] + rez[0]]
    c1_r = struct.unpack('<' + 'c' * rez[0], c1_b)
    c1_pr = b''.join(c1_r).decode('utf8')
    c4_b = bytes[rez[5]:rez[5] + rez[4] * 2]
    c4_pr = struct.unpack('<' + 'H' * rez[4], c4_b)
    c4_l = [parse_d(addr, bytes) for addr in c4_pr]
    c5_b = bytes[rez[7]:rez[7] + rez[6] * 4]
    c5_r = struct.unpack('<' + 'I' * rez[6], c5_b)
    return {'C1': c1_pr, 'C2': rez[2], 'C3': rez[3], 'C4': c4_l, 'C5': list(c5_r)}


def parse_a(offset, bytes):
    a = bytes[offset:offset + 4]
    rez = struct.unpack('<HH', a)
    offset += 4
    a3 = parse_c(offset, bytes)
    offset += CS
    a = bytes[offset:offset + 4*6 + 2]
    rez45 = struct.unpack('<6fh', a)
    return {'A1': parse_b(rez[0], bytes), 'A2': rez[1], 'A3': a3, 'A4': list(rez45[0:6]), 'A5': rez45[6]}


def f31(x):
    return parse_a(4, x)