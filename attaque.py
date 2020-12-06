from tab import *from boats import *
def attaqueUser(x,y):
    if m[x][y]=="■":
        m[x][y]=="▢"
        p[x][y]=="▢"
        print("touché",x,y)
        elif m[x][y]=="▢":
            return False
            elif m[x][y]=="~":
                print("dans l'eau")          
