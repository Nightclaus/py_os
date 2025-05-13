SET value_a
STO 12
SET value_b
STO 10
LDA value_a
GRE value_b
JEQ 9
JMP 11
LDA value_a
DIS
HLT