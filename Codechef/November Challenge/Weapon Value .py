# a=int(input(),2)
# b=int(input(),2)
# print(bin(a^b)[2:])
t=int(input())
for _ in range(t):
    n=int(input())
    values=[]
    for i in range(n):
        values.append(int(input(),2))
    final=0
    for i in range(n):
        final=final^values[i]
    count=0
    x=bin(final)[2:]
    for _ in x:
        if _=="1":
            count+=1
    print(count)
