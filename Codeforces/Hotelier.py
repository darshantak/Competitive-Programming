n=int(input())
values=input()
x=0
y=0
initial=""
ini=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,n):
    if values[i]=="L":
        ini[x]=1
        x+=1
    elif values[i]=="R":
        ini[9-y]=1
        y+=1
    else:
        temp=int(values[i])
        ini[temp]=0 
        if temp<x: 
            x=temp
        elif temp>y:
            y=9-temp
for i in ini:
    initial=initial+str(i)
print(initial)
