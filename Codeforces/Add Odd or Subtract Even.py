t=int(input())
for _ in range(t):
    a1,b1=map(int,input().split())
    if a1==b1:
        print(0)
    elif a1<b1:
        x=abs(b1-a1)
        if x%2==0:
            print(2)
        else:
            print(1)
    else:
        x=abs(b1-a1)
        if x%2==0:
            print(1)
        else:
            print(2)
        
    