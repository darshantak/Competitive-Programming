arr=[0]*2*(5*(10**5))
arr[1],arr[3],arr[5]=0,8,40
count=3
for i in range(7,2*(5*(10**5))):
    
    if i%2!=0:    
        arr[i]=arr[i-2]+8*(count*count)
        count+=1
# print(arr[:10])
    # arr.append(temp)
for i in range(int(input())):
    n=int(input())
    print(arr[n])