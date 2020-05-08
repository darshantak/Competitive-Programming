for _ in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    final=[]
    for i in range(0,len(v)):
        count=1
        check=i+1
        x=i
        while check!=v[x]:
            count+=1
            x=v[x]-1
        final.append(count)
    print(*final)

        