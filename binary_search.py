#Program to implement binary search algorithm on n numbers
#import time
def binsearch(lst,key,low,high):
  if(low>high):
    print ("NOT FOUND")
    return False
  middle=int((low+high)/2)
  if(key==lst[middle]):
    print("FOUND AT POSITION:",middle)
    return True
  elif(key>lst[middle]):
    return binsearch(lst,key,middle+1,high)
  else:
    return binsearch(lst,key,low,middle-1)
    
mylist=[int(x) for x in (input("ENTER NUMBERS: ").strip().split(' '))]
key=int(input('ENTER SEARCH ITEM: '))
binsearch(mylist,key,0,len(mylist)-1)
#time.sleep(5)

'''Uncomment Lines:2 and 19, if you want the console screen
   to wait for 5 seconds after  the result has been shown'''