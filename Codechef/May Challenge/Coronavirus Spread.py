author="DarshanMohan"
import sys
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(MAP()) 
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7
#returns (a + b) mod c
def add(a,b,c):
	res=a+b
	if(res>=c):
		return res-c
	else:
		return res
#returns (a * b) mod c
def mod(a,b,c):
	res=a*b
	if(res>=c):
		return res%c
	else:
		return res
#Complexity: O(max(log2(a), log2(b)))
def gcd(a,b):
	while b:
		a,b=b,a%b
	return a
#Complexity: O(max(log2(a), log2(b)))
def lcm(a,b):
	w=a//gcd(a,b)
	return w*b
def expo(a,b):
	x,y=1,a
	while(b>0):
		if(b&1):
			x=x*y
		y=y*y
		b>>=1
	return x

for _ in range(int(input())):
    num=int(input())
    x=list(map(int,input().split()))
    countarr=[]
    temp=1
    i=0
    while i<num-1:
        if x[i+1]-x[i]<=2:
            temp+=1
        else:
            countarr.append(temp)
            temp=1
        i+=1
    countarr.append(temp)
    print(min(countarr),max(countarr))