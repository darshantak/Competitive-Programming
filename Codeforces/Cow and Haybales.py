for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    if n==1:
        print(a[0])
    else:
        while d>0:
            for i in range(1,n):
                if a[i]>0:
                    a[i-1]+=1
                    a[i]-=1
                    break
            d-=1
        print(a[0])