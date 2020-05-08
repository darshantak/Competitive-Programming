for _ in range(int(input())):
    n=int(input())
    val=list(map(int,input().split()))
    maxi=max(val)
    mini=min(val)
    for i in range(n):
        if val[i]==maxi:
            max_ind=i
        if val[i]==mini:
            min_ind=i
    if max_ind>min_ind:
        print(mini,maxi)
    else:
        print(maxi,mini)