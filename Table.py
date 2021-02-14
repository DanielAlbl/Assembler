from Functions import *
from Disassembly import *

TABLE = {'B'     : (B , '000101'     , None    ),
         'FMULS' : (R , '00011110001', '000010'),
         'FDIVS' : (R , '00011110001', '000110'),
         'FCMPS' : (R , '00011110001', '001000'),
         'FADDS' : (R , '00011110001', '001010'),
         'FSUBS' : (R , '00011110001', '001110'),
         'FMULD' : (R , '00011110011', '000010'),
         'FDIVD' : (R , '00011110011', '000110'),
         'FCMPD' : (R , '00011110011', '001000'),
         'FADDD' : (R , '00011110011', '001010'),
         'FSUBD' : (R , '00011110011', '001110'),
         'STURB' : (D , '00111000000', None    ),
         'LDURB' : (D , '00111000010', None    ),
         'B.cnd' : (CB, '01010100'   , None    ),
         'STURH' : (D , '01111000000', None    ),
         'LDURH' : (D , '01111000010', None    ),
         'AND'   : (R , '10001010000', '000000'),
         'ADD'   : (R , '10001011000', '000000'),
         'ADDI'  : (I , '1001000100' , None    ),
         'ANDI'  : (I , '1001001000' , None    ),
         'BL'    : (B , '100101'     , None    ),
         'SDIV'  : (R , '10011010110', '000010'),
         'UDIV'  : (R , '10011010110', '000011'),
         'MUL'   : (R , '10011011000', '011111'),
         'SMULH' : (R , '10011011010', '000000'),
         'UMULH' : (R , '10011011110', '000000'),
         'ORR'   : (R , '10101010000', '000000'),
         'ADDS'  : (R , '10101011000', '000000'),
         'ADDIS' : (I , '1011000100' , None    ),
         'ORRI'  : (I , '1011001000' , None    ),
         'CBZ'   : (CB, '10110100'   , None    ),
         'CBNZ'  : (CB, '10110101'   , None    ),
         'STURW' : (D , '10111000000', None    ),
         'LDURSW': (D , '10111000100', None    ),
         'STURS' : (R , '10111100000', '000000'),
         'LDURS' : (R , '10111100010', '000000'),
         'STXR'  : (D , '11001000000', None    ),
         'LDXR'  : (D , '11001000010', None    ),
         'EOR'   : (R , '11001010000', '000000'),
         'SUB'   : (R , '11001011000', '000000'),
         'SUBI'  : (I , '1101000100' , None    ),
         'EORI'  : (I , '1101001000' , None    ),
         'MOVZ'  : (IM, '110100101'  , None    ),
         'LSR'   : (R , '11010011010', '000000'),
         'LSL'   : (R , '11010011011', '000000'),
         'BR'    : (R , '11010110000', '000000'),
         'ANDS'  : (R , '11101010000', '000000'),
         'SUBS'  : (R , '11101011000', '000000'),
         'SUBIS' : (I , '1111000100' , None    ),
         'ANDIS' : (I , '1111001000' , None    ),
         'MOVK'  : (IM, '111100101'  , None    ),
         'STUR'  : (D , '11111000000', None    ),
         'LDUR'  : (D , '11111000010', None    ),
         'STURD' : (R , '11111100000', '000000'),
         'LDURD' : (R , '11111100010', '000000')}

REV_TABLE = {'000101'     : (RB , 'B'     ),
             '00011110001': (RR ,  None   ),
             '00111000000': (RD , 'STURB' ),
             '00111000010': (RD , 'LDURB' ),
             '01010100'   : (RCB, 'B.cnd' ),
             '01111000000': (RD , 'STURH' ),
             '01111000010': (RD , 'LDURH' ),
             '10001010000': (RR , 'AND'   ),
             '10001011000': (RR , 'ADD'   ),
             '1001000100' : (RI , 'ADDI'  ),
             '1001001000' : (RI , 'ANDI'  ),
             '100101'     : (RB , 'BL'    ),
             '10011010110': (RR , None    ),
             '10011011000': (RR , 'MUL'   ),
             '10011011010': (RR , 'SMULH' ),
             '10011011110': (RR , 'UMULH' ),
             '10101010000': (RR , 'ORR'   ),
             '10101011000': (RR , 'ADDS'  ),
             '1011000100' : (RI , 'ADDIS' ),
             '1011001000' : (RI , 'ORRI'  ),
             '10110100'   : (RCB, 'CBZ'   ),
             '10110101'   : (RCB, 'CBNZ'  ),
             '10111000000': (RD , 'STURW' ),
             '10111000100': (RD , 'LDURSW'),
             '10111100000': (RR , 'STURS' ),
             '10111100010': (RR , 'LDURS' ),
             '11001000000': (RD , 'STXR'  ),
             '11001000010': (RD , 'LDXR'  ),
             '11001010000': (RR , 'EOR'   ),
             '11001011000': (RR , 'SUB'   ),
             '1101000100' : (RI , 'SUBI'  ),
             '1101001000' : (RI , 'EORI'  ),
             '110100101'  : (RIM, 'MOVZ'  ),
             '11010011010': (RR , 'LSR'   ),
             '11010011011': (RR , 'LSL'   ),
             '11010110000': (RR , 'BR'    ),
             '11101010000': (RR , 'ANDS'  ),
             '11101011000': (RR , 'SUBS'  ),
             '1111000100' : (RI , 'SUBIS' ),
             '1111001000' : (RI , 'ANDIS' ),
             '111100101'  : (RIM, 'MOVK'  ),
             '11111000000': (RD , 'STUR'  ),
             '11111000010': (RD , 'LDUR'  ),
             '11111100000': (RR , 'STURD' ),
             '11111100010': (RR , 'LDURD' )}