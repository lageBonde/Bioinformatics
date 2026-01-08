from Bio import SeqIO
from Bio import Blast
import xml.etree.ElementTree as ET
'''
records = [record for record in SeqIO.parse("/workspaces/Bioinformatics/genomes/input", "fasta")]
record = records[0]

result_stream = Blast.qblast("blastn", "nt", format(record, "fasta"))

with open("my_blast.xml", "wb") as out_stream:
    out_stream.write(result_stream.read())
'''
records = Blast.read("my_blast.xml")


print(records.query.description)

for record in records[:1]:
    print(record[0].annotations["evalue"])