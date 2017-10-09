stack=[]
def push(value):
  v=int(value)
  stack.append(v)
  return stack
def pop():
  if(len(stack)>0):
    x=stack[-1]
    stack.pop()
    print(x," POPPED")
    return stack
  else:
    print("EMPTY STACK. POP FAILED")
def peek():
  if(len(stack)==0):
    print("EMPTY STACK. PEEK FAILED")
    return
  print("VALUE AT TOP OF STACK: ",stack[-1])
  return stack
def show():
  print (stack[::-1])
  
choices={
  0:exit,
  1:push,
  2:pop,
  3:peek,
  4:show
}

while(True):
  print()
  print("Press 0 To Exit")
  print("Press 1 To Push")
  print("Press 2 To Pop")
  print("Press 3 To Peek")
  print("Press 4 To Display Stack")
  print("Your Choice? ")
  ch=int(input())
  if(ch==1):
    val=input("ENTER VALUE TO PUSH-> ")
    choices[ch](val)
  else:
    choices[ch]()