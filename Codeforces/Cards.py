val=int(input())
x=input()
z=0
n=0
for i in range(len(x)):
    if x[i]=="z":
        z=z+1
    elif x[i]=="n":
        n=n+1
ans=[]
for i in range(n):
    ans.append(1)
for i in range(z):
    ans.append(0)
print(*ans)