from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Align

histone_h3 = [rec for rec in SeqIO.parse(
    "histone_h3.fna",
    "fasta"
)]

cenp_a = [rec for rec in SeqIO.parse(
    "cenp_a.fna",
    "fasta"
)]



aligner = Align.PairwiseAligner()

alignments = aligner.align(cenp_a[0].seq.transcribe().translate(),histone_h3[1].seq.transcribe().translate())

print(alignments[0])


seq1 = Seq("AATTGGAATTGGAATTGG")
seq2 = Seq("AATTGGAATTGGAATTGG")

print(aligner.align(seq1,seq2).score)