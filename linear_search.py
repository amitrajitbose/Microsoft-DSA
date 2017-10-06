#Python programme to implement linear search
#import time
def linearSearch(lst,key):
	for i in range(len(lst)):
		if(lst[i]==key):
			print("found! It is at ", i)
			return
	print("the element is not in the array")

mylist=[int(x) for x in (input("ENTER NUMBERS: ").strip().split(' '))]
k=int(input("ENTER SEARCH ITEM: "))
linearSearch(mylist,k)
#time.sleep(5)

'''Uncomment Lines:2 and 13, if you want the console screen to wait for 5 seconds after 
   the result has been shown'''