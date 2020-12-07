from tab import *
from boats import *
# Modifications des tableaux (principalement graphiques) - faciliter la lecture

#On crée la variable qui sera repetée par la fonction tableau qui affiche le tableau de l'utilisateur 
l = 11 * ["~"]
for i in range(len(l)):
    l[i] = 11 * ["~"]
    
#Modifications de la première des 11 lignes du tableau, où on affichera le numéro de la colonne, facilitant la lecture par l'utilisateur
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

#Modifications des premières valeurs de chaque ligne du tableau , où on affichera la lettre de la lignes, facilitant la lecture par l'utilisateur
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

#On crée la variable qui sera repetée par la fonction tableau qui n'affichera pas le tableau à l'utilisateur, mais qui permettra au bot de placer ses bateaux
m = 11 * ["~"]
for i in range(len(m)):
    m[i] = 11 * ["~"]

#On crée la variable qui sera repetée par la fonction tableau qui affichera le tableau des coups joués
p = 11 * ["~"]
for i in range(len(p)):
    p[i] = 11 * ["~"]

#Modifications de la première des 11 lignes du tableau, où on affichera le numéro de la colonne, facilitant la lecture par l'utilisateur
p[0][0] = " "
p[0][1] = "1"
p[0][2] = "2"
p[0][3] = "3"
p[0][4] = "4"
p[0][5] = "5"
p[0][6] = "6"
p[0][7] = "7"
p[0][8] = "8"
p[0][9] = "9"
p[0][10] = "10"

#Modifications des premières valeurs de chaque ligne du tableau , où on affichera la lettre de la lignes, facilitant la lecture par l'utilisateur
p[1][0] = "A"
p[2][0] = "B"
p[3][0] = "C"
p[4][0] = "D"
p[5][0] = "E"
p[6][0] = "F"
p[7][0] = "G"
p[8][0] = "H"
p[9][0] = "I"
p[10][0] = "J"
