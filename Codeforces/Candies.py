for _ in range(int(input())):
    num=int(input())
    t,a=0,0
    for j in range(2,num):
        if num%(pow(2,j)-1)==0:
            t=j
            break
    a=num//(pow(2,t)-1)
    print(a)
