s=str(input())
temp1,temp2=[],[]
count=0
for i in range(len(s)-1):
    if s[i]=="A" and s[i+1]=="B":
        temp1.append((i+i+1))
        # temp1.append(i+1)
        count+=1
        
for i in range(len(s)-1,0,-1):
    if s[i]=="A" and s[i-1]=="B":
        temp2.append((i-1+i))
        # temp2.append(i-1)
        count+=1

# print(temp1)
# print(temp2)
if temp1 and temp2:
    if count>=2:
        if temp1==temp2:
            print("NO")
        elif (len(temp1)+len(temp2))==3:
            if sum(temp1)//2==sum(temp2) or sum(temp2)//2==sum(temp1):
                print("NO")
            else:
                print("YES")
        elif (len(temp1)+len(temp2))>3:
            print("YES")
        elif len(temp1)==1 and len(temp2)==1:
            if abs(temp1[0]-temp2[0])==2:
                print("NO")
            else:
                print("YES")
        else:
            print("NO")
        # elif len(set((set(temp1)&set(temp2))))>0:
    #     print("NO")
    
    else:
        print("NO")
else:
    print("NO")