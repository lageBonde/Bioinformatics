from Bio import SeqIO

sizes = [len(rec) for rec in SeqIO.parse("genomes/GCF_024807035.1_ASM2480703v1_genomic.fna", "fasta")]

import matplotlib.pyplot as plt

plt.hist(sizes, bins=20)
plt.title(
    "%i orchid sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes))
)
plt.xlabel("Sequence length (bp)")
plt.ylabel("Count")
plt.savefig("Histogram")
