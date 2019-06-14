cases=int(input())
for i in range(cases):
    m,n=map(int,input().split(" "))
    sol=m^n
    i=1
    while sol>0:
        rem=sol%2
        sol=sol/2
        if rem==1:
            print(i)
            break
        i+=1
    