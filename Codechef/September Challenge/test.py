# def SieveOfEratosthenes(n):  
#     prime = [True for i in range(n + 1)] 
#     p = 2
#     while (p * p <= n): 
#         if (prime[p] == True): 
#             for i in range(p * 2, n + 1, p): 
#                 prime[i] = False
#         p += 1
#     prime[0]= False
#     prime[1]= False
#     temp=[1,]
#     for p in range(n + 1): 
#         if prime[p]: 
#             temp.append(p) 
#     return temp
# primes=SieveOfEratosthenes(10**6)
# for _ in range(int(input())):
#     n=int(input())    
#     if n==1:
#         print(1)
#         print(1,1)
#     else:

#         temp={}
#         day1=[]
#         for i in primes:
#             if i<=n:
#                 day1.append(i)

#         temp[1]=day1  
#         i=2
#         while i<=n:
#             if i not in primes:
#                 temp[i]=[i]
#                 if i+1 not in primes:
#                     temp[i]=[i,i+1]
#                     i+=2
#                     continue
#             i+=1
#         print(n//2)
#         for i,j in temp.items():
#             print(len(j),*j)

for _ in range(int(input())):
    n,m=map(int,input().split())
    mat=[]
    for i in range(n):
        temp=""
        if i%2==0:
            for i in range(1,m+1):
                if i%2==0:
                    temp+="W"
                else:
                    temp+="B"
        else:
            for i in range(1,m+1):
                if i%2==0:
                    temp+="B"
                else:
                    temp+="W"
        # x.append(temp)
        mat.append(temp)
    # print(mat)
    if n*m%2==0:
        temp=""
        if n%2!=0:
            for i in range(1,m):
                if i%2==0:
                    temp+="W"
                else:
                    temp+="B"
            temp+="B"
        else:
            for i in range(1,m):
                if i%2==0:
                    temp+="B"
                else:
                    temp+="W"
            temp+="B"
        mat[n-1]=temp
    for i in mat:
        print(i)
    
            
    
                     