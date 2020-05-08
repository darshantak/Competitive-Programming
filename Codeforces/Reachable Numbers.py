value=int(input())
func=value+1
sol=[]
if func%10==0:
    while func>=10:
        func=func//10
        sol.append(func)
    while func%10!=0:
        func=func+1
        if func%10!=0:
            sol.append(func)
    print(len(sol))
    print(sol)
else:
    while func<
    while func%10!=10:
        if func%10!=0:
            sol.append(func)
            func+=1
    while func>=10:
        func=func//10
        if func%10!=0:
            sol.append(func)
    while func%10!=0:
        func=func+1
        if func%10!=0:
            sol.append(func)


