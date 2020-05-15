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
def SWAP(a,b): 
    a,b=b,a
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
#returns a^b
#Complexity: O(log2(b))
def expo(a,b):
	x,y=1,a
	while(b>0):
		if(b&1):
			x=x*y
		y=y*y
		b>>=1
	return x
#return (a ^ b) mod m
#Complexity: O(log2(b))
def power(a,b,m):
	x,y=1,1
	while(b>0):
		if(b&1):
			x=mod(x,y,m)
		y=mod(y,y,m)
		b>>=1
	return x
#returns (a ^ (-1)) mod m
#works only for m = prime
#Complexity: O(log2(m))
def inv(a,m):
	return power(a,m-2,m)
def mod_inverse(a, n):
	N = n
	xx = 0
	yy = 1
	y = 0
	x = 1
	while(n > 0):
		q = a // n
		t = n
		n = a % n
		a = t
		t = xx
		xx = x - q * xx
		x = t
		t = yy
		yy = y - q * yy
		y = t
	x %= N
	x += N
	x %= N
	return x 

for _ in range(int(input())):
    n,k=MAP()
    a=LIST()
    b=LIST()
    a.sort()
    temp=0
    b.sort(reverse=True)
    if k>0:
        for i in range(n):
            if a[i]<b[i]:
                a[i]=b[i]
                temp+=1
            if temp==k:
                break
    # print(a)
    print(sum(a))  