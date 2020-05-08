test=int(input())
for i in range(test):
    number=int(input())
    values=list(map(int,input().split()))
    c,z=0,0
    if 0 in values:
        for i in values:
            if i==0:
                z+=1
        c+=z
        if sum(values)==-1*z:
            c+=1
    elif sum(values)==0:
        c+=1
        if 0 in values:
            c+=1
    print(c)