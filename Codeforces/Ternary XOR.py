t=int(input())
for _ in range(t):
    number=int(input())
    input_string=str(input())
    str1="1"
    str2="1"
    temp=0
    for i in range(1,number):
        if input_string[i]=="2":
            str1+="1"
            str2+="1"
        elif input_string[i]=="1":
            str1+="1"
            str2+="0"
            temp=i
            break
        else:
            str1+="0"
            str2+="0"
    if temp!=0:
        for i in range(temp+1,number):
            str1+="0"
            str2+=input_string[i]
    print(str1)
    print(str2)