import sys
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction


AA_SEQ_SOURCE = Seq(open('N_BASE_CODE').read()).reverse_complement().transcribe().translate()

AA_SEQ_GENE = Seq(open('N_BASE_GENE')).reverse_complement().transcribe().translate()


print(AA_SEQ_SOURCE.count(AA_SEQ_GENE))