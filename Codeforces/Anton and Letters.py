a=list(map(str,input().split(", ")))
final_str=[]
if len(a)==1:
    if len(list(a[0]))==2:
        print(0)
        exit()
    else:
        print(1)
        exit()
if len(a)>=2:
    first=list(a[0])
    last=list(a[len(a)-1])
    first.pop(0)
    last.pop(len(last)-1)
    final_str.append(first[0])
    final_str.append(last[0])
    for i in range(1,len(a)-1):
        final_str.append(a[i])
    print(len(set(final_str)))
