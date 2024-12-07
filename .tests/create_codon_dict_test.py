from codons import create_codon_dict

def test_create_codon_dict():
    result = create_codon_dict("data/codons.txt")

    assert result['AAA'] == 'K', "Test Failed: 'AAA' should map to 'K'"
    assert result['AAC'] == 'N', "Test Failed: 'AAC' should map to 'N'"

    assert result['ACA'] == 'T', "Test Failed: 'ACA' should map to 'T'"
    assert result['ACC'] == 'T', "Test Failed: 'ACC' should map to 'T'"
