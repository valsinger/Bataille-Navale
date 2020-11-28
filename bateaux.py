def torpilleur(x, y, direction):
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


def sousmarin(x, y, direction):
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


def contretorpilleur(x, y, direction):
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


def croiseur(x, y, direction):
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


def porteavions(x, y, direction):
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
