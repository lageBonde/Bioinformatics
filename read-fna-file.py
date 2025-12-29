import sys
from Bio.Seq import Seq

file = open("/workspaces/Bioinformatics/genomes/"+sys.argv[1]).read()

# Remove first line, newlines and all unneccessary genomes
code = ''
for line in file.split('>')[int(sys.argv[2])+1].split('\n'):
    if len(line) != 0 and  ',' not in line:
        code += line

if len(code) % 3 != 0:
    print(Seq(code)[0:-(len(code) % 3)], end="")
else:
    print(Seq(code), end="")