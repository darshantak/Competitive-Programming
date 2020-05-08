import math

def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

for _ in range(int(input())):
    xstart,ystart=map(int,input().split())
    n,m,k=map(int,input().split())
    temp=[n,m,k]
    pts=[]
    for i in range(len(temp)):
        pts.append(list(map(int,input().split())))
    np=pts[0]
    mp=pts[1]
    kp=pts[2]
    mind=[]
    print(np,mp,kp)

    for i in range(0,len(np),2):
        for j in range(0,len(mp),2):
            mind.append(dist(np[i],np[i+1],mp[j],mp[j+1]))
    
    


    