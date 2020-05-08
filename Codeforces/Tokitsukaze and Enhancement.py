number=int(input())
rem=number%4
if rem==0:
    number=number+1
    print(1,"A")
elif rem==1:
    print(0,"A")
elif rem==2:
    number=number+1
    print(1,"B")
else:
    number=number+2
    print(2,"A")