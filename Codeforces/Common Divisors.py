from math import gcd
# def gcd(a,b):
#     a=int(a)
#     b=int(b)
#     if a==0:
#         return b
#     if b==0:
#         return a
#     return gcd(b,a%b)
n=int(input())
values=list(map(int,input().split(" ")))
count=0
temp=0
for i in range(len(values)):
    temp=gcd(temp,values[i])
for i in range(1,int(temp**0.5)+1):
    if temp%i==0:
        if temp//i==i:
            count+=1
        else:
            count+=2
print(count)