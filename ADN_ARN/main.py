from collections import Counter
import matplotlib.pyplot as plt
import re

def read_seq(filename):
    with open(filename) as f:
        seq = f.read()
    seq = seq.replace('\n', '')
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

#print(exercise2a("atoh1.txt"))

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

#dic = exercise2b('atoh1.txt')

#plot_bar_graph(list(dic.keys()),list(dic.values()),'Nitrogenous base ocurrence','','')

codon_table = {'UUU':'PHE','UUC':'PHE','UUA':'LEU','UUG':'LEU',
               'UCU':'SER','UCC':'SER','UCA':'SER','UCG':'SER',
               'UAU':'TYR','UAC':'TYR',
               'UGU':'CYS','UGC':'CYS',
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

def transcription(strand):
    dic = {'G': 'C', 'T': 'A', 'A': 'U', 'C': 'G'}
    rna_m = [dic.get(base) for base in strand]
    return rna_m

def traduction(rna_m):
    srna_m=''
    srna_m=srna_m.join(rna_m)
    codons=re.findall('[AUGC]{3}',srna_m)
    for codon in codons:
        print(codon_table.get(codon),' ',end='')

def exercise2c(filename):
    seq1 = read_seq(filename)
    strand3_5 = get_com(seq1)
    rna_m = transcription(strand3_5)
    rna_t = traduction(rna_m)


exercise2c('atoh1.txt')

