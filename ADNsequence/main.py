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


def exercise1(filename):
    seq1 = read_seq(filename)
    seq2 = get_com(seq1)
    print(list(seq1), '\n', seq2)
    return


exercise1("atoh1.txt")