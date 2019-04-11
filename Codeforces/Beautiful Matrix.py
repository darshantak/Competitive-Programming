n=5
m=5
mat=[] 
for i in range(n):
    inputs=list(map(int,input().split(' ')))[:m]
    mat.append(inputs)
for i in range(5):
    for j in range(5):
        if mat[i][j]==1:
            row=i
            column=j
count=0
while row!=2:
    if row>2:
        row=row-1
    else:
        row=row+1
    count=count+1 
while column!=2:
    if column>2:
        column=column-1
    else:
        column=column+1
    count+=1 
print(count)