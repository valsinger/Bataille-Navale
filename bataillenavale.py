def ocean(l):
    for i in range(len(l)):
        print("\n",l[i],)
        
    return ""

l = 11 * ["~"]

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

def porteAvion(x, y, direction):
    if x > 10 or x < 1:
        return False
    elif y > 10 or y < 1:
        return False
    elif direction < 1 or direction > 4:
        return False
    elif direction == 1:
        if x < 5:
            return False
        else:
            for i in range (5):
                l[x][y] = "■"
                x -= 1
    elif direction == 2:
        if y > 5:
            return False
        else:
            for i in range(5):
                l[x][y] = "■"
                y += 1
    elif direction == 3:
        if x > 5:
            return False
        else:
            for i in range(5):
                l[x][y] = "■"
    elif direction == 4:
        if y < 5:
            return False
        else:
            for i in range(5):
                l[x][y] = "■"
                y -= 1
    return ""

porteAvion(6, 5, 2)

print (" ")
print(ocean(l))



#lettres={chr(i+65):}
#def selection(x,y):

#~~~~

#https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode/U2460
