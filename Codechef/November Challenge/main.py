import math
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    # elif n==2:
    #     print(34)
    # elif n==3:
    #     print(122)
    else:        
        for i in range(10**(n-1)+1,10**n):
            if "0" not in str(i):
                flag=0
                temp=list(str(i))
                sum=0
                # print(temp)
                for j in temp:
                    sum=sum+(int(j)**2)
                root=math.sqrt(sum)
                # print(root)
                if ((root - math.floor(root)) == 0):
                    flag=i
                    print(flag)
                    break
