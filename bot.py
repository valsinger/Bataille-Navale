from random import randint
from boats import *
from attaque import *
BotStatus = "Search"

def randomCoordinate():
    # Cette fonction va nous permettre de generer aléatoirement x, y et direction, on la rappelle quand on veut utiliser d'autres valeurs
    x = randint(1, 10)
    y = randint(1, 10)
    direction = randint(1, 4)
    return x, y, direction


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

x=0
def botAttack():
    if BotStatus == "Search":
        while attaqueBot == False:
            x, y, trash = randomCoordinate()
            attaqueBot(x, y)
        if attaqueBot(x, y) == "Touché !":
            xt0 = x
            yt0 = y
    else:
        touch = 1
        higher = xt - 1
        lower = xt + 1
        righter = yt + 1
        lefter = yt - 1
        if touch == 1:
            while attaqueBot(xt, yt) == False:
                randomSearch = randint(1, 4)
                if randomSearch == 1:
                    attaqueBot(higher, yt)
                elif randomSearch == 2:
                    attaqueBot(lower, yt)
                elif randomSearch == 3:
                    attaqueBot(xt, righter)
                else:
                    attaqueBot(xt, lefter)
            if attaqueBot(x, y) == "Touché !":
                touch += 1
        if touch > 1:
            while attaqueBot(xt, yt) == False:
                randomSearch = randint(1, 2)
                if xt == xt0:
                    if yt > yt0:
                        if randomSearch == 1:
                           attaqueBot(xt, yt + 1)
                        else:
                           attaqueBot(xt, yt - 2)
                    else:
                        if randomSearch == 1:
                            attaqueBot(xt, yt - 1)
                        else:
                            attaqueBot(xt, yt + 2)
                else:
                    if xt > xt0:
                        if randomSearch == 1:
                            attaqueBot(xt + 1, yt)
                        else:
                            attaqueBot(xt - 2, yt)
                    else:
                        if randomSearch == 1:
                            attaqueBot(xt - 1, yt)
                        else:
                            attaqueBot(xt + 2, yt)
    return True
