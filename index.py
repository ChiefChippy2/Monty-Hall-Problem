import random
true=True
false=False
def start():
  isSwap=false;
  doors=[0,0,1] 
  choice,door,leftover=random.sample([0,1,2],3)
  if(door==2):
    choice,door=swap(choice,door)
  print("You chose door #"+str(choice)+", host opened door #"+str(door))
  if(random.randint(0,1)==0):
    print("Swapped")
    isSwap=true
    choice,leftover=swap(choice,leftover)
  print("Choice is -> "+str(doors[choice]))
  return [isSwap,doors[choice]]
def swap(x,y):
  return [y,x]
tys,tun,unswap,yswap=0,0,0,0
for i in range(100):
  result=start()
  if(result[0]):
    tun+=1
  else:
    tys+=1
  if(result[1]!=1):
    continue
  if(result[0]):
    unswap+=1
  else:
    yswap+=1
print("Times that contestant won without swapping : "+str(unswap/tun)+", and times that contestant won with swapping "+str(yswap/tys))
