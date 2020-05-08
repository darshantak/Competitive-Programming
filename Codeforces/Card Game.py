for t in range(int(input())):
    n,k1,k2=map(int,input().split())
    player1=list(map(int,input().split()))
    player2=list(map(int,input().split()))
    if n in player1:
        temp=1
    else:
        temp=0
    if temp:
        print("YES")
    else:
        print("NO")