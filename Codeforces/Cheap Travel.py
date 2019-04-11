n,m,a,b=map(int,input().split(' '))
temp1=0
temp2=0
x=n//m
temp1+=(x*b)
if n%m!=0:
    if (n-(x*m))*a<b:
        temp1+=(n-(x*m))*a
    else:
        temp1+=b
temp2=n*a
print(min(temp1,temp2))
