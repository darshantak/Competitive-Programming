for _ in range(int(input())):
    s=input()
    count0,count1=0,0
    temp=""
    for i in s:
        if i=="0":
            count0+=1
        else:
            count1+=1
    l=list(s)
    if len(set(l))==1:
        print(s)
    elif len(set(l))==len(s):
        print(s)
    else:
        for i in range(2*len(s)):
            if i%2==0:
                temp+="1"
            else:
                temp+="0"
        print(temp)