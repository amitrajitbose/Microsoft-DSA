#Python Program For Implementing Selection Sort on n numbers
#This Program also returns the number of swapping steps
#import time
def selectionSort(lst):
	n=len(lst) #store the length of the list
	c=0
	for i in range(0,n-1):
		index=0
		s=lst[i]
		'''In this list below, we are finding the smallest value in the subset of the list
			that is from i+1 th index to n-1 th index and assign it to s and its index to
			variable index'''
		for j in range(i+1,n):
			if(lst[j]<s):
				index=j
				s=lst[j]
		if(index!=0):
			c+=1
			'''if any shifting is required, the index position would change from zero
			   and hence we will swap them'''
			lst[i],lst[index]=lst[index],lst[i]
	print (lst)
	return c

mylist=[int(x) for x in (input("ENTER NUMBERS: ").strip().split(' '))]
c=selectionSort(mylist)
print (c , " swaps")
#time.sleep(5)

'''Uncomment Lines:3 and 28, if you want the console screen to wait for 5 seconds after 
   the result has been shown'''