# Import functions
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# The test
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

