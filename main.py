# Programme de Bataille Navale créé par Valentin Singer et Aurélien Dumay

#import de tous les scripts ----------------------------------------------------
from tab import *
from coords import *
from boats import *
from bot import *
from attaque import *


m[4][4]="■"

print(tab(l))

#BoatsBot()
print(tabBot(m))
x=int(input("x="))
y=int(input("y="))
print(attaqueUser(x,y))