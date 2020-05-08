import math
size=int(input())
mat=[]
for i in range(size):
    val=list(map(int,input().split(" ")))
    mat.append(val)
diag=[]
for i in range(1,size):
    diag.append(mat[0][i])
#print(diag)
x=mat[1][2]/diag[0]
y=math.sqrt(diag[1]/x)
diag.insert(0,int(y))
for i in range(1,len(diag)):
    diag[i]=int(diag[i]//y)
print(*diag)

