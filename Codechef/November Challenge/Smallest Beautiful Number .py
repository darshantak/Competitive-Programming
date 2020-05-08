import math
def isperfect(x):
    # print(12)
    root=math.sqrt(x)
    return ((root-math.floor(root))==0)
evn=6
od=5
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    elif n==2:
        print(34)
    elif n==3:
        print(122)
    elif isperfect(n)==1:
        # print(1)
        temp=""
        for i in range(n):
            temp=temp+"1"
        print(temp)
    else:
        if n%2==0:
            temp="" 
            # print(0)
            for i in range(n-2):
                temp=temp+"1"
            temp=temp+str(((n-evn)//2)+12)
            print(temp)
        else:
            temp=""
            for i in range(n-2):
                temp=temp+"1"
            temp=temp+str(((n-od)//2)+23)
            print(temp)