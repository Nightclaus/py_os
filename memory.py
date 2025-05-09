class RAM():
    def __init__(self, debug=False):
        self.storage={}
        self.pointer=0x00
        self.debug = debug
    
    def setDebug(self, mode):
        self.debug=mode
    
    def printDebug(self, string):
        if self.debug == True:
            print(string)
    
    def STO(self, value, address=None): # Store
        if address is None:
            address=self.pointer
        self.storage[address] = value
        self.printDebug(f'STO `{value}` => {hex(address)}')
        return value
    
    def LDA(self, address=None, avoidIndirect=False): # Load
        if address is None:
            address=self.pointer
        if address in self.storage:
            DATA_BUFFER = self.storage[address]
            if isinstance(DATA_BUFFER, list):
                self.printDebug(f'Redirected {hex(address)} to {hex(DATA_BUFFER[0])}')
                DATA_BUFFER_2 = self.LDA(DATA_BUFFER[0])
                return DATA_BUFFER_2
            else:
                self.printDebug(f'LDA {hex(address)} => `{DATA_BUFFER}`')
                return DATA_BUFFER
        else:
            self.printDebug(f'LDA {hex(address)} => None')
            return None
    
    def SetPointer(self, newAdress):
        self.printDebug(f'SET pointer TO {hex(newAdress)}')
        self.pointer=newAdress
        return newAdress
    
    def print(self, register):
        print(f'[Display] {register}')
        return register
    
    def STO_REGISTER(self, registerA):
        self.storage[self.pointer] = registerA
        return registerA