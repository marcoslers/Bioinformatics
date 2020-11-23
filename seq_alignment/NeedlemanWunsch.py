import numpy as np

class Cell:    
    def __init__(self, value,pos):
        self.value=value
        self.positions = [pos]
    
    def getValue(self):
        return self.value

    def getPos(self):
       return self.positions 

    def addPos(self,element):
        self.positions.append(element)


def read_seq(filename):    
    with open(filename) as f:
        seq = f.read()
    seq = seq.replace('\n', '')
    seq = seq.upper()
    return seq

def getScore(r,c):
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


seq1 = list(read_seq('seq1.txt'))
seq2 = list(read_seq('seq2.txt'))

nseq1, nseq2 = len(seq1)+1, len(seq2)+1
mtx = np.zeros((nseq1,nseq2),dtype=Cell)
mtx[0][0] = Cell(0,'done')

for i in range(1,nseq1):
    mtx[i][0] = Cell(0,'up')
    mtx[i][1] = Cell(getScore(seq1[i-1],seq2[0]),'diag')

for j in range(1,nseq2):
    mtx[0][j] = Cell(0,'left')
    mtx[1][j] = Cell(getScore(seq1[0],seq2[j-1]),'diag')

for i in range(2,nseq1):
    for j in range(2,nseq2):

        diag = mtx[i-1][j-1].getValue() +getScore(seq1[i-1],seq2[j-1])
        up   = mtx[i-1][j].getValue()-2
        left = mtx[i][j-1].getValue()-2

        mtx[i][j] = getMax(diag,up,left)
        #print(mtx[i][j].getValue(),' ',end='')

i,j=nseq1-1,nseq2-1

top,bot=[],[]

flag=True
while(flag):
    arrow = mtx[i][j].getPos()
    for a in arrow:
        if a == 'up':
            top.insert(0,seq1[i-1])
            bot.insert(0,'-')
            i-=1
        elif a == 'left':
            top.insert(0,'-')
            bot.insert(0,seq2[j-1])
            j-=1
        elif a == 'diag':
            top.insert(0,seq1[i-1])
            bot.insert(0,seq2[j-1])
            i-=1
            j-=1
        elif a == 'done':
            flag=False
        break

print(top)
print(bot)

optval=0
for i in range(len(top)):
    optval+=getScore(top[i],bot[i])
print('\nValor optimo de alineamiento: ',optval)

