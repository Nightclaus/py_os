SET value_a
STO 12
SET value_b
STO 10
LDA value_a
CMP value_b
JEQ 11
LDA value_a
DIS
JMP 11
HLT