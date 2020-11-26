def ocean(l):
    for i in range(len(l)):
        print("\n",l[i],)
        
    return ""

l=11*["o"]
for i in range(len(l)):
    l[i]=11*["o"]
    

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



print("")
print(ocean(l))



#lettres={chr(i+65):}
#def selection(x,y):

#~~~~

#https://fr.wikipedia.org/wiki/Table_des_caract%C3%A8res_Unicode/U2460

x=int(input("ligne(entre 0 et 9):"))
y=int(input("colonne(entre 0 et 9):"))

print(l[x][y])

l[x][y]="0"



print(ocean(l))