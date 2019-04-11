teams=int(input())
values=[]
count=0
for i in range(teams):
    values.append(list(map(int,input().split(" "))))
for i in range(teams):
    for j in range(teams):
        if values[i][1]==values[j][0]:
            count+=1
print(count)
