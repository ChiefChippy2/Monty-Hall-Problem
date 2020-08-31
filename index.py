import random
def start():
  doors=[0,0,1] 
  choice,door,leftover=random.sample([0,1,2],3)
  if(door==2):
    choice,door=swap(choice,door)
  if(random.randint(0,1)==0):
    choice,leftover=swap(leftover,choice)
  print("Choice is -> "+doors[choice])
start()
  
  
