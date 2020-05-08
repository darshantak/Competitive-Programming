n=int(input())
mat=[]
for i in range(n):
    temp=list(map(int,input().split()))
    mat.append(temp)
a,b=[],[]
for i in range(n):
    x=[]
    for j in range(n):
        if i==j:
            v="{0:.8f}".format(mat[i][j])
            x.append(v)
        else:
            v="{0:.8f}".format((mat[i][j]+mat[j][i])/2)
            x.append(v)
    a.append(x)

for i in range(n):
    x=[]
    for j in range(n):
        if i==j:
            v="{0:.8f}".format(0)
            x.append(v)
        else:
            v="{0:.8f}".format(mat[i][j]-float(a[i][j]))
            x.append(v)
    b.append(x)
for i in a:
    print(*i)
for i in b:
    print(*i)

            