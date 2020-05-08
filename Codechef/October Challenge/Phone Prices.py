for _ in range(int(input())):
    from collections import deque
    n=int(input())
    values=list(map(int,input().split()))
    ans=1
    small=0
    qu=deque([0])
    for i in range(1,n):
        while(len(qu)!=0 and i-qu[0]>5):
            qu.popleft()
        small=qu[0]
        if values[small]>values[i]:
            small=i
            ans+=1
        while(len(qu)!=0 and values[qu[len(qu)-1]]>values[i]):
            qu.pop()
        qu.append(i)

    print(ans)
