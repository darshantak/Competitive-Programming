cases=int(input())
for i in range(cases):
    n=int((input()))
    if n%2!=0:
        a=list(map(int,input().split(" ")))
        xor=0
        for i in a:
            xor=xor^i
        print(xor)