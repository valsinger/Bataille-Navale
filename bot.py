from random import randint
from placement import *

# placement --------------------------------------------------------------------
def placerbot():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 4)
    while torpilleurBot(a, b, c) == False:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 4)
        torpilleurBot(a, b, c)
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 4)
    while sousmarinBot(a, b, c) == False:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 4)
        sousmarinBot(a, b, c)
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 4)
    while contretorpilleurBot(a, b, c) == False:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 4)
        contretorpilleurBot(a, b, c)
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 4)
    while croiseurBot(a, b, c) == False:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 4)
        croiseurBot(a, b, c)
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 4)
    while porteavionsBot(a, b, c) == False:
        a = randint(1, 10)
        b = randint(1, 10)
        c = randint(1, 4)
        porteavionsBot(a, b, c)
