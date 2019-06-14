cases=int(input())
for i in range(cases):
    n=int(input())
    flag=0
    if n==1:
        print("YES")
    elif n==0:
        print("NO")
    else:    
        while n>1:
            if n%2!=0:
                flag=1
                break
            n=int(n/2)
        if flag==0:
            print("YES")    
        else:
            print("NO")

