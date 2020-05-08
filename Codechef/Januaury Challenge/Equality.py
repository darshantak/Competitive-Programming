
def lenOfLongIncSubArr(arr, i,j) : 
	m = 1
	l = 1
	for i in range(i,j) : 

		if (arr[i] > arr[i-1]) : 
			l =l + 1
		else : 
			if (m < l) : 
				m = l 
			l = 1
	if (m < l) : 
		m = l 
	
	return m 

arr = [5, 6, 3, 5, 7, 8, 9,22,14,15,16,17,18] 
n = len(arr) 
print("Length = ", lenOfLongIncSubArr(arr, 0,4)) 

incomplete
# This code is contributed 
# by Nikita Tiwari. 
