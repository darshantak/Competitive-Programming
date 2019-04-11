students,gifts=map(int,input().split(" "))
input_list=list(map(int,input().split(" ")))
sorted_list=sorted(input_list)
j=[]
for i in range(len(input_list)):
    if students+i<=len(input_list):
        j.append(sorted_list[students-1+i]-sorted_list[i])
print(min(j))