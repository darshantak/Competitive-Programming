tc= int(input())
 
for _ in range(tc):
    a,b,c= map(int, input().split())
    count=0
    while c>1 and b>0:
        count+=3
        c-=2
        b-=1
    
    while a>0 and b>1:
        count+=3
        a-=1
        b-=2
            
    print(count)