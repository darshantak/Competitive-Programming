for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    sol=[]
    for i in range(n):
        count=0
        for j in range(i+1,n):
            if a[i]<a[j]:
                count=n-j
                sol.append(count)
                break
    for i in range(len(a)-len(sol)):
        sol.append(0)
    print(*sol)