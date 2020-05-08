a=[0]
b=[0]*129 #count array
for i in range(len(b)):
    #first check count of the coming element
    if b[a[i]]==0:
        a.append(0)
        b[a[i]]+=1
    else:
        for j in range(len(a)-2,-1,-1):
            if a[j]==a[len(a)-1]:
                temp=j
                break
        a.append((i)-j)
        b[a[i]]+=1

for _ in range(int(input())):
    n=int(input())
    x=a[n-1]
    count=0
    for i in range(n):
        if a[i]==x:
            count+=1

    print(count)
