from tab import *
from boats import *


# On definie la fonction qui permettra à l'utilisateur de choisir des coordonnées sur le tableau m
def attaqueUser(x, y):
    # En fontion du type du carré unicode (un différent pour chaque type de bateau), on determinera le type du bateau du bot touché, et on lui enlevera 20pv
    if m[x][y] == "▤":
        if torpilleurBot.getPv(torpilleurBot) != 20:
            # Tant que le bateau a plus de 20pv, on peut lui enlever 20pv
            torpilleurBot.setPv(torpilleurBot.getPV(torpilleurBot) - 20)
            # On modifie le caractère touché du bateau par une croix sur les tableaux m et p
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            # Si le bateau touché n'a que 20pv, cela veut dire que si on lui met un coup, il coule, donc on utilise directement la fonction .setCoule()
            torpilleurBot.setCoule(torpilleurBot)
            # On modifie le caractère touché du bateau par une croix sur les tableaux m et p
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▥":
        if sousmarinBot.getPv(sousmarinBot) != 20:
            sousmarinBot.setPv(sousmarinBot.getPV(sousmarinBot) - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            sousmarinBot.setCoule(sousmarinBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▦":
        if contretorpilleurBot.getPv(contretorpilleurBot) != 20:
            contretorpilleurBot.setPv(contretorpilleurBot.getPV(contretorpilleurBot) - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            contretorpilleurBot.setCoule(contretorpilleurBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▧":
        if croiseurBot.getPv(croiseurBot) != 20:
            croiseurBot.setPv(croiseurBot.getPV(croiseurBot) - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            croiseurBot.setCoule(croiseurBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▨":
        if porteavionsBot.getPv(porteavionsBot) != 20:
            porteavionsBot.setPv(porteavionsBot.getPV(porteavionsBot) - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            porteavionsBot.setCoule(porteavionsBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    # Si la coordonnée saisie à deja été saisie, donc que le caractère a dejà été changé, donc on retourne False, ce qui demandera à l'utilisateur de saisir de noucelles valeurs
    elif m[x][y] == "x" or m[x][y] == "o":
        return False
    # Si le tir de l'utilisateur atterir dans l'eau, on modifie le caractère et on previent l'utilisateur que rien n'a été touché
    elif m[x][y] == "~":
        m[x][y] = "o"
        p[x][y] = "o"
        print("Dans l'eau !")
        

# On definie la fonction qui permettra au bot de choisir des coordonnées sur le tableau l
def attaqueBot(x, y):
    # En fontion du type du carré unicode (un différent pour chaque type de bateau), on determinera le type du bateau de l'utilisateur touché, et on lui enlevera 20pv
    if l[x][y] == "▤":
        if torpilleurUser.getPv(torpilleurUser) != 20:
            # Tant que le bateau a plus de 20pv, on peut lui enlever 20pv
            torpilleurUser.setPv(torpilleurUser.getPV(torpilleurUser) - 20)
            # On modifie le caractère touché du bateau par une croix sur le tableau l
            l[x][y] = "x"
            return "Touché !"
            BotStatus = "Sniper"
            xt = x
            yt = y
        else:
            # Si le bateau touché n'a que 20pv, cela veut dire que si on lui met un coup, il coule, donc on utilise directement la fonction .setCoule()
            torpilleurUser.setCoule(torpilleurUser)
            # On modifie le caractère touché du bateau par une croix sur le tableau l
            l[x][y] = "x"
            return "Coulé !"
            BotStatus = "Search"
    elif l[x][y] == "▥":
        if sousmarinUser.getPv(sousmarinUser) != 20:
            sousmarinUser.setPv(sousmarinUser.getPV(sousmarinUser) - 20)
            l[x][y] = "x"
            return "Touché !"
            BotStatus = "Sniper"
            xt = x
            yt = y
        else:
            sousmarinUser.setCoule(sousmarinUser)
            l[x][y] = "x"
            return "Coulé !"
            BotStatus = "Search"
    elif l[x][y] == "▦":
        if contretorpilleurUser.getPv(contretorpilleurUser) != 20:
            contretorpilleurUser.setPv(contretorpilleurUser.getPV(contretorpilleurUser) - 20)
            l[x][y] = "x"
            return "Touché !"
            BotStatus = "Sniper"
            xt = x
            yt = y
        else:
            contretorpilleurUser.setCoule(contretorpilleurUser)
            l[x][y] = "x"
            return "Coulé !"
            BotStatus = "Search"
    elif l[x][y] == "▧":
        if croiseurUser.getPv(croiseurUser) != 20:
            croiseurUser.setPv(croiseurUser.getPV(croiseurUser) - 20)
            l[x][y] = "x"
            return "Touché !"
            BotStatus = "Sniper"
            xt = x
            yt = y
        else:
            croiseurUser.setCoule(croiseurUser)
            l[x][y] = "x"
            return "Coulé !"
            BotStatus = "Search"
    elif l[x][y] == "▨":
        if porteavionsUser.getPv(porteavionsUser) != 20:
            porteavionsUser.setPv(porteavionsUser.getPV(porteavionsUser) - 20)
            l[x][y] = "x"
            return "Touché !"
            BotStatus = "Sniper"
            xt = x
            yt = y
        else:
            porteavionsUser.setCoule(porteavionsUser)
            l[x][y] = "x"
            return "Coulé !"
            BotStatus = "Search"
    # Si la coordonnée saisie à deja été saisie, donc que le caractère a dejà été changé, donc on retourne False, ce qui demandera à l'utilisateur de saisir de noucelles valeurs
    elif l[x][y] == "x" or l[x][y] == "o":
        return False
    # Si le tir de l'utilisateur atterir dans l'eau, on modifie le caractère et on previent l'utilisateur que rien n'a été touché
    elif l[x][y] == "~":
        l[x][y] = "o"
        return "Dans l'eau !"    
        
        

