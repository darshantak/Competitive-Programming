def lps(s):
    n=len(s)
    for i in range(n//2,0,-1):
        pre=s[0:i]
        suff=s[n-i:n]
        if pre==suff:
            return pre,i
    return 0

s=str(input())
prefix,index=lps(s)
temp=s[index:len(s)-index]
# print(prefix,index)
if prefix in temp:
    print(prefix)
else:
    print("Just a legend")
