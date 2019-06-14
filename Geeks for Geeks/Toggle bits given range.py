cases=int(input())
for i in range(cases):
    n,l,r=map(int,input().split(" "))
    for j in range(l,r+1):
        n=(n^(1<<(j-1)))
    print(n)