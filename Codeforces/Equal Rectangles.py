cases=int(input())
for i in range(cases):
    n=int(input())
    values=list(map(int,input().split(" ")))
    values.sort()
    flag=0
    temp=0
    area=values[0]*values[-1]
    if len(values)%4!=0:
        flag=0
    else:
        for i in range(0,len(values),2):
            if values[i]==values[i+1] and values[4*n-i-1]==values[4*n-i-2] and values[i]*values[4*n-i-1]==area:
                flag=1
                # print(0)
            else:
                flag=0
                break
    if flag==1:
        print("YES")
    else:

        print("NO")
