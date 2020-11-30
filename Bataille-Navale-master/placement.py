from coords import *

# placement du Torpilleur par l'utilisateur avec restrictions ------------------
def torpilleurUser(x, y, direction):
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

# placement du Sous-marin par l'utilisateur avec restrictions ------------------
def sousmarinUser(x, y, direction):
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

# placement du Contretorpilleur par l'utilisateur avec restrictions ------------
def contretorpilleurUser(x, y, direction):
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

# placement du croiseur par l'utilisateur avec restrictions --------------------
def croiseurUser(x, y, direction):
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

# placement du Porte avion par l'utilisateur avec restrictions -----------------
def porteavionsUser(x, y, direction):
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

# Placement pour le bot ========================================================

# placement du Torpilleur par le bot avec restrictions -------------------------
def torpilleurBot(x, y, direction):
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

# placement du Sous-marin par le bot avec restrictions -------------------------
def sousmarinBot(x, y, direction):
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

# placement du Contretorpilleur par le bot avec restrictions -------------------
def contretorpilleurBot(x, y, direction):
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

# placement du croiseur par le bot avec restrictions ---------------------------
def croiseurBot(x, y, direction):
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

# placement du Porte avion par le bot avec restrictions ------------------------
def porteavionsBot(x, y, direction):
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
