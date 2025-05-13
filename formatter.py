# Matches file structure with the ST structure
END = 'HLT'
CONTENT = 'content'

COMMAND_LOOKUP = {
    "if": [
        "LDA 0x01",
        "CMP 0x00",
        "JEQ 19",
        CONTENT,
        "JMP 21",
        CONTENT,
        ],
    "while": [
        "LDA 0x01",
        "CMP 0x00",
        "JEQ 19",
        CONTENT,
        "JMP START_WHILE_1",
    ],
    "repeat": [
        CONTENT,
        "INC 0x03",
        "LDA 0x02",  # Pointer for arg 1
        "NCP 0x03",   # Pointer for arg 2
        "JEQ START_REPEAT_1",
    ],
}

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # recurse into sublist
        else:
            result.append(item)
    return result

def IfElse(parg1, parg2, true_action, false_action, mode='=='):
    operator = {
        '==': 'CMP',
        '>': "GRE", 
        '<': "LES",
        '!=': "NCP"
    }[mode]
    if_template = COMMAND_LOOKUP['if']

    if_template[0] = f'LDA {parg1}'
    if_template[1] = f'{operator} {parg2}'
    if_template[2] = f'JEQ {len(false_action) + 2}' # Current position + next position
    if_template[3] = false_action                   # Unoptimised, does not discard vestigal jump for non-else Ifs
    if_template[4] = f'JMP {len(true_action) + 1}' 
    if_template[5] = true_action

    return flatten(if_template)

def While(parg1, parg2, while_action):
    if_template = COMMAND_LOOKUP['while']

    if_template[0] = f'LDA {parg1}'
    if_template[1] = f'NCP {parg2}'
    if_template[2] = f'JEQ {len(while_action) + 2}' # Current position + next position
    if_template[3] = while_action
    if_template[4] = f'JMP -{len(while_action) + 3}' # Current position + next position

    return flatten(if_template)

def Repeat(parg1, parg2, repeat_action):
    """
    parg1 is amount of times to repeat
    parg2 is internal
    """
    if_template = COMMAND_LOOKUP['repeat']

    if_template[0] = repeat_action
    if_template[1] = f'INC {parg2}'
    if_template[2] = f'LDA {parg1}' 
    if_template[3] = f'NCP {parg2}' 
    if_template[4] = f'JEQ -{len(repeat_action) + 3}'

    return flatten(if_template)