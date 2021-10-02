import random
def gamewin(comp,you):
    if comp == you:
        return None

    elif comp =="s":
        if you =="w":
            return False
        elif you =="g":
            return True
    
    elif comp =="w":
        if you =="g":
            return False
        elif you =="s":
            return True        

    
    elif comp =="g":
        if you =="s":
            return False
        elif you =="w":
            return True

print('comp turn: snack(s) water(w) or gun(g)?')
a = random.randint(1,3)
if a == 1:
    comp = "s"
elif a== 2:
    comp = "w"
elif a ==3:
    comp = "g"

you = input('your turn: snack(s) water(w) or gun(g)? : ')

print(f'comp chose: {comp}')
print(f'you chose: {you}')
s = gamewin(comp,you)
print(s)
if s==None:
    print('the game is tie!')
elif s:
    print('you win!')
else:
    print('you loss!')
