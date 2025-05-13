SET "secret_number"
STO 56
SET "user_guess"
INP "What is your guess"
RGA
LDA "user_guess"
CMP "secret_number"
JEQ 10
JMP 13
SET 0x00
STO "You Win"
DIS
LDA "user_guess"
LES "secret_number"
JEQ 17
JMP 20
SET 0x00
STO "Higher"
DIS
LDA "user_guess"
GRE "secret_number"
JEQ 24
JMP 27
SET 0x00
STO "Lower"
DIS
HLT