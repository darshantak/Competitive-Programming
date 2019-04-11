input_no=(input())
input_list=list(str(input_no))
count=0
for i in range(len(input_list)):
    if input_list[i]=="4" or input_list[i]=="7":
        count+=1
    if count==len(input_list):
        print("YES")
        exit()
if int(input_no)%4==0 or int(input_no)%7==0 or int(input_no)%47==0:
    print("YES")
    exit()
if int(input_no)%4!=0 and int(input_no)%7!=0 and int(input_no)%47!=0:
    print("NO")
elif count<len(input_list):
    print("NO")



