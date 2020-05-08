# a=[[0,0,0],[0,0,0],[0,0,0]]
# def c(my):
    
#     freq={}
#     for i in my:
#         freq[i]=my.count(i)
#     for i,j in freq.items(): 
#         for k in range(3):
#             a[i-1][k]+=1
    
    
#     # for i in freq.values():
#     #     print(i)
#     # for i in freq.keys():
#     #     print(i)
# my=[1,3,1]
# my1=[2,3,1]
# c(my)
# c(my1)
# print(a)

import string

def inter(ls1,ls2):
    return list(set(ls1)&set(ls2))
    
letters={letter:str(index) for index,letter in enumerate(string.ascii_uppercase,start=10)}
for t in range(int(input())):
    n=int(input())
    #Taking Input
    inp=[]
    for i in range(n):
        x=list(map(str,input().split()))
        inp.append(x)
    base=[]
    for i in range(n):
        base.append(inp[i][0])
    num=[]
    for i in range(n):
        num.append(inp[i][1])

    if len(set(base))==1:
        final=[]
        for i in num[:2]:
            x=str(i)
            x=x[::-1]
            b=2
            temp=[]
            while b<=36:
                sum=0
                for j in range(len(x)):
                    if x[j].isdigit():
                        sum=sum+(b**j)*int(x[j])
                    else:
                        sum=sum+(b**j)*int(letters[x[j]])
                b+=1
                temp.append(sum)
            final.append(temp)
        intersection=inter(final[0],final[1])

        if len(intersection)==0:
            print(-1)
        else:
            if n>2:
                for i in num[2:]:
                    flag=0
                    x=str(i)
                    x=x[::-1]
                    b=2
                    while b<=36:
                        sum=0
                        for j in range(len(x)):
                            if x[j].isdigit():
                                sum=sum+(b**j)*int(x[j])
                            else:
                                sum=sum+(b**j)*int(letters[x[j]])
                        # print(sum,end=" ")
                        if sum in intersection:
                            flag=sum
            
                        b+=1
                    if flag==0:
                        break
            else:
                flag=intersection[0]
        if flag==0:
            print(-1)
        else:
            print(flag)
    else:
        for i in range(n):
            if int(base[i])!=-1:
                val=num[i]
                b=int(base[i])
                temp=i
                # print(val)
                break
        x=str(val)
        x=x[::-1]
        sum1=0
        # print(b)
        for j in range(len(x)):
            if x[j].isdigit():
                sum1=sum1+(b**j)*int(x[j])
            else:
                sum1=sum1+(b**j)*int(letters[x[j]])
            # print(sum1)
        for i in num:
            
            if i!=val:
                flag=0
                y=str(i)
                y=y[::-1]
                b=2
                while b<=36:
                    sum=0
                    for j in range(len(y)):
                        if y[j].isdigit():
                            sum=sum+(b**j)*int(y[j])
                        else:
                            sum=sum+(b**j)*int(letters[y[j]])
                    b+=1
                    # print(sum)
                    if sum==sum1:
                        flag=sum
                        break
                if flag==0:
                    break
        if flag==0:
            print(-1)
        else:
            print(flag)
        
                    

    

