from collections import Counter
import matplotlib.pyplot as plt

def read_seq(filename):
    with open(filename) as f:
        seq = f.read()
    seq = seq.replace('\n', '')
    return seq

def get_com(seq):
    adn = list(seq)
    dic = {'G': 'C', 'T': 'A', 'A': 'T', 'C': 'G'}
    adn = [dic.get(base) for base in adn]
    return adn

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

dic = exercise2b('atoh1.txt')

#plot_bar_graph(list(dic.keys()),list(dic.values()),'Nitrogenous base ocurrence','','')

def exercise2c(filename):
    seq1 = read_seq(filename)


