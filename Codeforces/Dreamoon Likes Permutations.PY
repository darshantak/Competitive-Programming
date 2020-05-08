for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    arr,temp,temp1=[],[],[]
    x=1
    if len(set(a))==1 and len(a)>1:
        print(0)
        continue
    for i in range(len(a)):
        arr.append(a[i])
        # print(arr)

        if i==len(a)-1:
            
            x+=1
            # arr.append(a[i])
            if sorted(arr)== [j for j in range(1,x+1)]:
                temp.append(x)
                # print(0)
        elif a[i+1] in arr:
            # test=[j for j in range(1,x+1)]
            if sorted(arr)== [j for j in range(1,x+1)]:
                temp.append(x)
            arr=[]
            x=0
        else:
            x+=1
    # print(temp)
    
    x=1
    arr=[]
    for i in range(len(a)-1,-1,-1):
        arr.append(a[i])
        # print(arr)

        if i==0:
            
            x+=1
            # arr.append(a[i])
            if sorted(arr)== [j for j in range(1,x+1)]:
                temp1.append(x)
                # print(0)
        elif a[i-1] in arr:
            # test=[j for j in range(1,x+1)]
            if sorted(arr)== [j for j in range(1,x+1)]:
                temp1.append(x)
            arr=[]
            x=0
        else:
            x+=1
    if len(temp1)==2 and len(temp)==2:
        print(2)
        print(*temp1[::-1])
        # print(*temp[::-1])
        print(*temp1)
    elif len(temp1)==2:
        print(1)
        print(*temp1[::-1])
    elif len(temp)==2:
        print(1)
        print(*temp)
    else:
        print(0)
    
//WA