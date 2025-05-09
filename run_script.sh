#!/bin/bash
SCRIPT=$1

python3 -c "
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath('$0')))
from processor import Core
with open('$SCRIPT') as f:
    lines = f.readlines()
Core(lines).run()
"

# alias cst='python3 -c "from processor import Core; import sys; lines=open(sys.argv[1]).readlines(); Core(lines).run()"'
