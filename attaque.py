from ocean import *


def attaqueUser(x,y):
    if m[x][y]=="■":
        m[x][y]=="▢"
        p[x][y]=="▢"
        print("touché",x,y)
    elif m[x][y]=="▢":
        print("déja fait")
        return attaqueUser
    elif m[x][y]=="~":
        print("dans l'eau")