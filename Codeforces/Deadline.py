import math
for _ in range(int(input())):
    n,d=map(int,input().split())
    if n>=d:
        print("YES")
    else:
        q=d//n
        x=(d//(q+1))
        flag=0
        for i in range(1,d):
            temp=math.ceil(d/(i+1))+i
            if temp<=n:
                print("YES")
                flag=1
                break
        if not flag:
            print("NO")

