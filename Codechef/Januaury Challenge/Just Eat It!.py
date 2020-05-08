
def SubArraySum(arr, n ): 
	result = 0

	for i in range(0, n): 
		result += (arr[i] * (i+1) * (n-i)) 

	# return all subarray sum 
	return result 



for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    yas=sum(a)
    flag=0
    for i in range(n):
        if a[i]>=0:
            flag=1
        else:
            flag=0
            break
    if flag:
        print("YES")
    else:
        # diff=[]
        # sum1=0
        # for i in range(n):
        #     if a[i]>=0:
        #         sum1+=a[i]
        #     else:
        #         diff.append(sum1)
        #         sum1=0
        #         sum1+=a[i]
        #     if i==len(a)-1:
        #         diff.append(sum1)
        # print(diff)
        # flag=1
        # for i in diff:
        #     if i>=yas:
        #         flag=0   
        #         # print(i)
        #         break
        # if flag:
        #     print("YES")
        # else:
        #     print("NO")
