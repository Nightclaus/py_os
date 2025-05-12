# Matches file structure with the ST structure
END = 'hlt'
CONTENT = 'content'
IDENTIFIER = 'IDENTIFIER_'
IDENTIFIER_INCREMENT = 0

COMMAND_LOOKUP = {
    "if": [
        IDENTIFIER,
        "LDA 0x01",
        "CMP 0x00",
        "JEQ 19",
        CONTENT,
        "JMP 21",
        CONTENT,
        END,
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

def if_else(parg1, parg2, true_action, false_action):
    if_template = COMMAND_LOOKUP['if']

    identifier = getIdentfier()

    if_template[0] = identifier

    if_template[1] = f'LDA {parg1}'
    if_template[2] = f'CMP {parg2}'

    if_template[3] = f'JEQ {len(true_action) + 2}' # Current position + next position

    if_template[4] = true_action

    if_template[5] = f'JMP {len(false_action) + 1}' 

    if_template[6] = false_action

    return flatten(if_template)

program = if_else(0x00, 0x01, ['test command'], ['Test command 2'])
for index, line in enumerate(program):
    componenets = line.split()
    command = componenets[0]
    if command in ['JEQ', 'JMP']:
        program[index] = f'{command} {(index+1) + int(componenets[1])}'

for i in program:
    print(i)
# Automatically handles memory allocation
