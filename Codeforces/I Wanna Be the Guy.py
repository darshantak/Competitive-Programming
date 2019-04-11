level=int(input())
x=list(map(int,input().split(" ")))
y=list(map(int,input().split(" ")))
levels_count_x=x[0]
levels_count_y=y[0]
final_values=[]
check_list=[]
for i in range(1,len(x)):
    final_values.append(x[i])
for i in range(1,len(y)):
    final_values.append(y[i])
a=sorted(final_values,reverse=True)
for i in range(len(final_values)-1):
    if a[i]==a[i+1]:
        check_list.append(i)
for i in sorted(check_list,reverse=True):
    a.pop(i)
if len(a)==level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")