str=input()
word = "hello"
index = 0
count=0
for i in range(len(str)):
    if str[i]==word[index]:
        index+=1
        count+=1
    if(count==5):
        print("YES")
        break
if count==5:
    exit()
if(index<5):
    print("NO")
else:
    print("YES")