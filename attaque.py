from tab import *
from boats import *

def attaqueUser(x,y):
    if m[x][y] == "▤":
        torpilleurBot.setPv(torpilleurBot.getPV-20)
        m[x][y] == "x"
        p[x][y] = "x"
        print("touché")
    elif m[x][y] == "▥":
        sousmarinBot.setPv(sousmarinBot.getPV-20)
        m[x][y] = "x"
        p[x][y] = "x"
        print("touché")
    elif m[x][y] == "▦":
        contretorpilleurBot.setPv(contretorpilleurBot.getPV-20)
        m[x][y] = "x"
        p[x][y] = "x"
        print("touché!")
    elif m[x][y] == "▧":
        croiseurBot.setPv(croieurBot.getPV-20)
        m[x][y] = "x"
        p[x][y] = "x"
        print("touché!")
    elif m[x][y] == "▨":
        porteavionsBot.setPv(porteavionsBot.getPV-20)
        m[x][y] = "x"
        p[x][y] = "x"
        print("touché!")
    elif m[x][y] == "x" or m[x][y] == "o":
        return False
    elif m[x][y] == "~":
        m[x][y] = "o"
        p[x][y] = "o"
        print("Dans l'eau!")          
