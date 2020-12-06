from coords import *
from random import randint
from boats import *

def BoatsBot():
    x = randint(1, 10)
    y = randint(1, 10)
    z = randint(1, 4)
    while torpilleurBot.setPlace(torpilleurBot, x, y, z) != True:
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 4)
    torpilleurBot.setPlace(torpilleurBot, x, y, z)
    while sousmarinBot.setPlace(sousmarinBot, x, y, z) != True:
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 4)
    torpilleurBot.setPlace(sousmarinBot, x, y, z)
    while contretorpilleurBot.setPlace(contretorpilleurBot, x, y, z) != True:
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 4)
    contretorpilleurBot.setPlace(contretorpilleurBot, x, y, z)
    while croiseurBot.setPlace(croiseurBot, x, y, z) != True:
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 4)
    croiseurBot.setPlace(croiseurBot, x, y, z)
    while porteavionsBot.setPlace(porteavionsBot, x, y, z) != True:
        x = randint(1, 10)
        y = randint(1, 10)
        z = randint(1, 4)
    porteavionsBot.setPlace(porteavionsBot, x, y, z)
