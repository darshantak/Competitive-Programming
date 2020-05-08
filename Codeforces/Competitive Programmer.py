def div(a):
    sum1=0
    for i in a:
        sum1+=int(i)
    # print(sum1)
    if sum1%3==0:
        return 1
    else:
        return 0
for t in range(int(input())):
    inp=(input())
    li=list(str(inp))
    if "0" in li:
        for i in range(len(li)-1):
            if li[i]=="0": 
                li.pop(i)
                break
        flag=0
        for i in li:
            if int(i)%2==0:
                if div(li):
                    flag=1
        
        if flag==0:
            print("cyan")
        else:
            print("red")
    else:
        print("cyan")