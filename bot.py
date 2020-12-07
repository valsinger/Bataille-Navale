from random import randint
from boats import *


def randomCoordinate():
    # Cette fonction va nous permettre de generer aléatoirement x, y et direction, on la rappelle quand on veut utiliser d'autres valeurs
    x = randint(1, 10)
    y = randint(1, 10)
    direction = randint(1, 4)
    return x, y, direction

def BoatsBot():
    x, y, z = randomCoordinate()
    while torpilleurBot.setPlace(torpilleurBot, x, y, direction) != True:
        x, y, z = randomCoordinate()
        torpilleurBot.setPlace(torpilleurBot, x, y, direction)
    while sousmarinBot.setPlace(sousmarinBot, x, y, direction) != True:
        x, y, z = randomCoordinate()
        torpilleurBot.setPlace(sousmarinBot, x, y, direction)
    while contretorpilleurBot.setPlace(contretorpilleurBot, x, y, direction) != True:
        x, y, z = randomCoordinate()
        contretorpilleurBot.setPlace(contretorpilleurBot, x, y, direction)
    while croiseurBot.setPlace(croiseurBot, x, y, direction) != True:
        x, y, z = randomCoordinate()
        croiseurBot.setPlace(croiseurBot, x, y, direction)
    while porteavionsBot.setPlace(porteavionsBot, x, y, direction) != True:
        x, y, z = randomCoordinate()
        porteavionsBot.setPlace(porteavionsBot, x, y, direction)
    return True
