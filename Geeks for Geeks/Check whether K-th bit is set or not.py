cases=int(input())
for i in range(cases):
    x=int(input())
    bit=int(input())
    temp=[]
    string=""
    while x>1:
        rem=x%2
        temp.append(rem)
        x=int(x/2)
        if x==1:
            temp.append(1)
    for i in temp[::-1]:
        string=string+str(i)
    for i in range(len(string)-1,-1,-1):
        if string[len(string)-bit-1]=="1":
            print("Yes")
            break
        else:
            print("No")
            break