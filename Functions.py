import re

def intToBin(x, n):
    bits = ""
    for i in range(n):
        bits = ("1" if x & 1 else "0") + bits
        x >>= 1
    return bits

def towsComp(bits):
    return intToBin(-1 * int(bits, 2), len(bits))

def hexToBin(x, n):
    neg = False
    if x[0] == '-':
        neg = True
        x = x[1:]

    bits = ""
    for c in x:
        i = 10+ord(c)-ord('A') if c.isalpha() else int(c)
        bits += intToBin(i, 4)

    if len(bits) < n:
        bits = (n - len(bits)) * '0' + bits
    else:
        bits = bits[-n:]

    return towsComp(bits) if neg else bits


def decR(tok):
    if tok[0] != 'X':
        print('Registers must be written as X<reg num>')
        exit(1)
    return intToBin(int(tok[1:]), 5)

def decI(tok, size):
    if tok[0] == '#':
        return intToBin(int(tok[1:]), size)
    return hexToBin(tok, size)

def tokenize(str):
    return re.split('\s*,\s*', str)

def R(asm, shamt):
    toks = tokenize(asm)
    return decR(toks[2]) + shamt + decR(toks[1]) + decR(toks[0])

def I(asm, shamt):
    toks = tokenize(asm)
    return decI(toks[2], 12) + decR(toks[1]) + decR(toks[0])

def D(asm, shamt):
    toks = tokenize(asm)
    if toks[1][0] != '[' or toks[2][-1] != ']':
        print('"D" instructions must be of the form "[X<regNum>, #<offset>]"')
        exit(1)
    return decI(toks[2][:-1], 9) + "00" + decR(toks[1][1:]) + decR(toks[0])

def B(asm, shamt):
    return decI(asm, 26)

def CB(asm, shamt):
    toks = tokenize(asm)
    return decI(toks[1], 19) + decR(toks[0])

def IM(asm, shamt):
    toks = tokenize(asm)

    lsl = re.split('\s+#?', toks[2])
    if lsl[0] != 'LSL':
        print('Move immediate instructions must have "LSL <number>"')
        exit(1)

    shamt = int(lsl[1], 16)

    if shamt == 0:
        shift = '00'
    elif shamt == 16:
        shift = '01'
    elif shamt == 32:
        shift = '10'
    elif shamt == 48:
        shift = '11'
    else:
        print('Shift amount must be #0, #16, #32, or #48')
        exit(1)

    return shift + decI(toks[1], 16) + decR(toks[0])