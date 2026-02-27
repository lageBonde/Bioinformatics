from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Align
import numpy as np
import math, re, csv
import matplotlib.pyplot as plt

seq_16790_recs = [rec.seq for rec in SeqIO.parse("/workspaces/Bioinformatics/compare_genomes/GCA_000009185.1_ASM918v1_genomic.fna", "fasta")]
seq_D2T01_recs = [rec.seq for rec in SeqIO.parse("/workspaces/Bioinformatics/compare_genomes/GCA_903989505.1_D2T2_genomic.fna", "fasta")]

def splitByTATABoxes(seq):
    seq_str = str(seq)
    motif = "TATA[AT]A[AT]"

    return re.split(motif,seq_str)

def main():
    genes = splitByTATABoxes(seq_16790_recs[0])

    aligner = Align.PairwiseAligner()

    results = []
    done = 0
    for gene in genes:
        try:
            results.append(
                aligner.score(seq_D2T01_recs,gene)
            )
        except ValueError:
            pass
        print(round(done/len(genes)*100,3), "%", end="\r")
        done += 1
    plt.plot(range(len(results)),results)
    plt.savefig("bysearch_tata")

    with open('bysearch_tata.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(
            [
                [
                    [i,results[i]] for i in range(len(results))
                ]
            ]
        )

main()