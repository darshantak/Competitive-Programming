for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(0)
    elif n in [2,3]:
        print(1)
    else:
        for i in range(1,n,4):
            if n in range(2**(i+1),2**(i+2)):
                print(2)
                break
            elif n in range(2**(i+2),2**(i+3)):
                print(3)
                break
            elif n in range(2**(i+3),2**(i+4)):
                print(0)
                break
            elif n in range(2**(i+4),2**(i+5)):
                print(9) 
                break