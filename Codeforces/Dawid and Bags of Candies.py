val=list(map(int,input().split(" ")))
val.sort()
temp=[]
if sum(val)%2==0:
    for i in range(len(val)//2):
        temp.append(val[i]+val[len(val)-i-1])
    if len(set(temp))==1 or val[0]+val[1]+val[2]==val[3]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    
    