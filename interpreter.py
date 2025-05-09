from processor import Core
import sys
filename = sys.argv[1]

if not filename.endswith('.st'):
    raise ValueError("Only .st files are supported!")

with open(filename, 'r') as file:
    lines = file.readlines()
    CORE = Core(lines, False)
    CORE.run()
