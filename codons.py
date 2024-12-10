def create_codon_dict(file_path):
  path = "/content/data/codons.txt"
  file = open(path)
  rows = file.readlines()
  file.close()
  mapping= {}
  for row in rows:
    row = row.strip().split('\t')
    codon = row[0]
    amino_acid = row[2]
    mapping[codon] = amino_acid
  return mapping


