import sys
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from colorama import Fore, Back, Style


def PrintWithMismatch(code):
    print("hejhej")
    for l in code:
        if l.islower():
            print(Back.RED + l.upper() + Style.RESET_ALL, end="")
        else:
            print(l, end="")


AA_SEQ_SOURCE = Seq(open('N_BASE_CODE').read())

AA_SEQ_GENE = Seq(open('N_BASE_GENE').read())

for i in range(len(AA_SEQ_SOURCE)):
    if AA_SEQ_SOURCE[i] == AA_SEQ_GENE[0]:
        mismatch = 0
        out = ""
        for k in range(len(AA_SEQ_GENE)):
            if AA_SEQ_GENE[k] != AA_SEQ_SOURCE[i+k]:
                out += str(AA_SEQ_SOURCE[i+k]).lower()
                
                mismatch += 1
            else:
                out += AA_SEQ_SOURCE[i+k]
            if mismatch >= 10:
                break
        if mismatch < 10:
            print("Mismatch:\t",mismatch)
            print("AA_SEQ_SOURCE:\n")
            PrintWithMismatch(out)
            
            print("\n\n")
            print("AA_SEQ_GENE:\n",AA_SEQ_GENE)
            print("---------------\n\n")