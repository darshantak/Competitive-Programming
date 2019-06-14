a=[9, 8 ,5]
inc=a[0]
temp=[]
for j in range(len(a)):
    for i in range(1,len(a)):
        sol=max(a[j]^a[i],a[j])
        temp.append(sol)
sol=a[0]
exc=0
for j in range(len(a)):
    for i in range(1,len(a)):
        temp1 = sol
        sol=max(exc^a[i],sol)
        exc=temp1
        temp.append(sol)
a.sort()
sol1=a[0]
exc1=0
for j in range(len(a)):
    for i in range(1,len(a)):
        temp2 = sol1
        sol1=max(exc1^a[i],sol1)
        exc1=temp2
        temp.append(sol1)
print(max(temp))