cases=int(input())
for i in range(cases):
    input_string=str(input())
    spaces=[]
    temp=""
    for i in range(len(input_string)):
        if input_string[i]==".":
            spaces.append(i)
    spaces.append(-1)
    spaces.sort(reverse=True)
    temp=""
    for i in spaces:
        for j in range(i+1,len(input_string)):
            if input_string[j]==".":
                break
            temp=temp+input_string[j]
        if i!=-1:
            temp=temp+"."
    print(temp)
            

# for i in range(spaces[0]+1,len(input_string)):
    #     temp=temp+input_string[i]
    # for i in range(len(spaces)-1):
    #     temp=temp+"."
    #     for j in range(spaces[i+1]+1,spaces[i]):
    #         temp=temp+input_string[j]
    # temp=temp+"."
    # for i in range(0,spaces[len(spaces)-1]):
    #     temp=temp+input_string[i]
    # print(temp)