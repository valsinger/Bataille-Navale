def ocean(l):
    for i in range(len(l)):
        print("\n",l[i],)
       
    return ""

l=11*["~"]
for i in range(len(l)):
    l[i]=11*["~"]
   

l[0][0] = " "
l[0][1] = "1"
l[0][2] = "2"
l[0][3] = "3"
l[0][4] = "4"
l[0][5] = "5"
l[0][6] = "6"
l[0][7] = "7"
l[0][8] = "8"
l[0][9] = "9"
l[0][10] = "10"
   
l[1][0] = "A"
l[2][0] = "B"
l[3][0] = "C"
l[4][0] = "D"
l[5][0] = "E"
l[6][0] = "F"
l[7][0] = "G"
l[8][0] = "H"
l[9][0] = "I"
l[10][0] = "J"

print(ocean(l))

class sousmarin:
    def __init__(self,pv,x,y,direction):
        self._pv=60
        self._x=0
        self._y=0
        self._direction=0
    def getPv(self):
        return self._pv
    def setPv(self,p):
        self._pv=60
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getdirection(self):
        return self._direction
    def setx(self,x):
        self._x=int(input("ligne(entre 1 et 10):"))
        if x>10 or x<1:
            return "entrez une ligne valide"
    def sety(self,y):
        self._y=int(input("colonne(entre 1 et 10):"))
        if y>10 or y<1:
            return "entrez une colonne valide"
    def setdirection(self,direction):
        x=self._x
        y=self._y
        self.direction=int(input("1=haut 2=droite 3=bas 4=gauche: "))
        if l[x][y]=="■":
            print("impossible",x=int(input("ligne(entre 1 et 10):")),y=int(input("colonne(entre 1 et 10):")),direction=int(input("1=haut 2=droite 3=bas 4=gauche: ")))    
        elif direction<1 or direction>4:
            return "entrez une direction valide"
        elif direction==1:
            if x<3:
                return "impossible"
            else:
                for i in range(3):
                    l[x][y]="■"
                    x +=-1
        elif direction==2:
            if y >= 8:
                return False
            else:
                for i in range(3):
                    l[x][y] = "■"
                    y += 1
            if y>=8:
                return "impossible"
            else:
                for i in range(3):
                    l[x][y]="■"
                    y +=1
        elif direction==3:
            if x>=8:
                return "impossible"
            else:
                for i in range(3):
                    l[x][y]="■"
                    x +=1
        elif direction==4:
            if y<3:
                return "impossible"
            else:
                for i in range(3):
                    l[x][y]="■"
                    y+=-1    
        return ""
    

x=int(input("ligne(entre 1 et 10):"))
y=int(input("colonne(entre 1 et 10):"))
direction=int(input("1=haut 2=droite 3=bas 4=gauche: "))    
s=sousmarin(60,x,y,direction)
print(ocean(l))
        
