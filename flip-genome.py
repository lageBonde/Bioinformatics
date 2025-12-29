import sys

file = open("/workspaces/Bioinformatics/"+sys.argv[1])
code = file.read()
file.close()
code = code[::-1]
open("/workspaces/Bioinformatics/"+sys.argv[1], 'w').write(code)