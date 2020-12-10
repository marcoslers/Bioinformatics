gapPenalty=2

class Cell:    
    def __init__(self, value,direction):
        self.value=value
        self.direction=direction
      
class MaxValue:
        def __init__(self,value,i,j):
            self.value = value
            self.i=i
            self.j=j

#   Matriz de sustitucion
def s(r,c):
    if r==c: return 3
    elif r=='G' and c=='A' or r=='A' and c=='G': return 1
    elif r=='T' and c=='C' or r=='C' and c=='T': return 1
    else: return -1


def getMax(diag,up,left):
    if diag>up and diag>left: c = Cell(diag,'diag')
    elif up>diag and up>left: c = Cell(up,'up')
    elif left>diag and left>up: c = Cell(left,'left')
    elif diag == up and diag > left:
        c = Cell(diag,'diag')
        #c.addPos('up')
    elif diag == left and diag >up:
        c=Cell(diag,'diag')
        #c.addPos('left')
    elif left==up and left>diag:
        c=Cell(left,'left')
        #c.addPos('up')
    else:
        c=Cell(diag,'diag')
        #c.addPos('up')
        #c.addPos('left')
    return c

def read_seq(filename):    
    with open(filename) as f:
        seq = f.read()
    seq = (seq.replace('\n', '')).upper()
    return seq

#   Lectura de archivos
seq1 = list(read_seq('seq1.txt'))
seq2 = list(read_seq('seq2.txt'))

#   Longitudes de la matriz
lnseq1, lnseq2 = len(seq1)+1, len(seq2)+1

#   Creacion de la matriz de objetos Cell
M, rows = [],[]
M = [[Cell(0,None) for j in range(lnseq2)] for i in range(lnseq1)] 

maxv = MaxValue(0,0,0)

for i in range (1,lnseq1):
    for j in range(1,lnseq2):
        
        diag = M[i-1][j-1].value+s(seq1[i-1],seq2[j-1])
        up   = M[i-1][j].value-gapPenalty
        left = M[i][j-1].value-gapPenalty
        
        c = getMax(diag,up,left)

        M[i][j]=Cell(0,None) if c.value<0 else c

        if M[i][j].value>=maxv.value: 
            maxv.value=M[i][j].value
            maxv.i, maxv.j =i,j

        print(M[i][j].value,' ',end='')

    print('')

al1,al2=[],[]

i,j = maxv.i ,maxv.j

while True:
    
    if M[i][j].value==0: break
   
    dir=M[i][j].direction

    if dir=='diag':
        al1.insert(0,seq1[i-1])
        al2.insert(0,seq2[j-1])
        i,j =i-1,j-1
    elif dir=='up':
        al1.insert(0,seq1[i-1])
        al2.insert(0,'-')
        i-=1
    elif dir=='left':
        al1.insert(0,'-')
        al2.insert(0,seq2[j-1])
        j-=1

print(al1,'\n',al2)
