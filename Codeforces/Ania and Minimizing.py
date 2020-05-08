n,k=map(int,input().split(" "))
val=int(input())
s=str(val)
if len(s)==1 or val%10==0:
    print(0)
    exit()
if s[0]=="1":
    for i in range(1,k+1):
        val=val-int(s[i])*(10**(k-i))
        
else:
    val=val-((int(s[0])-1)*(10**(len(s)-1)))

    for i in range(1,k):
        val=val-(int(s[i])*(10**(n-i-1)))
print(val)