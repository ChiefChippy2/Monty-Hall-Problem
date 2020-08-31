import random
def start():
  doors=[0,0,1] 
  choice,door,leftover=random.sample([0,1,2],3)
  if(door==2):
    choice,door=swap(choice,door)
  print("You chose door #"+str(choice)+", host opened door #"+str(door))
  if(random.randint(0,1)==0):
    print("Swapped")
    choice,leftover=swap(leftover,choice)
  print("Choice is -> "+str(doors[choice]))
def swap(x,y):
  return [y,x]
for i in range(10):
  start()
  
