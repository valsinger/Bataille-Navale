from ocean import *



def attaque(x,y):
    if m[x][y]=="■":
        m[x][y]="▢"
        p[x][y]="▢"
        return 12
    elif p[x][y]=="▢":
        return False
    elif m[x][y]=="~":
        m[x][y]="x"
        p[x][y]="x"
        return 444
    elif p[x][y]=="x":
        return False
    
def attaqueBot(x,y):
    if l[x][y]=="■":
        l[x][y]="▢"
        m[x][y]="▢"
        a,b=x,y
        return 12
    elif l[x][y]=="▢":
        return False
    elif l[x][y]=="~":
        l[x][y]="x"
        m[x][y]="x"
        return 444
    elif l[x][y]=="x":
        return False
        
        