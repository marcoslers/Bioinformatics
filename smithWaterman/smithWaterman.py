gapPenalty=-2

class Cell:    
    def __init__(self, value,position):
        self.value=value
        self.position=position

    def setVal(self,value): self.value=value

    def setPos(self,position): self.position=position
        
    def getVal(self): return self.value

    def getPos(self): return self.position

#   Matriz de sustitucion
def s(r,c):
    if r==c: return 3
    elif r=='G' and c=='A' or r=='A' and c=='G': return 1
    elif r=='T' and c=='C' or r=='C' and c=='T': return 1
    else: return -1

def read_seq(filename):    
    with open(filename) as f:
        seq = f.read()
    seq = (seq.replace('\n', '')).upper()
    return seq

seq1 = list(read_seq('seq1.txt'))
seq2 = list(read_seq('seq2.txt'))

#   Longitudes de la matriz
lnseq1, lnseq2 = len(seq1)+1, len(seq2)+1

#   Inicializacion de la matriz
M, rows = [],[]
rows = [Cell(0,None) for j in range(lnseq2)]
m = [rows for i in range(lnseq1)]

for i in range (lnseq1):
    for j in range(lnseq2):
        diag = m[i-1][j-1].getVal() +s(seq1[i-1],seq2[j-1])
        up   = m[i-1][j].getVal()-gapPenalty
        left = m[i][j-1].getVal()-gapPenalty
        
