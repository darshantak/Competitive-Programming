# def bit(l):
#     temp=[]
#     for i in range(len(l)-1):
#         if l[i+1]>l[i]:
#             temp.append(i)
#     return temp
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    p=list(map(int,input().split()))
    s=sorted(a)
    p.sort()
    if a==s:
        print("YES")
    else:
        x=min(p)
        y=max(p)
        temp=[]
        fin=[]
        for i in range(x,y+1):
            temp.append(i)
        temp1=[]
        for i in range(1,len(temp)+1):
            if i not in p:
                fin.append(temp1)
                temp1=[]
            else:
                temp1.append(i)
            print(temp1)
        fin.append(temp1)
        print(fin)
gfgfgthg
        # print(m)
        # if len(m)==0:
        #     for i in range(len(p)-1):
        #         a[x-1:p[i]+1+1]=sorted(a[x-1:p[i]+1+1])
        #         # print(sorted(a[x:p[i]+1]))
        #         a[p[i+1]-1:y+1+1]=sorted(a[p[i+1]-1:y+1+1])
        #         # print(a)
        #     if a==s:
        #         print("YES")
        #     else:
        #         print("NO")
        # else:
        #     for i in range(len(m)):
        #         a[x:m[i]+1]=sorted(a[x:m[i]+1])
        #         a[m[i+1]:y+1]=sorted(a[m[i+1]:y+1])
        #     if a==s:
        #         print("YES")
        #     else:
        #         print("NO")