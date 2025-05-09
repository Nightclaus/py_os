from memory import RAM

SYS_RAM = RAM()

SYS_RAM.STO([0x01], 0x00)
SYS_RAM.STO('Test Value 1', 0x01)
SYS_RAM.SetPointer(0x09)
SYS_RAM.STO('Test Value 2')
SYS_RAM.SetPointer(0x00)
a = SYS_RAM.LDA()
b = SYS_RAM.LDA(0x09)
print(a)
print(b)