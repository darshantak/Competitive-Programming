input_string=list(map(str,input().split("+")))
sorted_string=sorted(input_string)
final_string=""
for i in range(1,len(sorted_string)):
    final_string=final_string+str("+"+sorted_string[i])
print(str(sorted_string[0])+final_string)