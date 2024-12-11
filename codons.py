def create_codon_dict(file_path):
    codon_to_aa = {}
    with open(file_path, 'r') as file:
        rows = file.readlines()
        for row in rows:
          parts = row.strip().split('\t')
          codon = parts[0]
          amino_acid = parts[2]
          codon_to_aa[codon] = amino_acid
    return codon_to_aa
