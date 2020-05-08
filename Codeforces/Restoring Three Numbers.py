input_values=list(map(int,input().split(" ")))
sorted_val=sorted(input_values,reverse=True)
b=(sorted_val[1]+sorted_val[2]-sorted_val[3])/2
a=sorted_val[1]-b
c=sorted_val[2]-b
print(int(a),int(b),int(c))





