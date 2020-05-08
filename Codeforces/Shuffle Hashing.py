for t in range(int(input())):
    pin=input()
    hin=input()
    p_sort=sorted(pin)
    if len(pin)==len(hin):
        hfin=sorted(hin)
        if hfin==p_sort:
            print("YES")
        else:
            print("NO")
    elif len(pin)>len(hin):
        print("NO")
    
    else:
        flag=0
        for i in range(0,len(hin)-len(pin)+1):
            hfin=hin[i:i+len(pin)]
            temp=sorted(hfin)
            if temp==p_sort:
                flag=1
                break
        if flag:
            print("YES")
        else:
            print("NO")