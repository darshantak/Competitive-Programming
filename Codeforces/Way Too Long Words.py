number_inputs=int(input())
for i in range(number_inputs):
    input_string=str(input())
    items=list(input_string)
    if len(items)>10:
        print(items[0]+str(len(items)-2)+items[len(items)-1])
    else:
        print(input_string)
