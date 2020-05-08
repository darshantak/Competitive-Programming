def isPowerOfTen(n): 
    if (n == 0): 
        return False
    while (n != 1): 
        if (n % 10 != 0): 
            return False
        n = n // 10
              
    return True
def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
        if (n % 20 != 0): 
            return False
        n = n // 20
              
    return True
for i in range(int(input())):
    n=int(input())
    flag=0
    while n>=10:
        if isPowerOfTen(n)==True:
            flag=1
            break
        elif isPowerOfTwo(n)==True:
            flag=1
            break
        else:
            n=n//20
    
    if flag==1:
        print("Yes")
    else:
        print("No")

        