from Bio import SeqIO

records = [rec for rec in SeqIO.parse("own-aligning/1.fna", "fasta")]
gene1 = records[0]

records = [rec for rec in SeqIO.parse("own-aligning/2.fna", "fasta")]
gene2 = records[0]

if len(gene2) > len(gene1):
    temp = gene1
    gene1 = gene2
    gene2 = temp

matches = []
for i in range(len(gene1)):
    base = gene1[i]
    if base = gene[0]:
        