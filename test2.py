from Bio import SeqIO
from Bio import Blast
import xml.etree.ElementTree as ET

#records = [record for record in SeqIO.parse("/workspaces/Bioinformatics/genomes/input", "fasta")]
#record = records[0]

#result_stream = Blast.qblast("blastn", "nt", format(record, "fasta"))

#with open("my_blast.xml", "wb") as out_stream:
#    out_stream.write(result_stream.read())


tree = ET.parse('my_blast.xml')
root = tree.getroot()

#for child in root.findall("BlastOutput_iterations")[0].findall("Iteration")[0].findall("Iteration_hits")[0]:
#    print(child)

#hsp_rankings = [int(rank.text) for rank in root.iter("Hsp_score")]

for child in root.iter("Hit"):
    name = child.findall("Hit_def")[0].text
    #name = name[0:name.index(',')]
    hsp_score = child.find("Hit_hsps").find("Hsp").find("Hsp_score").text
    print(hsp_score + "\t" + name)