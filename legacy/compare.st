# Set the completion to false
PTR 0x02
STO "Not Done"

# This is the code that needs to be repeated (Below)
PTR 0x00
STO 'Message 1'
DIS 

# Validate the completion
LDA 0x02
CMP "Done"
JEQ 29

# Set the completion status
PTR 0x02
STO "Done"

# Storing a value
PTR 0x01
STO 12

# Loading and comparing that value
LDA 0x01
CMP 12

# Jump to line 4 only if 0x01 == 12
JEQ 6

HLT