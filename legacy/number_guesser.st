# Store 23 as the winning number
PTR 0x00
STO 23

# Store input into 0x01
PTR 0x01
INP 'Guess a number! '
RGA 

LDA 0x01
CMP 0x00
JEQ 16
JMP 22

# Display Success
PTR 0x02
STO "You win"
DIS
JMP 26

# Display Failed
PTR 0x02
STO "You Lose"
DIS

HLT