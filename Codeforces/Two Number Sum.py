#Naive Solution
def naive(input_list,result):
    for i in range(len(input_list)-1):
        for j in range(i+1,len(input_list)):
            if input_list[i]+input_list[j]==result:
                return [input_list[i],input_list[j]]

#Using Hash Table
def hash_table(input_list,result):
    nums={}
    for i in range(len(input_list)):
        if result-input_list[i] in nums.keys():
            return nums[input_list[i]],input_list[i]
        else:
            nums[input_list[i]]=True
    return -1
l=[3,5,-4,8,11,1,-1,6]
print(hash_table(l,10))

fdincomplete
