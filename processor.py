from memory import RAM
from random import randint

SYS_RAM = RAM()
commands = {
    'STO': "SYS_RAM.STO",
    'LDA': "SYS_RAM.LDA", ## Loads to register A
    'SET': "SYS_RAM.SetPointer",
    'DIS': "SYS_RAM.print",
    'RGA': "SYS_RAM.STO_REGISTER",
    'JMP': "self.jumpTo",
    'JEQ': "self.jumpIf", ## Jumps only if register A is true
    'CMP': "self.compare", ## Compares Argument with Register A
    'HLT': "return", 
    "GRE": "self.isGreaterThanRegA",
    "LES": "self.isLesserThanRegA",
    "INP": "self.input",
    "ADD": "self.add",
    "RAN": "randint",
}

class Core():
    def __init__(self, commandArray, debug=False):
        self.lines = commandArray
        self.program_counter = 0
        self.LIMIT = len(self.lines)
        self.registerA = 0

        # Enable Debugging
        self.debug = debug
        global SYS_RAM
        SYS_RAM.setDebug(self.debug)

    def printDebug(self, string):
        if self.debug == True:
            print(string)
    
    def run(self):
        while self.program_counter < self.LIMIT:
            line = self.lines[self.program_counter].strip()
            self.program_counter+=1

            if not line or line.startswith('//'):
                continue  # Skip empty lines or comments

            interableLine = line.split(maxsplit=1)
            #opcode = int(interableLine[0], 16)
            opcode = interableLine[0]

            try:
                if opcode in ['DIS', 'RGA']: # Redirect print to use the register
                    args = f'"{self.registerA}"' ## Clean
                elif opcode == "HLT":
                    return
                elif opcode == "RAN": ## Special
                    self.registerA = randint(0, 100)
                    continue
                else:
                    args = interableLine[1] if len(interableLine) > 1 else "" ## Sanitise
                self.registerA = eval(f"{commands[opcode]}({args})")
            except Exception as e:
                print(f"Error: {e}")

    def jumpTo(self, newNumber):
        self.program_counter = newNumber-1
        self.printDebug(f'JUMP TO {newNumber}')
    
    def jumpIf(self, newNumber):
        booleanFromRegisterA = self.registerA
        if booleanFromRegisterA == True:
            self.jumpTo(newNumber)
    
    def compare(self, pointerArg):
        arg = str(SYS_RAM.LDA(pointerArg))
        regA = str(self.registerA)
        if arg == regA:
            self.registerA = True
            self.printDebug(f'CMP [ {arg} is equal to {regA} ] => True')
            return True
        else:
            self.printDebug(f'COMPARE [ {arg} is NOT equal to {regA} ] => False')
            return False
    
    def add(self, pointerArg): ## CHECK THIS
        try:
            return int(SYS_RAM.LDA(pointerArg)) + int(self.registerA)
        except:
            print('[Cannot Add] Expected type INT')
            return False
    
    def isGreaterThanRegA(self, pointerArg):
        arg = str(SYS_RAM.LDA(pointerArg))
        try:
            if int(self.registerA) < int(arg):
                return True
            return False
        except:
            print('[Cannot Compare] Expected type INT')
            return False
    
    def isLesserThanRegA(self, pointerArg):
        arg = str(SYS_RAM.LDA(pointerArg))
        try:
            if int(self.registerA) > int(arg):
                return True
            return False
        except:
            print('[Cannot Compare] Expected type INT')
            return False
    
    def input(self, text=''):
        return input(text)
