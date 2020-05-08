for _ in range(int(input())):
    n=int(input())
    values=list(map(int,input().split(" ")))
    s=sum(values)
    l=len(set(values))
    if len(values)==l:
        avg=s//len(values)
    elif l==1:
        avg=values[0]
    else:
        for i in range(len(values)):
            temp=(s//len(values))+i
            if temp*len(values)>=s:
                avg=temp
                break

    print(avg)