import numpy as np

gapPenalty=-2

class Cell:    
    def __init__(self, value,position):
        self.value=value
        self.position=position
    
    def getVal(self):
        return self.value

    def getPos(self):
        return self.position

def s(r,c):
    if r==c:
        return 3
    elif r=='-' or c=='-':
        return -2
    elif r=='G' and c=='A' or r=='A' and c=='G':
        return 1
    elif r=='T' and c=='C' or r=='C' and c=='T':
        return 1
    else: 
        return -1

def getMax(diag,up,left):
    if diag > up and diag > left:
        c = Cell(diag,'diag')
    elif up > diag and up >left:
        c = Cell(up,'up')
    elif left > diag and left>up:
        c = Cell(left,'left')
    elif diag == up and diag > left:
        c = Cell(diag,'diag')
        c.addPos('up')
    elif diag == left and diag >up:
        c=Cell(diag,'diag')
        c.addPos('left')
    elif left==up and left>diag:
        c=Cell(left,'left')
        c.addPos('up')
    else:
        c=Cell(diag,'diag')
        c.addPos('up')
        c.addPos('left')
    return c

def read_seq(filename):    
    with open(filename) as f:
        seq = f.read()
    seq = seq.replace('\n', '')
    seq = seq.upper()
    return seq


seq1 = list(read_seq('seq1.txt'))
seq2 = list(read_seq('seq2.txt'))


lnseq1, lnseq2 = len(seq1)+1, len(seq2)+1
m = np.zeros((lnseq1,lnseq2),dtype=Cell)


#   Llenado de 0's primera fila y columna 
#   m[i][0] = m[0][j] = 0

for i in range(1,lnseq1):
    m[i][0] = Cell(0,None)

for j in range(1, lnseq2):
    m[0][j] = Cell(0,None)


#   Llenado de 

for i in range(1,lnseq1):
    for j in range(1,lnseq2):
        diag = m[i-1][j-1].getVal() +s(seq1[i-1],seq2[j-1])
        up   = m[i-1][j].getVal()-gapPenalty
        left = m[i][j-1].getVal()-gapPenalty
        
        
        max(diag,up,left,0)
