SET 0x1 // Can optimise to 27 lines via properly handling If and Else
RAN
RGA
LDA 0x1
NCP 0x1
JEQ 33
SET 0x2
INP "What is your guess "
RGA
LDA 0x2
CMP 0x1
JEQ 14
JMP 18
SET 0x00
STO "You Win"
DIS
HLT
LDA 0x2
LES 0x1
JEQ 22
JMP 25
SET 0x00
STO "Higher"
DIS
LDA 0x2
GRE 0x1
JEQ 29
JMP 32
SET 0x00
STO "Lower"
DIS
JMP 4
HLT