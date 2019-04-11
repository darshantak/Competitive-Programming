input_string=str(input())
convert=input_string.lower()
list_string=list(convert)
vowels=[]
final=[]
for i in range(len(list_string)):
    if list_string[i]=="a" or list_string[i]=="e" or list_string[i]=="i" or list_string[i]=="o" or list_string[i]=="u" or list_string[i]=="y":
        vowels.append(i)
for i in range(len(list_string)):
    if i in vowels:
        continue
    else:
        final.append(list_string[i])
final_string=""
for i in range(len(final)):
    final_string=final_string+str("."+final[i])
print(final_string)
