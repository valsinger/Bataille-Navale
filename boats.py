from coords import *
from tab import *

# Feuille avec toutes les classes objets des bateaux de l'utilisateur et du bot
# On repete les accesseurs getPv et getPlace ainsi que le mutateur setPv.
# Pour chaque bateau, on modifie les PV dans chaque initialisation, ainsi que chaque contraintes dans le mutateur setPlace
# 1 carré représente 20pv

# Bateaux de l'utilisateur

# Classe du topilleur de l'utilisateur
class torpilleurUser:
    # On definit les accesseurs et les mutateurs
    def __init__(self, pv, place):
        self._pv = 40
        self._place = []
        self._coule = False
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        # On applique les contraintes de positionnement en fonction de la taille du bateau
        if x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 2:
                return False
            else:
                for i in range(2):
                    l[x][y] = "▤"
                    x += -1
        elif direction == 2:
            if y >= 9:
                return False
            else:
                for i in range(2):
                    l[x][y] = "▤"
                    y += 1
        elif direction == 3:
            if x >= 9:
                return False
            else:
                for i in range(2):
                    l[x][y] = "▤"
                    x += 1
        elif direction == 4:
            if y < 2:
                return False
            else:
                for i in range(2):
                    l[x][y] = "▤"
                    y += -1
        return ""
    def coule():
        self._coule = True

# Classe du sous-marin de l'utilisateur:
class sousmarinUser:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if l[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 3:
                return False
            else:
                for i in range(3):
                    if l[x][y] != "~":
                        return False
                    else:
                        l[x][y] = "▥"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    if l[x][y] != "~":
                        return False
                    else:
                        l[x][y] = "▥"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    if l[x][y] != "~":
                        return False
                    else:
                        l[x][y] = "▥"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    if l[x][y] != "~":
                        return False
                    else:
                        l[x][y] = "▥"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du contre torpilleur de l'utilisateur:
class contretorpilleurUser:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if l[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 3:
                return False
            else:
                for i in range(3):
                    l[x][y] = "▦"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "▦"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "▦"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    l[x][y] = "▦"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du croiseur de l'utilisateur:
class croiseurUser:
    def __init__(self, pv, place):
        self._pv = 80
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if l[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 4:
                return False
            else:
                for i in range(4):
                    l[x][y] = "▧"
                    x += -1
        elif direction == 2:
            if y >= 7:
                return False
            else:
                for i in range(4):
                    l[x][y] = "▧"
                    y += 1
        elif direction == 3:
            if x >= 7:
                return False
            else:
                for i in range(4):
                    l[x][y] = "▧"
                    x += 1
        elif direction == 4:
            if y < 4:
                return False
            else:
                for i in range(4):
                    l[x][y] = "▧"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du porte-avions de l'utilisateur:
class porteavionsUser:
    def __init__(self, pv, place):
        self._pv = 100
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if l[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 5:
                return False
            else:
                for i in range(5):
                    l[x][y] = "▨"
                    x += -1
        elif direction == 2:
            if y >= 6:
                return False
            else:
                for i in range(5):
                    l[x][y] = "▨"
                    y += 1
        elif direction == 3:
            if x >= 6:
                return False
            else:
                for i in range(5):
                    l[x][y] = "▨"
                    x += 1
        elif direction == 4:
            if y < 5:
                return False
            else:
                for i in range(5):
                    l[x][y] = "▨"
                    y += -1
        return ""
    def coule():
        self._coule = True




# Bateaux du bot

# Classe du torpilleur du bot:
class torpilleurBot:
    def __init__(self, pv, place):
        self._pv = 40
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 2:
                return False
            else:
                for i in range(2):
                    m[x][y] = "▤"
                    x += -1
        elif direction == 2:
            if y >= 9:
                return False
            else:
                for i in range(2):
                    m[x][y] = "▤"
                    y += 1
        elif direction == 3:
            if x >= 9:
                return False
            else:
                for i in range(2):
                    m[x][y] = "▤"
                    x += 1
        elif direction == 4:
            if y < 2:
                return False
            else:
                for i in range(2):
                    m[x][y] = "▤"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du sous-marin du bot:
class sousmarinBot:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if m[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 3:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▥"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▥"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▥"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▥"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du contre torpilleur du bot:
class contretorpilleurBot:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if m[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 3:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▦"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▦"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▦"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    m[x][y] = "▦"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du croiseur du bot:
class croiseurBot:
    def __init__(self, pv, place):
        self._pv = 80
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if m[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 4:
                return False
            else:
                for i in range(4):
                    m[x][y] = "▧"
                    x += -1
        elif direction == 2:
            if y >= 7:
                return False
            else:
                for i in range(4):
                    m[x][y] = "▧"
                    y += 1
        elif direction == 3:
            if x >= 7:
                return False
            else:
                for i in range(4):
                    m[x][y] = "▧"
                    x += 1
        elif direction == 4:
            if y < 4:
                return False
            else:
                for i in range(4):
                    m[x][y] = "▧"
                    y += -1
        return ""
    def coule():
        self._coule = True


# Classe du porte-avions du bot:
class porteavionsBot:
    def __init__(self, pv, place):
        self._pv = 100
        self._place = []
    def getPv():
        return self._pv
    def setPv(pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(x, y, direction):
        if m[x][y] != "~":
            return False
        elif x > 10 or x < 1:
            return False
        elif y > 10 or y < 1:
            return False
        elif direction < 1 or direction > 4:
            return False
        elif direction == 1:
            if x < 5:
                return False
            else:
                for i in range(5):
                    m[x][y] = "▨"
                    x += -1
        elif direction == 2:
            if y >= 6:
                return False
            else:
                for i in range(5):
                    m[x][y] = "▨"
                    y += 1
        elif direction == 3:
            if x >= 6:
                return False
            else:
                for i in range(5):
                    m[x][y] = "▨"
                    x += 1
        elif direction == 4:
            if y < 5:
                return False
            else:
                for i in range(5):
                    m[x][y] = "▨"
                    y += -1
        return ""
    def coule():
        self._coule = True
