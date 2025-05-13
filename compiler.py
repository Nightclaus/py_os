from formatter import IfElse, Print, Repeat, While, flatten

# TODO Get Print, Repeat, While into the thing
# TODO Get the auto variable assigment table done

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

def deconstruct(lines):
    output = []
    LINE_COMPLETED = 0
    LIMIT = len(lines)
    while LINE_COMPLETED < LIMIT:
        line = lines[LINE_COMPLETED]
        LINE_COMPLETED += 1
        if line == '':
            continue
        line = line.split()
        command = line[0].lower()
        if command in ["endif", "endwhile", "endfor"]:
            return output, LINE_COMPLETED
        match command: # else
            case 'set':
                output += [
                    f'SET {line[1]}',
                    f'STO {line[3]}'
                ]
            case 'print':
                output += [
                    f'LDA {line[1]}',
                    f'DIS'
                ]
            case 'if':
                nested_lines, completed_lines = deconstruct(lines[LINE_COMPLETED:])
                LINE_COMPLETED += completed_lines ## Skip the lines that have been done in the for loop
                output += [
                    IfElse(line[1], line[3], nested_lines, []) # Hardcoded for now
                ]
    return flatten(output)

compiled = []
with open('pre_compiled_test.st') as file:
    lines = [line.strip('\n') for line in file.readlines()]
    compiled = finalise_jumps_in_context(deconstruct(lines))
    compiled.append('HLT')

with open('template.st', 'w') as file:
    file.writelines("\n".join(compiled))
    


#for i in program:
#    print(i)

# Automatically handles memory allocation
