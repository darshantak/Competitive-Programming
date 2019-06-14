n=int(input())
if n==0:
    print(0)
else:
    for i in range(n):
        x=int(input())
        if x==0:
            print(0)
        i=1
        while x>0:
            rem=x%2
            x=int(x/2)
            if rem==1:
                print(i)
                break
            i+=1