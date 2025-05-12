// Store a random number
SET 0x00
RAN
RGA

// Store a random number
SET 0x00
STO "Value to store"

// Load number from pointer
LDA 0x00

// IF ELSE
LDA 0x01 // Pointer for arg 1
CMP 0x00 // Pointer for arg 2
JEQ 19   // True
JMP 22   // False
// Content
JMP 21   // Move to ENDIF
// Content
JMP 21   // Move to ENDIF


// Load number from pointer
LDA 0x00

// WHILE Condition
START_WHILE_1
LDA 0x01 // Pointer for arg 1
CMP 0x00 // Pointer for arg 2
JEQ END_WHILE_1 (43)   // Complete Loop
JMP 17   // Continue Loop

// Content

JMP START_WHILE_1 (34)
END_WHILE_1

// REPEAT
START_REPEAT_1
SET 0x02      // Any free pointer
STO 4         // Limit
SET 0x03      // Any free pointer
STO 0         // Amount of time completed

// Content

INC 0x03
LDA 0x01 // Pointer for arg 1
CMP 0x00 // Pointer for arg 2
NOT      // Not completed
JEQ START_REPEAT_1 (46)
END_REPEAT_1

// No FOR yet bc they need ARRAYS as a data type, not yet concieved

// Function, Either placed into code at compile, or have redirects
// Redirect method

// Calling
SET 0x04     // Assigned return pointer for this function
STO 68       // Return Address
JMP 71       // Function location

// Actual function
// Content
LDA 0x04
ADD 2       // Make sure it doesnt trigger the jump again (could be done by the compiler)
JPA         // Return back to after jump

// END
HLT