from coords import *


# Bateaux user -----------------------------------------------------------------
class torpilleurUser:
    def __init__(self, pv, place):
        self._pv = 40
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
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
                    l[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 9:
                return False
            else:
                for i in range(2):
                    l[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 9:
                return False
            else:
                for i in range(2):
                    l[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 2:
                return False
            else:
                for i in range(2):
                    l[x][y] = "■"
                    y += -1
        return ""

class sousmarinUser:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if l[x][y] == "■":
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
                    l[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    y += -1
        return ""

class contretorpilleurUser:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if l[x][y] == "■":
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
                    l[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    y += -1
        return ""

class croiseurUser:
    def __init__(self, pv, place):
        self._pv = 80
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if l[x][y] == "■":
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
                    l[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 7:
                return False
            else:
                for i in range(4):
                    l[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 7:
                return False
            else:
                for i in range(4):
                    l[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 4:
                return False
            else:
                for i in range(4):
                    l[x][y] = "■"
                    y += -1
        return ""

class porteavionsUser:
    def __init__(self, pv, place):
        self._pv = 80
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if l[x][y] == "■":
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
                    l[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 6:
                return False
            else:
                for i in range(5):
                    l[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 6:
                return False
            else:
                for i in range(5):
                    l[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 5:
                return False
            else:
                for i in range(5):
                    l[x][y] = "■"
                    y += -1
        return ""


# Bateaux bot ------------------------------------------------------------------
class torpilleurBot:
    def __init__(self, pv, place):
        self._pv = 40
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
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
                    m[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 9:
                return False
            else:
                for i in range(2):
                    m[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 9:
                return False
            else:
                for i in range(2):
                    m[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 2:
                return False
            else:
                for i in range(2):
                    m[x][y] = "■"
                    y += -1
        return ""

class sousmarinBot:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if m[x][y] == "■":
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
                    m[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    m[x][y] = "■"
                    y += -1
        return ""

class contretorpilleurBot:
    def __init__(self, pv, place):
        self._pv = 60
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if m[x][y] == "■":
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
                    m[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 8:
                return False
            else:
                for i in range(3):
                    m[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 3:
                return False
            else:
                for i in range(3):
                    m[x][y] = "■"
                    y += -1
        return ""

class croiseurBot:
    def __init__(self, pv, place):
        self._pv = 80
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if m[x][y] == "■":
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
                    m[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 7:
                return False
            else:
                for i in range(4):
                    m[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 7:
                return False
            else:
                for i in range(4):
                    m[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 4:
                return False
            else:
                for i in range(4):
                    m[x][y] = "■"
                    y += -1
        return ""

class porteavionsBot:
    def __init__(self, pv, place):
        self._pv = 80
        self._place = []
    def getPv(self):
        return self._pv
    def setPv(self, pv):
        self._pv = pv
    def getPlace(self):
        return self._place
    def setPlace(self, x, y, direction):
        if m[x][y] == "■":
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
                    m[x][y] = "■"
                    x += -1
        elif direction == 2:
            if y >= 6:
                return False
            else:
                for i in range(5):
                    m[x][y] = "■"
                    y += 1
        elif direction == 3:
            if x >= 6:
                return False
            else:
                for i in range(5):
                    m[x][y] = "■"
                    x += 1
        elif direction == 4:
            if y < 5:
                return False
            else:
                for i in range(5):
                    m[x][y] = "■"
                    y += -1
        return ""
