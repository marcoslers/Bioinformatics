from collections import Counter
#import matplotlib.pyplot as plt
import re

def read_seq(filename):    
    with open(filename) as f:
        seq = f.read()
    seq = seq.replace('\n', '')
    seq = seq.upper()
    return seq

def get_com(seq):
    dna = list(seq)
    dic = {'G': 'C', 'T': 'A', 'A': 'T', 'C': 'G'}
    dna = [dic.get(base) for base in dna]
    return dna

def exercise2a(filename):
    seq1 = read_seq(filename)
    seq2 = get_com(seq1)
    return seq2

#print(exercise2a('hiv-1.txt'))

def plot_bar_graph(names,values,title,xlbl,ylbl):
    plt.bar(names,values)
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.show()

def exercise2b(filename):
    seq = read_seq(filename)
    dic = Counter(list(seq))
    return dic

dic = exercise2b('hiv-1.txt')

#print(dic)

#plot_bar_graph(list(dic.keys()),list(dic.values()),'Nitrogenous base ocurrence','','')

codon_table = {'UUU':'PHE','UUC':'PHE','UUA':'LEU','UUG':'LEU',
               'UCU':'SER','UCC':'SER','UCA':'SER','UCG':'SER',
               'UAU':'TYR','UAC':'TYR','UAA':'UAA','UAG':'UAG',
               'UGU':'CYS','UGC':'CYS','UGG':'TRP','UGA':'UGA',
               'CUU':'LEU','CUC':'LEU','CUA':'LEU','CUG':'LEU',
               'CCU':'PRO','CCC':'PRO','CCA':'PRO','CCG':'PRO',
               'CAU':'HIS','CAC':'HIS','CAA':'GLN','CAG':'GLN',
               'CGU':'ARG','CGC':'ARG','CGA':'ARG','CGG':'ARG',
               'AUU':'ILE','AUC':'ILE','AUA':'ILE','AUG':'MET',
               'ACU':'THR','ACC':'THR','ACA':'THR','ACG':'THR',
               'AAU':'ASN','AAC':'ASN','AAA':'LYS','AAG':'LYS',
               'AGU':'SER','AGC':'SER','AGA':'ARG','AGG':'ARG',
               'GUU':'VAL','GUC':'VAL','GUA':'VAL','GUG':'VAL',
               'GCU':'ALA','GCC':'ALA','GCA':'ALA','GCG':'ALA',   
               'GAU':'ASP','GAC':'ASP','GAA':'GLU','GAG':'GLU',
               'GGU':'GLY','GGC':'GLY','GGA':'GLY','GGG':'GLY'}

amino_acids_table ={'ALA':'A','CYS':'C','ASP':'D','GLU':'E','PHE':'F',
                    'GLY':'G','HIS':'H','ILE':'I','LYS':'K','LEU':'L',
                    'MET':'M','ASN':'N','PRO':'P','GLN':'Q','ARG':'R',
                    'SER':'S','THR':'T','VAL':'V','TRP':'W','TYR':'Y'}


def transcription(strand):
    dic = {'G': 'C', 'T': 'A', 'A': 'U', 'C': 'G'}
    rna_m = [dic.get(base) for base in strand]
    return rna_m

def traduction(rna_m):
    srna_m=''
    srna_m=srna_m.join(rna_m)
    codons=re.findall('[AUGC]{3}',srna_m)
    return codons

def get_aminoacids(codons):
    aminoacids=[]
    for codon in codons:
        s = codon_table.get(codon)
        aminoacids.append(s)

    return aminoacids

def get_proteins(aminoacids):
    protein=''
    proteins=[]
    for amn in aminoacids:
        if  amn=='UAA' or amn=='UAG' or amn=='UGA':
            proteins.append(protein)
            protein=''
        else:
            protein+=amino_acids_table.get(amn)    
    return proteins

def exercise2c(filename):
    seq1 = read_seq(filename)
    strand3_5 = get_com(seq1)
    rna_m = transcription(strand3_5)
    codons = traduction(rna_m)
    aminoacids = get_aminoacids(codons)
    proteins = get_proteins(aminoacids)
    return proteins
    
print(exercise2c('hiv-1.txt'))

