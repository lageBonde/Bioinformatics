from Bio import SeqIO
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import sys

def base_to_gc_percentage(base):
    if base.lower() == "g" or base.lower() == "c":
        return 1
    return 0

records = [record for record in SeqIO.parse("/workspaces/Bioinformatics/genomes/GCF_024807035.1_ASM2480703v1_genomic.fna", "fasta")]

range_ = 1000
mu = range_/2
sigma = 500

normal_dist = scipy.stats.norm.pdf(
    np.array([i for i in range(range_)]),
    mu,
    sigma
)

plt.text(0,1.05, 'GCF_024807035.1_ASM2480703v1_genomic, record '+sys.argv[1], transform=plt.gca().transAxes)

plt.plot(
    np.convolve(
        [base_to_gc_percentage(base) for base in records[
            int(sys.argv[1])
        ].seq],
        normal_dist,
        mode="valid"
    )
)
plt.xlabel("bp", fontsize="15")
plt.ylabel("%GC", fontsize="15")

plt.show()
plt.savefig("Convolution")