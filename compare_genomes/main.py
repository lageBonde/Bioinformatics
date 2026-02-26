from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Align
import numpy as np
import matplotlib.pyplot as plt

aa_seq_16790_recs = [rec.seq.transcribe().translate() for rec in SeqIO.parse("/workspaces/Bioinformatics/compare_genomes/GCA_000009185.1_ASM918v1_genomic.fna", "fasta")]
aa_seq_D2T01_recs = [rec.seq.transcribe().translate() for rec in SeqIO.parse("/workspaces/Bioinformatics/compare_genomes/GCA_903989505.1_D2T2_genomic.fna", "fasta")]

aa_seq_16790 = aa_seq_16790_recs[0]

aa_seq_D2T01_array = np.concatenate([
    str(rec).split("*") for rec in aa_seq_D2T01_recs
])

aa_seq_D2T01_array = [fragment for fragment in aa_seq_D2T01_array if fragment != ""]

matches = np.array([])

aligner = Align.PairwiseAligner()

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

    for aa_seq in aa_seq_D2T01_array:
        best_match = 0
        for fragment in aa_seq_D2T01_array:
            alignment = aligner.score(fragment,aa_seq)
            if alignment > best_match:
                best_match = alignment
        matches = np.append(matches,best_match)

plt.plot(range(len(matches)),matches)
plt.savefig("Comparision")