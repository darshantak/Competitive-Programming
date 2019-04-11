value,number=map(int,input().split(" "))
if value%2==0:
    temp=value//2
    if number<=temp:
        print(2*number-1)
    else:
        print(2*(number-temp))
else:
    temp=value//2+1
    if number<=temp:
        print(2*number-1)
    else:
        print(2*(number-temp))
