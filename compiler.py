from formatter import IfElse, Print, Repeat, While, flatten

# TODO Get Print, Repeat, While into the thing
# TODO Add NCP (Not compare)

def finalise_jumps_in_context(program):
    for index, line in enumerate(program):
        line_components = line.split()
        command = line_components[0]
        if command in ['JEQ', 'JMP']:
            program[index] = f'{command} {(index+1) + int(line_components[1])}'
    return program

# Automatically handles memory allocation
currentMemory = 0 # Reserve 0x00
def getFreeMemory():
    global currentMemory
    currentMemory+=1
    return hex(currentMemory)

variable_map = {}

def deconstruct(lines):
    global variable_map
    output = []
    LINE_COMPLETED = 0
    LIMIT = len(lines)
    while LINE_COMPLETED < LIMIT:
        line = lines[LINE_COMPLETED]
        LINE_COMPLETED += 1
        HAS_VARIABLE = False
        if line == '' or line.startswith('##'):
            continue
        line = line.split()
        command = line[0].lower()
        for index, part in enumerate(line):
            if part in variable_map:
                line[index] = variable_map[part]
                HAS_VARIABLE = True
        if command in ["endif", "endwhile", "endfor"]:
            return output, LINE_COMPLETED
        match command: # else
            case 'set':
                allocated_memory = getFreeMemory()
                variable_map[line[1]] = allocated_memory
                output += [
                    f'SET {allocated_memory}',
                    f'STO {line[3]}'
                ]
            case 'print':
                ## Do different if it is a variable or not
                if HAS_VARIABLE:
                    output += [
                        f'LDA {line[1]}',
                        f'DIS'
                    ]
                else:
                    output += [
                        f'SET 0x00',
                        f'STO {" ".join(line[1:])}',
                        f'DIS'
                    ]
            case 'end':
                output += [
                    'HLT'
                ]
            case 'input':
                allocated_memory = getFreeMemory()
                variable_map[" ".join(line[:len(line)-2:-1])] = allocated_memory
                output += [
                    f'SET {allocated_memory}',
                    f'INP {" ".join(line[1:len(line)-2])}',
                    'RGA'
                ]
            case 'randint':
                allocated_memory = getFreeMemory()
                variable_map[line[1]] = allocated_memory
                output += [
                    f'SET {allocated_memory}',
                    'RAN',
                    'RGA'
                ]
            case 'if':
                nested_lines, completed_lines = deconstruct(lines[LINE_COMPLETED:])
                LINE_COMPLETED += completed_lines ## Skip the lines that have been done in the for loop
                output += [
                    IfElse(line[1], line[3], flatten(nested_lines), [], line[2])
                ]
            case 'while':
                nested_lines, completed_lines = deconstruct(lines[LINE_COMPLETED:]) 
                LINE_COMPLETED += completed_lines ## Skip the lines that have been done in the for loop
                output += [
                    While(line[1], line[3], flatten(nested_lines)) ## Not sure why i hvae to flatten again but yeah
                ]
    return flatten(output)

compiled = []
with open('pre_compiled_test.st') as file:
    lines = [line.strip('\n') for line in file.readlines()]
    compiled = finalise_jumps_in_context(deconstruct(lines))
    compiled.append('HLT')

with open('template.st', 'w') as file:
    file.writelines("\n".join(compiled))