mod=1000000007
fact=[0]*(10**6+1)
dp=[0]*(10**6+1)
fact[1],fact[2]=1,2
dp[1],dp[2]=1,2
for i in range(3,10**6+1):
    fact[i]=((fact[i-1]%mod)*(i%mod))%mod
for i in range(3,10**6+1):
    dp[i]=((dp[i-1]%mod)*(fact[i]%mod))%mod
for _ in range(int(input())):
    n=int(input())
    print(dp[n])
