import numpy
import matplotlib.pyplot as plt

def delta(x,y):
    return 0 if x == y else 1

def M(seq1,seq2,i,j,k):
    return sum(delta(x,y) for x,y in zip(seq1[i:i+k],seq2[j:j+k]))

def makeMatrix(seq1,seq2,k):
    n = len(seq1)
    m = len(seq2)
    return [[M(seq1,seq2,i,j,k) for j in range(m-k+1)] for i in range(n-k+1)]


def read_seq(filename,n):    
    with open(filename) as f:
        seq = f.read(n)
    seq = seq.replace('\n', '')
    seq = seq.upper()
    return seq



seqx = read_seq('atoh1.txt',20)
seqy = read_seq('hiv-1.txt',20)

print(seqx,seqy)
dotplot=plt.imshow(numpy.array(makeMatrix(seqx,seqy,1)))
xt=plt.xticks(numpy.arange(len(list(seqx))),list(seqx))
yt=plt.yticks(numpy.arange(len(list(seqy))),list(seqy))
plt.show()
