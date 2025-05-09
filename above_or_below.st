// Store a random number
SET 0x00
RAN
RGA

// Store input into 0x01
SET 0x01
INP 'Guess a number! '
RGA 

// Check if it is correct
LDA 0x01
CMP 0x00
JEQ 16
JMP 22

// Display Success
SET 0x02
STO "You win"
DIS
HLT

// Higher or lower
LDA 0x01
GRE 0x00
JEQ 29
JMP 34

SET 0x02
STO "Higher"
DIS
JMP 6

SET 0x02
STO "Lower"
DIS
JMP 6

HLT