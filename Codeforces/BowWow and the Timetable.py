import math
def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    if binary1==0:
        return 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal
def isPowerOfTwo(x): 
    if (x == 0): 
        return False
    while (x != 1): 
            if (x %4 != 0): 
                return False
            x = x// 4
              
    return True
val=int(input())
dec=binaryToDecimal(val)
if val==0:
    print(0)
    exit()
elif val==1:
    print(0)
    exit()
for i in range(0,dec):
    if pow(4,i)>dec:
        temp=i
        break
if isPowerOfTwo(dec):
    temp=temp-1
print(temp)