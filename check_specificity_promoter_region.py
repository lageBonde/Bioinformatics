import numpy as np

data = """

gtcgac aagcttatcg atgactttat
     1321 tagaggcagt gtttatatac cataaacgtc aaaagtcatt tttataactg gatctcaaaa
     1381 tacctataaa cccattgttc ttctctttta gctctaagaa caatcaattt ataaatatat
     1441 ttattattat gctataatat aaatactata taaatacatt taccttttta taaatacatt
     1501 tacctttttt ttaatttgca tgattttaat gcttatgcta tcttttttat ttagtccata
     1561 aaacctttaa aggacctttt cttatgggat atttatattt tcctaacaaa gcaatcggcg
     1621 tcataaactt tagttgctta cgacgcctgt ggacgtcccc cccttcccct tacgggcaag
     1681 taaacttagg gattttaatg caataaataa atttgtcctc ttcgggcaaa tgaattttag
     1741 tatttaaata tgacaagggt gaaccattac ttttgttaac aagtgatctt accactcact
     1801 atttttgttg aattttaaac ttatttaaaa ttctcgagaa agattttaaa aataaacttt
     1861 tttaatcttt tatttatttt ttctttttta tggcaatgcg tactccagaa gaacttagta
     1921 atcttattaa agatttaatt gaacaataca ctccagaagt gaaaatgtcc

"""

data = "".join([c for c in data if c in "atgc"])

def to_nucleotide_seq(seq):
    return "".join([
        "a" if i=='0' else "t" if i=='1' else "g" if i=='2' else "c" if i=='3' else "" for i in np.base_repr(seq, base=4) 
    ])

force_seq = 0
force_shooting = []

print("Copies\tSequence")

while True:
    nucleotide_seq = to_nucleotide_seq(force_seqseq)
    
    if len(nucleotide_seq) > 5:
        break
    
    copies = data.count(nucleotide_seq)

    if copies >= 4:
        force_shooting.append([nucleotide_seq,copies])
    seq += 1

