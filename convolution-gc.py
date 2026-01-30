from Bio import SeqIO
from numpy import convolve

def base_to_gc_percentage(base):
    if base.lower() == "g" or base.lower() == "c":
        return 1
    return 0

records = [record for record in SeqIO.parse("/workspaces/Bioinformatics/genomes/GCF_024807035.1_ASM2480703v1_genomic.fna", "fasta")]
print(records[0].seq[0:10])

convolve(
    [base_to_gc_percentage(base) for base in records[0].seq],
    [0,]# normal dist...........
)

# matplot