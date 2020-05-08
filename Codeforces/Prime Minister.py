num=int(input())
votes=list(map(int,input().split(" ")))
total=sum(votes)
final=votes[0]

spaces=[]
if votes[0]>int(total/2):
    print(1)
    print(1)
else:
    count=1
    if votes[0]<=int(total/2):
        spaces.append(0)
        for i in range(1,len(votes)):
            if votes[0]>=2*votes[i]:
                final=final+votes[i]
                count=count+1
                spaces.append(i)
            if final>int(total/2):
                print(count)
               
                for i in spaces:
                    print(i+1,end=" ")
                exit()

        for i in range(1,len(votes)):
            flag=1
            if votes[0]<2*votes[i]:
                flag=0
        if flag==0:
            print(0)
            exit()
            print(count)
            for i in spaces:
                print(i,end=" ")        

