n=int(input())
p=list(map(int(input().split())))
odd=[]
even=[]
for i in range(n):
    if (i+1) not in p:
        if (i+1)%2==0:
            even.append(i+1)
        else:
            odd.append(i+1)
if p[0]==0:
    for i in range(n):
        if p[i]!=0:
            dsfs