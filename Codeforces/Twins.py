coins= int(input())
values= map(int,input().split())
sort_coins=sorted(values,reverse=True)
sum_coins = sum(sort_coins)
sum_coins = int(sum_coins/2)+1
sumi = 0
i = 0
for j in sort_coins:
	sumi = sumi+j
	i = i+1	
	if(sumi>=sum_coins):
		break 
print(i)