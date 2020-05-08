t=int(input())
for _ in range(t):
    inp=input()
    temp=0
    fin=[]
    if len(inp)==1:
        print(inp)
    else:
        while temp<len(inp):
            if temp==len(inp)-1:
                fin.append(inp[temp])
                break
            if inp[temp]==inp[temp+1]:
                temp=temp+2
                # print(temp)
            else:
                fin.append(inp[temp])
                temp=temp+1
                # print(final)
        x=list(sorted(set(fin)))
        count=""
        for i in range(len(x)):
            count=count+str(x[i])

        print(count)