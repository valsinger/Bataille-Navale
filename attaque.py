from tab import *
from boats import *


# On definie la fonction qui permettra à l'utilisateur de choisir des coordonnées sur le tableau m
def attaqueUser(x, y):
    # En fontion du type du carré unicode (un différent pour chaque type de bateau), on determinera le type du bateau du bot touché, et on lui enlevera 20pv
    if m[x][y] == "▤":
        if torpilleurBot._pv != 20:
            # Tant que le bateau a plus de 20pv, on peut lui enlever 20pv
            torpilleurBot.setPv(torpilleurBot.getPV() - 20)
            # On modifie le caractère touché du bateau par une croix sur les tableaux m et p
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            # Si le bateau touché n'a que 20pv, cela veut dire que si on lui met un coup, il coule, donc on utilise directement la fonction .coule()
            torpilleurBot.setCoule(torpilleurBot)
            # On modifie le caractère touché du bateau par une croix sur les tableaux m et p
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▥":
        if sousmarinBot._pv != 20:
            sousmarinBot.setPv(sousmarinBot.getPV() - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            sousmarinBot.setCoule(sousmarinBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▦":
        if contretorpilleurBot._pv != 20:
            contretorpilleurBot.setPv(contretorpilleurBot.getPV() - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            contretorpilleurBot.setCoule(contretorpilleurBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▧":
        if croiseurBot._pv != 20:
            croiseurBot.setPv(croiseurBot.getPV() - 20)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Touché !")
        else:
            croiseurBot.setCoule(croiseurBot)
            m[x][y] = "x"
            p[x][y] = "x"
            print("Coulé !")
    elif m[x][y] == "▨":
        if porteavionsBot._pv != 20:
            porteavionsBot.setPv(porteavionsBot.getPV() - 20)
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
