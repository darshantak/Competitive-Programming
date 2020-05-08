# cook your dish here
def nCr(n, r): 
  
    return (fact(n) // (fact(r)  
                * fact(n - r))) 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 
for _ in range(int(input())):
    n,k=map(int,input().split())
    val=list(map(int,input().split()))
    val.sort()
    if len(set(val))==1:
        print(nCr(n,k))
    elif len(set(val))==len(val):
        print(1)
    else:
        count,sel=0,0
        tot=sum(val[0:k])
        templist=val[0:k]
        for i in range(0,len(val)):
            if templist[k-1]==val[i]:
                count+=1
        for i in range(len(templist)):
            if templist[k-1]==templist[i]:
                sel+=1
        sol=nCr(count,sel) 
        print(sol)