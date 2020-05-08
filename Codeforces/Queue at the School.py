n,t=map(int,input().split())
val=list(input())
temp=[]
ans=""
if "G" in val:
    for i in range(n-1):
        if val[i]=="B":
            temp.append(i)
for i in range(t):
    for j in range(len(temp)):
        if temp[j]>=n-1 : 
            temp[j]=temp[j]
        else:
            temp[j]+=1
    print(temp)
if len(temp)!=0:
    for i in range(n):
        if i in temp:
            ans=ans+"B" 
        else:
            ans=ans+"G"
    print(ans)
else:
    for i in val:
        ans=ans+i
    print(ans)