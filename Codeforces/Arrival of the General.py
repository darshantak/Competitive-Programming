soldiers=int(input())
values=list(map(int,input().split(" ")))
max_height=max(values)
index_max=values.index(max_height)
values=values[::-1]
min_height=min(values)
index_min=values.index(min_height)
if soldiers-1-index_min<index_max:
	sol=index_max+index_min-1
else:
	sol=index_max+index_min
print (sol)
