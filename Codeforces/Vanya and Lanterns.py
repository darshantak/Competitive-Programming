n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
x=0 in a
y=l in a
if x & y:
    mini=0
    for i in range(n-1):
        diff=a[i+1]-a[i]
        if diff>mini:
            mini=diff
    print("{:.9f}".format(mini/2))
    
elif x or y:
    mini=0
    for i in range(n-1):
        diff=a[i+1]-a[i]
        if diff>mini:
            mini=diff
    if 0 in a:
        if l-a[n-1]>mini/2:
            print("{:.9f}".format(l-a[0]))
        else:
            print("{:.9f}".format(mini/2))
    else:
        
        if a[0]-0>mini/2:
            print("{:.9f}".format(a[0]-0))
        else:
            print("{:.9f}".format(mini/2))
        
else:
    # print(0)
    mini=0
    for i in range(n-1):
        diff=a[i+1]-a[i]
        if diff>mini:
            mini=diff
    start=a[0]-0
    end=l-a[n-1]
    # print(start,end)
    if start>=mini/2 and start>=end:
        # print(1)
        print("{:.9f}".format(start))
    elif end>mini/2 and end>start:
        # print(2)
        print("{:.9f}".format(end))
    else:
        print("{:.9f}".format(mini/2))

