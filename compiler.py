# Matches file structure with the ST structure
END = 'HLT'
CONTENT = 'content'
IDENTIFIER = 'IDENTIFIER_'
IDENTIFIER_INCREMENT = 0

COMMAND_LOOKUP = {
    "if": [
        "LDA 0x01",
        "CMP 0x00",
        "JEQ 19",
        CONTENT,
        "JMP 21",
        CONTENT,
        END,
        ],
    "while": [
        "LDA 0x01",
        "CMP 0x00",
        "JEQ 19",
        CONTENT,
        "JMP START_WHILE_1",
        END
    ],
    "repeat": [
        CONTENT,
        "INC 0x03",
        "LDA 0x02",  # Pointer for arg 1
        "CMP 0x03",   # Pointer for arg 2
        "NOT",       # Not completed
        "JEQ START_REPEAT_1",
        END
    ],
    "storage": [
        "SET 0x02", # Any free pointer
        "STO 4",    # Limit
        "SET 0x03", # Any free pointer
        "STO 0",    # Amount of time completed
    ]
}

def getIdentfier():
    global IDENTIFIER_INCREMENT
    output = f'{IDENTIFIER}{IDENTIFIER_INCREMENT}_' # tail required
    IDENTIFIER_INCREMENT+=1
    return output

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # recurse into sublist
        else:
            result.append(item)
    return result

def _if_else(parg1, parg2, true_action, false_action):
    if_template = COMMAND_LOOKUP['if']

    if_template[0] = f'LDA {parg1}'
    if_template[1] = f'CMP {parg2}'
    if_template[2] = f'JEQ {len(true_action) + 2}' # Current position + next position
    if_template[3] = true_action
    if_template[4] = f'JMP {len(false_action) + 1}' 
    if_template[5] = false_action

    return flatten(if_template)

def _while(parg1, parg2, while_action):
    if_template = COMMAND_LOOKUP['while']

    if_template[0] = f'LDA {parg1}'
    if_template[1] = f'CMP {parg2}'
    if_template[2] = f'JEQ {len(while_action) + 2}' # Current position + next position
    if_template[3] = while_action
    if_template[4] = f'JMP -{len(while_action) + 3}' # Current position + next position

    return flatten(if_template)

def _repeat(parg1, parg2, repeat_action):
    """
    parg1 is amount of time to repeat
    parg2 is internal
    """
    if_template = COMMAND_LOOKUP['while']

    if_template[0] = repeat_action
    if_template[1] = f'INC {parg2}' # Current position + next position
    if_template[2] = f'LDA {parg1}' # Current position + next position
    if_template[3] = f'CMP {parg2}' # Current position + next position
    if_template[4] = f'NOT' # Current position + next position
    if_template[5] = f'JEQ -{len(repeat_action) + 4}' # Current position + next position

    return flatten(if_template)

#program = _if_else(0x00, 0x01, ['RAN', 'DIS'], ['RAN', 'DIS'])
#program = _while(0x00, 0x01, ['RAN', 'DIS'])
program = _repeat(0x00, 0x01, ['RAN', 'DIS'])
for index, line in enumerate(program):
    componenets = line.split()
    command = componenets[0]
    if command in ['JEQ', 'JMP']:
        program[index] = f'{command} {(index+1) + int(componenets[1])}'

for i in program:
    print(i)


# Automatically handles memory allocation
