from Bio import SeqIO

class Relation:
    def __init__(self, seq_original, seq_record):
        self.seq_original = seq_original
        self.seq_record = seq_record
        
        self.start = None
        self.mismatches = [] # Mismatch element: [start,end] in relation to self.start

def Check_Record(seq_original, seq_record):
    relation = Relation(seq_original, seq_record)

    i = 0
    while True:
        print(i, "\t/ ", len(seq_original),end="\r")
        i+=1
        if i > len(seq_original):
            break

        if seq_original[i] == seq_record[0]: # Something's similar?
            mismatches = []
            new_mismatch = None
            quantity_mismatch = 0
            for k in range(len(seq_record)):
                if seq_original[i+k] != seq_record[k]:
                    quantity_mismatch += 1
                    if quantity_mismatch > k*0.7:
                        quantity_mismatch = len(seq_record)
                        break
                if seq_original[i+k] != seq_record[k] and new_mismatch == None:
                    new_mismatch = [k]
                elif seq_original[i+k] == seq_record[k] and new_mismatch != None:
                    new_mismatch.append(k)
                    mismatches.append(new_mismatch)
                    new_mismatch = None
            if quantity_mismatch < len(seq_record)/2:
                relation.start = i
                relation.mismatches = mismatches
                return relation
    return None

seq = [record for record in SeqIO.parse("/workspaces/Bioinformatics/genomes/GCF_024807035.1_ASM2480703v1_genomic.fna", "fasta")]

print(
    Check_Record(seq[0], seq[1])
)