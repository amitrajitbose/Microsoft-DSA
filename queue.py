queue=[]
def add(value):
  v=int(value)
  queue.append(v)
  return queue
def poll():
  if(len(queue)>0):
    x=queue[0]
    queue.remove(x)
    print(x," POPPED")
    return queue
  else:
    print("EMPTY QUEUE. POP FAILED")
def peek():
  if(len(queue)==0):
    print("EMPTY QUEUE. PEEK FAILED")
    return
  print("VALUE AT FRONT OF QUEUE: ",queue[0])
  return queue
def show():
  print (queue)
  
choices={
  0:exit,
  1:add,
  2:poll,
  3:peek,
  4:show
}

while(True):
  print()
  print("Press 0 To Exit")
  print("Press 1 To Enqueue")
  print("Press 2 To Dequeue")
  print("Press 3 To Peek")
  print("Press 4 To Display Queue")
  print("Your Choice? ")
  ch=int(input())
  if(ch==1):
    val=input("ENTER VALUE TO ADD-> ")
    choices[ch](val)
  else:
    choices[ch]()