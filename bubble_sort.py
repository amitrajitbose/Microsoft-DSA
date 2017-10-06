#Python Program For Implementing Bubble Sort on n numbers
#This Program also returns the number of swapping steps
#import time
def bubbleSort(lst):
	n=len(lst)
	c=0
	swapped=True
	while(swapped):
	  swapped=False
	  for p in range(n-1):
	    if(lst[p]>lst[p+1]):
	      c+=1
	      temp=lst[p]
	      lst[p]=lst[p+1]
	      lst[p+1]=temp
	      swapped = True
	print (lst)
	return c

mylist=[int(x) for x in (input("ENTER NUMBERS: ").strip().split(' '))]
ci=bubbleSort(mylist)
print (ci , " swaps")
#time.sleep(5)

'''Uncomment Lines:3 and 23, if you want the console screen to wait for 5 seconds after 
   the result has been shown'''

