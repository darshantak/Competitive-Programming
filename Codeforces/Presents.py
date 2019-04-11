friend=int(input())
gifts_dis=list(map(int,input().split(' ')))
sols=[]
sols_string=""
for i in range(1,friend+1):
    for j in range(0,len(gifts_dis)):
        if gifts_dis[j]==i:
            sols.append(j)
for i in range(len(sols)):
    sols[i]=sols[i]+1             
for i in sols:
    sols_string=sols_string+str(i)+" "
print(sols_string)