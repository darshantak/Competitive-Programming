for _ in range(int(input())):
    n,k=map(int,input().split())
    temp=n//k
    temp1=temp+1
    if n%k==0:
        print(n)
    elif n==1:
        print(1)
    else:
        if k%2==0:
            print((temp*(k//2))+(temp1*(k//2)))
        else:
            x=k//2
            print((temp*(k-x)+(temp1*(x))))
