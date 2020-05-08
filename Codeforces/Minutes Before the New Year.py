for t in range(int(input())):
    h,m=map(int,input().split())
    total_mins=h*60+m
    print(1440-total_mins)
