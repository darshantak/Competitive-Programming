n,m,k=map(int,input().split())
freq={}
rows=[]
cols=[]
for i in range(k):
    a=list(map(int,input().split()))
    rows.append(a[0])
    cols.append(a[1])
def CountFrequency(my_list): 
	freq = {} 
	for i in my_list:
        freq[i]=my_list.count(i)
    for i in freq.items():
        print(i)
	