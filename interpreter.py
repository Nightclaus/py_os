from processor import Core
import sys
filename = sys.argv[1]

if filename.endswith('.st'):
    with open(filename, 'r') as file:
        lines = file.readlines()
        CORE = Core(lines, False)
        CORE.run()
else:
    with open(filename) as file:
        code = file.read()
        exec(code)
