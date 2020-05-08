n=int(input())
f=list(map(int,input().split()))
temp=[]
flag=[]
for i in range(1,n+1):
    if i not in f:
        temp.append(i)
    if f[i-1]==0:
        flag.append(i)
# print(temp)
# print(flag)
if len(temp)%2==0:
    temp1=sorted(temp,reverse=True)
else:
    temp.sort(reverse=True)
    x=temp.pop(len(temp)//2)
    temp.append(x)
    temp1=temp
    # print(temp1)
for i in range(len(temp)):
    # print(i)
    f[flag[i]-1]=temp1[i]
print(*f)