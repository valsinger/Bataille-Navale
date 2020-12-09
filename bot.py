from random import randint
from boats import *


def randomCoordinate():
    # Cette fonction va nous permettre de generer aléatoirement x, y et direction, on la rappelle quand on veut utiliser d'autres valeurs
    x = randint(1, 10)
    y = randint(1, 10)
    direction = randint(1, 4)
    return x, y, direction

def grille1Bot():
    torpilleurBot.setPlace(1,2,3)
    sousmarinBot.setPlace(7,7,4)
    contretorpilleurBot.setPlace(3,10,3)
    croiseurBot.setPlace(10,1,2)
    porteavionsBot.setPlace(8,2,1)

def BoatsBot():
    x, y, direction = randomCoordinate()
    while torpilleurBot.setPlace(x, y, direction) != True:
        x, y, direction = randomCoordinate()
        torpilleurBot.setPlace(x, y, direction)
    while sousmarinBot.setPlace(x, y, direction) != True:
        x, y, direction = randomCoordinate()
        sousmarinBot.setPlace(x, y, direction)
    while contretorpilleurBot.setPlace(x, y, direction) != True:
        x, y, direction = randomCoordinate()
        contretorpilleurBot.setPlace(x, y, direction)
    while croiseurBot.setPlace(x, y, direction) != True:
        x, y, direction = randomCoordinate()
        croiseurBot.setPlace(x, y, direction)
    while porteavionsBot.setPlace(x, y, direction) != True:
        x, y, direction = randomCoordinate()
        porteavionsBot.setPlace(x, y, direction)
    return True
