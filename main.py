import gzip
from Bio import SeqIO

file_path = 'gbbct100.seq.gz'

snippet_length = 50

with gzip.open(file_path, 'rt') as handle:
    for record in SeqIO.parse(handle, 'genbank'):
        seq_id = record.id
        seq = record.seq
        
        print(f"ID: {seq_id}")
        print(f"Sequence snippet: {seq[:snippet_length]}")

        if len(seq) >= snippet_length:
