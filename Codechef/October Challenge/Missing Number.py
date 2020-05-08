import string
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
    if len(set(base))!=1:
        val=[]
        notval=[]
        for i in range(len(base)):
            if base[i]!="-1":
                val.append(i)
            else:
                notval.append(i)
        final=[]
        for i in range(len(val)):
            sum=0
            x=str(num[val[i]])
            x=x[::-1]
            b=int(base[val[i]])
            for j in range(len(x)):
                if x[j].isdigit():
                    sum=sum+(b**j)*int(x[j])
                else:
                    sum=sum+(b**j)*int(letters[x[j]])
            final.append(sum)
        if len(set(final))==1:
            if len(num)>1:
                for i in range(len(notval)):
                    x=str(num[notval[i]])
                    x=x[::-1]
                    b=2
                    final1=[]
                    # print(b)
                    while b<=36:
                        sum1=0
                        flag=0
                        
                        for j in range(len(x)):
                            if x[j].isdigit():
                                # print(1)
                                sum1=sum1+(b**j)*int(x[j])
                            else:
                                sum1=sum1+(b**j)*int(letters[x[j]])
                        final1.append(sum1)
                        b+=1
                    for i in final1:
                        if i==final[0]:
                            flag=i
                            break
                        else:
                            flag=0

                if flag==0:
                    print(-1)
                else:
                    print(flag)  
            
    
        else:
            print(-1)
    else:
        sum1=0
        x=str(num[0])
        x=x[::-1]
        b=int(base[0])
        for j in range(len(x)):
            if x[j].isdigit():
                # print(1)
                sum1=sum1+(b**j)*int(x[j])
            else:
                sum1=sum1+(b**j)*int(letters[x[j]])
        print(sum1)