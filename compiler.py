from formatter import IfElse, Print, Repeat, While, flatten

def finalise_jumps_in_context(program):
    for index, line in enumerate(program):
        line_components = line.split()
        command = line_components[0]
        if command in ['JEQ', 'JMP']:
            program[index] = f'{command} {(index+1) + int(line_components[1])}'
    return program

# Examples
#program = IfElse(0x00, 0x01, ['RAN', 'DIS'], ['RAN', 'DIS'])
#program = While(0x00, 0x01, ['RAN', 'DIS'])
#program = finalise_jumps_in_context(Repeat(0x00, 0x01, ['RAN', 'DIS']))

with open('pre_compiled_test.st') as file:
    output = []
    lines = [line.strip('\n') for line in file.readlines()]
    for line in lines:
        if line == '':
            continue
        line = line.split()
        command = line[0].lower()
        match command:
            case 'set':
                output.append([
                    f'SET {line[1]}',
                    f'STO {line[3]}'
                ])
            case 'if':
                output.append([
                    IfElse(line[1], line[3], Print(line[1]), []) # Hardcoded for now
                ])

    output = finalise_jumps_in_context(flatten(output))
    output.append('HLT')
    for i in output:
        print(i)
    


#for i in program:
#    print(i)

# Automatically handles memory allocation
