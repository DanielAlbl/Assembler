from Table import TABLE, REV_TABLE
from Condition import CND

def spaceBits(bits):
    out = ''
    for i in range(8):
        out += bits[4*i:4*i+4] + ' '
    return out

def assemble(asm):
    asm = asm.upper()
    (name, asm) = asm.split(maxsplit=1)

    if name[:2] == "B.":
        return TABLE['B.cnd'][1] + CND(name[2:], asm)

    row = TABLE[name]
    bits = row[1] + row[0](asm, row[2])
    return spaceBits(bits)

def disassemble(bits):
    bits = bits.replace(' ', '')
    if bits[:6] in REV_TABLE:
        size = 6
    elif bits[:8] in REV_TABLE:
        size = 8
    elif bits[:10] in REV_TABLE:
        size = 10
    elif bits[:11] in REV_TABLE:
        size = 11
    else:
        print('Not a valid opcode')
        exit(1)

    row = REV_TABLE[bits[:size]]
    return row[0](row[1], bits)

def bit4ToHex(bin):
    n = 8*int(bin[0]) + 4*int(bin[1]) + 2*int(bin[2]) + int(bin[3])
    if n < 10:
        return str(n)
    return chr(n - 10 + ord('A'))

def hex(bin):
    hex = ""
    n = len(bin)
    bin = "000" + bin  # padding in case n % 4 != 0
    for i in range(n+3, 3, -4):
        hex = bit4ToHex(bin[i-4:i]) + hex
    return "0x" + hex

def main():
    choice = input("Assemble or Disassemble? (A/D): ")
    choice = choice.upper()

    if choice == 'A':
        asm = input("LEGv8 Instruction: ")
        bits = assemble(asm)
        print("Binary Instruction: " + bits)

    elif choice == 'D':
        bits = input("Binary Instruction: ")
        asm = disassemble(bits)
        print("LEGv8 Instruction: " + asm)

    else:
        print("Choice must be 'A' or 'D'")

if __name__ == '__main__':
    main()

