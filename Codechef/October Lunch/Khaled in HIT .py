for _ in range(int(input())):
    n=int(input())
    v=list(map(int,input().split()))
    v.sort()
    temp=[]
    if n==4:
        if len(set(v))==4:
            print(v[1],v[2],v[3])
        else:
            print(-1)
    elif n>4:
        final=[]
        flag=0
        for i in range(n//4,n,n//4):
            final.append(v[i-1])
            final.append(v[i])
        for i in range(0,len(final),2):
            if final[i]<final[i+1]:
                flag=1
            else:
                flag=0
                break
        ans=""
        if flag==1:
            for i in range(n//4,n,n//4):
                ans=ans+str(v[i])+" "
            print(ans)
        else:
            print(-1)


# s=list(set(v))
        # flag=0
        # for i in s:
        #     temp.append(v.count(i))
        # print(temp)
        # for i in temp:
        #     if i>n//4:
        #         flag=0
        #         break
        #     else:
        #         flag=1
        # ans=""
        # if flag==1:
        #     for i in range(n//4,n,n//4):
        #         ans=ans+str(v[i])+" "
        #     print(ans)
        # else:
        #     print(-1)