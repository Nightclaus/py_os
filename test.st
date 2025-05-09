# Testing indirect referenceing
PTR 0x00
STO [0x01]

# Assigning Values
PTR 0x01
STO 'Test Value 1'
PTR 0x09
STO 'Test Value 2'

# Printing "Value 1"
PTR 0x00
LDA
DIS

# Setting, and Loading the register A into memory
PTR 0x0A
LDA 0x00
RGA

# Shorthand for printing Value 2
LDA 0x09
DIS

# Printing "Value 1" (Stored via Register A)
PTR 0x0A
LDA
DIS
