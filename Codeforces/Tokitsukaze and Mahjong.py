a,b,c=input().split(" ")
# num=[]
# suits=[]
# num.append(int(a[0]))
# num.append(int(b[0]))
# num.append(int(c[0]))
# suits.append(a[1])
# suits.append(b[1])
# suits.append(c[1])
# num.sort()
if a[1]==b[1] and b[1]==c[1] and a[1]==c[1]:
    sol=[]
    sol.append(a)
    sol.append(b)
    sol.append(c)
    sol.sort()
    
diffa=int(a[0])-int(b[0])
diffb=int(b[0])-int(c[0])
diffc=int(c[0])-int(a[0])
if diffa<0 :
    diffa=diffa*(-1)
if diffa<0 :
    diffb=diffb*(-1)
if diffa<0 :
    diffc=diffc*(-1)
if a[1]!=b[1] and  b[1]!=c[1] and a[1]!=c[1]:
    print(2)
elif a[1]==b[1] and a[1]!=c[1]:
    if diffa<=2:
        print(1)
    else:
        print(2)
elif b[1]==c[1] and a[1]!=b[1]:
    if diffb<=2:
        print(1)
    else:
        print(2)
elif c[1]==a[1] and a[1]!=b[1]:
    if diffc<=2:
        print(1)
    else:
        print(2)
elif a==b and b==c and a==c:
    print(0)
elif a==b:
    print(1)
elif b==c:
    print(1)
elif a==c:
    print(1)
elif diffa==1 and diffb==1 and diffc==1:
    print(0)

print(diffa,diffb,diffc)
