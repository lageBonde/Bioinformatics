from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import textwrap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


records = [rec for rec in SeqIO.parse("genomes/GCF_024807035.1_ASM2480703v1_genomic.fna", "fasta")]

import matplotlib.pyplot as plt


def generate_y_1(n):
    CHUNKS = int(len(seq)/n)

    ypoints = np.array([])

    for chunk in textwrap.wrap(str(seq.seq),CHUNKS):
        ypoints = np.append(ypoints,gc_fraction(chunk))
    return ypoints

def generate_y_2():
    ypoints = np.array([])

    try:
        for i in range(len(seq)):
            ypoints = np.append(ypoints,gc_fraction(seq.seq[i:i+10**5]))
    except :
        pass
    return ypoints

def generate_y_3(chunk_length):
    ypoints = np.array([])

    try:
        for i in range(int(len(seq)/chunk_length)):
            ypoints = np.append(ypoints,gc_fraction(seq.seq[chunk_length*i:chunk_length*i+chunk_length]))
    except :
        pass
    return ypoints

'''
for i in range(3,-1,-1):
    ypoints = generate_y_1()
    xpoints = np.array(range(
        0,
        int(len(seq)/len(ypoints))*len(ypoints),
        int(len(seq)/len(ypoints))
    ))
    plt.plot(xpoints, ypoints)
'''

chunk_lengths = [10000,15000,20000]

for chunk_length in chunk_lengths:
    seq = records[3]

    ypoints = generate_y_3(chunk_length)
    xpoints = np.array(range(
        0,
        int(len(seq)/len(ypoints))*len(ypoints),
        int(len(seq)/len(ypoints))
    ))
    plt.plot(xpoints, ypoints)
    print("Sequence length\t", len(seq))

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig("Histogram")
