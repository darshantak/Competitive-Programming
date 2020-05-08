t=int(input())
for _ in range(t):
	a,b,c=map(int,input().split())
	sub=[[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
	count=0
	sor=[a,b,c]
	sor.sort()
	a=sor[0]
	b=sor[1]
	c=sor[2]
	for i in range(len(sub)):
		a1=a-sub[i][0]
		b1=b-sub[i][1]
		c1=c-sub[i][2]
		if (a1>=0) and (b1>=0) and (c1>=0):
			count+=1
			a=a-sub[i][0]
			b=b-sub[i][1]
			c=c-sub[i][2]
			# print(a,b,c)
	print(count)

    