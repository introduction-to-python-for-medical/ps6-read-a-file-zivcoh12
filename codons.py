def create_codon_dict(file_path):
   amino_acid_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            cells = line.strip().split('\t')
            if len(cells) >= 3:
                codon, amino_acid = cells[0], cells[2]
                amino_acid_dict[codon] = amino_acid
    return amino_acid_dict
