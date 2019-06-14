cases=int(input())
for i in range(cases):
    a,b=map(int,input().split(" "))
    sol=a^b
    count=0
    while sol>0:
        rem=sol%2
        sol=int(sol/2)
        if rem==1:
            count+=1
    print(count)