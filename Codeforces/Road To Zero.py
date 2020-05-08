t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    temp=abs(y-x)

    sum1=temp*a+min(x,y)*b
    print(sum1)

gfjdghkjsgaj