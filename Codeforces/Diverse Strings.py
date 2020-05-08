number=input()
count=0
for i in range(int(number)):
        input_string=input()
        sorted_list=sorted(input_string)
        for i in range(len(sorted_list)-1):
                if chr(ord(sorted_list[i])+1)==sorted_list[i+1]:
                        count+=1
                else:
                        continue
        if count+1==len(input_string):
                print("YES")
                count=0
        else:
                print("NO")
                count=0