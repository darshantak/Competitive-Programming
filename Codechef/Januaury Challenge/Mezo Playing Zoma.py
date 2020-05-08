number=int(input())
st=input()
right,left=0,0
for i in range(number):
    if st=="L":
        left-=1
    else:
        right+=1
temp=abs(left-right)
print(temp+1)