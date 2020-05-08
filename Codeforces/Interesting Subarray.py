for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    for i in range(n):
        for j in range(i+1,n):
            k=(j-i)+1
            maxi=max(a[i:j+1])
            mini=min(a[i:j+1])
            if maxi-mini>=k:
                print("YES")gu
                print(i+1,j+1)
                flag=1
                break
        if flag==1:
            break
    if flag==0:
        print("NO")
