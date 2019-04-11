n=int(input())
temp1 = int(n / 10)
temp2= -(int(-n / 100) * 10 + (-n) % 10)
if n>0:
    print(n)
else:
    print(max(temp1,temp2))
