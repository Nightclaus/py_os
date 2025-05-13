from formatter import IfElse, Print, Repeat, While

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
program = finalise_jumps_in_context(Repeat(0x00, 0x01, ['RAN', 'DIS']))

for i in program:
    print(i)

# Automatically handles memory allocation
