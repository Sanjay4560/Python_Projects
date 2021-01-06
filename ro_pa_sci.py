import random  
def gameWin(comp,you):   #--> Game definition
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
            
print("Comp turn: Rock(r) Paper(p) or Scissor(s) ? ")
randNo = random.randint(1,3)
# print(randNo)
if randNo==1:
    comp = 'r'
elif randNo==2:
    comp = 'p'
elif randNo==3:
    comp = 's'

you = input("Your turn: Rock(r) Paper(p) or Scissor(s) ? ")
a = gameWin(comp,you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a==None:
    print("\t********** The game is Tie **********")
elif a:
    print("\t********** You Win !!! **********")
else:
    print("\t********** You Lose!!! **********")
