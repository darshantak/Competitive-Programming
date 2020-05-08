n=int(input())
a=list(map(int,input().split()))
i=0
count=[]
temp=0
while i<n-1:
    if a[i+1]>=a[i]:
        # print(a[i+1],a[i])
        temp+=1
    else:
        count.append(temp)
        temp=0
    i+=1
    if i==n-1:
        count.append(temp)
        
# print(count)
if temp>=0 and len(count)==0:
    print(temp+1)
elif len(count)>0:
    print(max(count)+1)
else:
    print(0)