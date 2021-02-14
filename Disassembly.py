from Shamt import SHAMT
from Condition import REV_COND

def tabbed(ins):
    return ins + (8-len(ins)) * ' '

def num(bits):
    return str(int(bits, 2))

def numS(bits):
    num = int(bits, 2)
    if bits[0] == '1':
        return str(num - 2**len(bits))
    return str(int(bits, 2))

def RB(ins, bits):
    adr = bits[6:]
    return tabbed(ins) + '#' + numS(adr)

def RD(ins, bits):
    adr = bits[11:20]
    rn = bits[22:27]
    rt = bits[27:]
    return tabbed(ins) + 'X' + num(rt) + ', X' + num(rn) + ', #' + numS(adr)

def RI(ins, bits):
    im = bits[10:22]
    rn = bits[22:27]
    rd = bits[27:]
    return tabbed(ins) + 'X' + num(rd) + ', X' + num(rn) + ', #' + numS(im)

def RR(ins, bits):
    sh = bits[16:22]
    if ins is None:
        ins = SHAMT[bits[:11]][sh]
    rm = bits[11:16]
    rn = bits[22:27]
    rd = bits[27:]
    return tabbed(ins) + 'X' + num(rd) + ', X' + num(rn) + ', X' + num(rm)

def RCB(ins, bits):
    rt = bits[27:]
    adr = bits[8:27]
    if ins == 'B.cnd':
        return tabbed('B.'+REV_COND[rt]) + '#' + numS(adr)
    return tabbed(ins) + 'X' + num(rt) + ', #' + numS(adr)

def RIM(ins, bits):
    sh = bits[9:11] + '0000'
    im = bits[11:27]
    rd = bits[27:]
    return tabbed(ins) + 'X' + num(rd) + ', #' + numS(im) + ', LSL #' + num(sh)
