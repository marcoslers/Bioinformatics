import re
diccionario={   'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
                'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
                'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
                'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
                'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
                'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
                'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
                'CGA':'R','CGC':'R','CGG':'R','CGT':'R',
                'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
                'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
                'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
                'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
                'TCA':'S','TCC':'S','TCG':'S','TCT':'S',    
                'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
                'TAC':'Y','TAT':'Y','TAA':'_','TAG':'_',
                'TGC':'C','TGT':'C','TGA':'_','TGG':'W',}

def read_seq(filename):
    with open(filename) as f:
        seq=f.read()
    seq=seq.replace('\n','')
    seq=seq.upper()
    return seq

def getCodons(rna_m):
    srna_m=''
    srna_m=srna_m.join(rna_m)
    codons=re.findall('[ATGC]{3}',srna_m)
    return codons

def getProtein(codons):
    protein = ''
    for codon in codons:
        protein+=diccionario.get(codon)
    return protein

def exercise2c(filename):
    seq1 = read_seq(filename)
    codons = getCodons(seq1)
    protein = getProtein(codons)
    return protein

print(exercise2c('hiv-1.txt'))