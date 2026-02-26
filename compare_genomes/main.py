from Bio import SeqIO
from Bio.Seq import Seq
import numpy as np

aa_seq_16790_recs = [rec.seq.transcribe().translate() for rec in SeqIO.parse("/workspaces/Bioinformatics/compare_genomes/GCA_000009185.1_ASM918v1_genomic.fna", "fasta")]
aa_seq_D2T01_recs = [rec.seq.transcribe().translate() for rec in SeqIO.parse("/workspaces/Bioinformatics/compare_genomes/GCA_903989505.1_D2T2_genomic.fna", "fasta")]

aa_seq_16790 = aa_seq_16790_recs[0]

found = 0
missing = 0

while True:
    # Get gene
    try: 
        start = aa_seq_16790.index("M")
        aa_seq_16790 = aa_seq_16790[start:]
        stop = aa_seq_16790.index("*")
    except ValueError: 
        break
    
    gene = aa_seq_16790[1:stop] # Without M and *

    aa_seq_16790 = aa_seq_16790[stop:]

    isfound = False
    for aa_seq in aa_seq_D2T01_recs:
        if gene in aa_seq:
            isfound = True
    
    if isfound:
        found += 1
    else:
        missing += 1

    
print(f"Found {found}")
print(f"Missing {missing}")