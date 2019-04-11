input_line=int(input())
mat=[]
add_x=0
add_y=0
add_z=0
for i in range(input_line):
    mat.append(list(map(int,input().split(" "))))
for i in range(3):
    for j in range(input_line):
        if i==0:
            add_x=add_x+mat[j][i]
        if i==1:
            add_y=add_y+mat[j][i]
        if i==2:
            add_z=add_z+mat[j][i]
if add_x==add_y==add_z==0:
    print("YES")
else:
    print("NO")