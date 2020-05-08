def count(n):
    if n==0:
        return 0
    else:
        return (n&1)+(count(n>>1))

n,m,k=map(int,input().split())
inp=[]
for _ in range(m+1):
    inp.append(int(input()))
fed=inp[m]
temp=[]
for i in range(m+1):
    sol=fed^inp[i]
    temp.append(count(sol))
count=0
print(temp)
for i in temp:
    if i<=k:
        count+=1
print(count)
