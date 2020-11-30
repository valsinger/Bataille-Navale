from random import randint
from placement import *
from attaque import *

# placement --------------------------------------------------------------------
def attaqueAuto(): 
    x=randint(1, 10)
    y=randint(1, 10)
    while attaqueBot == False:
        if a == x:
            z = randint(1, 4)
            if z == 1:
                attaqueBot(a-1, b)
            elif z == 2:
                attaqueBot(a+1, b)
            elif z == 3:
                attaqueBot(a, b-1)
            elif z == 4:
                attaqueBot(a, b+1)
            else:    
                x=randint(1, 10)
                y=randint(1, 10)
                x=randint(1, 10)
                attaqueBot(x, y)
        