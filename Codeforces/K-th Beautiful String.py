for _ in range(int(input())):
    n,k=map(int,input().split())
    temp,flag=0,0
    while (temp*(temp+1)/2)<=k:
        flag=temp
        temp+=1
    fin=""
    flag1=flag+1
    flag_sum=k-((flag*(flag+1))/2)
    # print(flag1,flag_sum)
        # print(0)
    if k==1:
        for i in range(n-2):
            fin=fin+"a"
        fin=fin+"bb"
        print(fin)
    elif k==(n*(n-1))//2:
        fin=fin+"bb"
        for i in range(2,n):
            fin=fin+"a"
        print(fin)
    else:
        for i in range(n):
            if i==flag+1 or i==flag_sum-1:
                fin+="b"
            else:
                fin+="a"
        # print(fin)
    
        print(fin[::-1])

        
