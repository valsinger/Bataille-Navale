from tab import *

from boats import *

def attaqueUser(x,y):

    if m[x][y] == "▤":
        if torpilleurBot.pv!=0:
            torpilleurBot.setPv(torpilleurBot.getPV-20)
        else:
            torpilleurBot.coule()
            print("coulé")
        torpilleurBot.setPv(torpilleurBot.getPV-20)

        m[x][y] = "x"

        p[x][y] = "x"

        print("touché")

    elif m[x][y] == "▥":
        if sousmarinBot.pv!=0:
            sousmarinBot.setPv(sousmarinBot.getPV-20)
        else:
            sousmarinBot.coule()
            print("coulé")
        sousmarinBot.setPv(sousmarinBot.getPV-20)

        m[x][y] = "x"

        p[x][y] = "x"

        print("touché")

    elif m[x][y] == "▦":
        if contretorpilleurBot.pv!=0:
            contretorpilleurBot.setPv(contretorpilleurBot.getPV-20)
        else:
            contretorpilleurBot.coule()
            print("coulé")
        m[x][y] = "x"

        p[x][y] = "x"

        print("touché!")

    elif m[x][y] == "▧":
        if croiseurBot.pv!=0:
            croiseurBot.setPv(croiseurBot.getPV-20)
        else:
            croiseurBot.coule()
            print("coulé")
        croiseurBot.setPv(croieurBot.getPV-20)

        m[x][y] = "x"

        p[x][y] = "x"

        print("touché!")

    elif m[x][y] == "▨":
        if porteavionsBot.pv!=0:
            porteavionsBot.setPv(porteavionsBot.getPV-20)
        else:
            porteavionsBot.coule()
            print("coulé")
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
         
 
