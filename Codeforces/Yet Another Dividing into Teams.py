t=int(input())
for _ in range(t):
    number= int(input())
    values=list(map(int,input().split()))
    values.sort()
    if len(values)==2:
        if abs(values[0]-values[1])==1:
            print(2)
        else:
            print(1)
    elif len(values)==1:
        print(1)
    else:
        count=0
        for i in range(len(values)-1):
            if abs(values[i]-values[i+1])==1:
                count+=1
        if count>0:
            print(2)
        else:
            print(1)