for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(-1)
    else:
        temp="5"
        for i in range(n-1):
            temp=temp+"7"
        print(temp)
