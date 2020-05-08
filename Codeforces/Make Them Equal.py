input()
a = set(map(int, input().split()))
if len(a) > 3:
    print(-1)
elif len(a) == 1:
    print(0)
elif len(a) == 2:
    x = max(a)
    y = min(a)
    if (x-y)%2==0:
        print((x-y)//2)
    else:
        print(x-y)
else:
    max = max(a)
    a.remove(max)
    min = min(a)
    a.remove(min)
    mean, = a
    print(mean)
    if (max-mean)==(mean-min):
        print(max-mean)
    else:
        print(-1)