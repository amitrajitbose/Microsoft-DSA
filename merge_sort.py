#Program to implement merge sort algorithm on n unsorted numbers
#import time
def merge(left,right):
  i,j=0,0
  result=[]
  while(i<len(left) and j<len(right)):
    if(left[i]<right[j]):
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  #For adding the remaining elements into result
  #Either of the following two while loops will execute
  while(i<len(left)):
    result.append(left[i])
    i+=1
  while(j<len(right)):
    result.append(right[j])
    j+=1
  return (result)
  
def mergeSort(lst):
  n=len(lst)
  if n == 0 or n == 1:
      return lst
  mid=int(n/2)
  #creating the two subarrays by 'slicing of lists method'
  left=lst[:mid]
  right=lst[mid:]
  #recursive call to both halves
  #splitting
  left=mergeSort(left)
  right=mergeSort(right)
  #combining
  r=(merge(left,right))
  return (r)
  
mylist=[int(x) for x in (input("ENTER NUMBERS: ").strip().split(' '))]
print (mergeSort(mylist))
#time.sleep(5)

'''Uncomment Lines:2 and 41, if you want the console screen to wait for 5 seconds after 
   the result has been shown'''