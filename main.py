# Programme de Bataille Navale créé par Valentin Singer et Aurélien Dumay

# import de tous les scripts ---------------------------------------------------
from tab import *
from coords import *
from boats import *
from bot import *
from attaque import *
from grille import *
from random import *


print("__________         __         .__.__  .__            _______                      .__          ")
print("\______   \_____ _/  |______  |__|  | |  |   ____    \      \ _____ ___  _______  |  |   ____  ")
print(" |    |  _/\__  \\   __\__  \ |  |  | |  | _/ __ \   /   |   \\__  \\  \/ /\__  \ |  | _/ __ \ ")
print(" |    |   \ / __ \|  |  / __ \|  |  |_|  |_\  ___/  /    |    \/ __ \\   /  / __ \|  |_\  ___/ ")
print(" |______  /(____  /__| (____  /__|____/____/\___  > \____|__  (____  /\_/  (____  /____/\___  >")
print("        \/      \/          \/                  \/          \/     \/           \/          \/ ")



# Initialisiation du jeu
BotStatus = "Search"
# création du tableau + placement des bateaux du bot
# fonction de placement des bateaux du joueur
bateaux_joueur = 5
bateaux_bot = 5

# Phase de jeu
# Boucle entre 1a et 1b jusqu'à ce qu'il y ait un gagnant
#1a - joueur
    # Lecture de coornonnées du shoot (entré par l'utilisatuer)
    # Feedback Touché/Dans l'eau (affichage + uptade du nombre de bateaux pour le bot)

#1b - bot
    # Tirage des coordonnées du shoot
    # Feedback du bot (affichage + uptade du nombre de bateaux pour le joueur)
    # Changement du statut (Attention, il faut des conditions subtiles)
        # Si coulé : BotStatus = "Search"
        # Si touché : BotStatus = "Sniper"


#BoatsBot()
#print(tabBot(m))

#Programme qui va choisir au hasard une des grilles du bot

a=randint(1,5)

if a == 1:
    grille1Bot()
elif a == 2:
    grille2Bot()
elif a == 3:
    grille3Bot()
elif a == 4:
    grille4Bot()
elif a == 5:
    grille5Bot()

ligne = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}

orientation = {"haut": 1, "droite": 2, "bas": 3, "gauche": 4}

print(tab(l))
x = 0
y = 0
direction = 0


#torpilleurUser.setPlace(x, y, direction)

print("Placement du torpilleur (deux cases)")
while torpilleurUser.setPlace(x, y, direction) == False:
    while True:
        try:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
            break
        except KeyError:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
    while True:
        try:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            break
        except ValueError:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
    while True:
        try:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            break
        except KeyError:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            torpilleurUser.setPlace(x, y, direction)
    print("Les coordonées que vous avez entré ne fonctionnent pas, veuillez recommencer.")
    
print(tab(l))

x = 0
y = 0
direction = 0

sousmarinUser.setPlace(x, y, direction)

print("Placement du sous-marin (trois cases)")
while sousmarinUser.setPlace(x, y, direction) == False:
    while True:
        try:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
            break
        except KeyError:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
    while True:
        try:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            break
        except ValueError:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
    while True:
        try:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            break
        except KeyError:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            sousmarinUser.setPlace(x, y, direction)
    print("Les coordonées que vous avez entré ne fonctionnent pas, veuillez recommencer.")

print(tab(l))

x = 0
y = 0
direction = 0

contretorpilleurUser.setPlace(x, y, direction)

print("Placement du contre-torpillieur (trois cases)")
while contretorpilleurUser.setPlace(x, y, direction) == False:
    while True:
        try:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
            break
        except KeyError:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
    while True:
        try:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            break
        except ValueError:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
    while True:
        try:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            break
        except KeyError:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            contretorpilleurUser.setPlace(x, y, direction)
    print("Les coordonées que vous avez entré ne fonctionnent pas, veuillez recommencer.")

print(tab(l))

x = 0
y = 0
direction = 0

croiseurUser.setPlace(x, y, direction)

print("Placement du croiseur (quatre cases)")
while croiseurUser.setPlace(x, y, direction) == False:
    while True:
        try:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
            break
        except KeyError:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
    while True:
        try:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            break
        except ValueError:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
    while True:
        try:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            break
        except KeyError:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            croiseurUser.setPlace(x, y, direction)
    print("Les coordonées que vous avez entré ne fonctionnent pas, veuillez recommencer.")

print(tab(l))

x = 0
y = 0
direction = 0

porteavionsUser.setPlace(x, y, direction)

print("Placement du porte-avions (cinq cases)")
while porteavionsUser.setPlace(x, y, direction) == False:
    while True:
        try:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
            break
        except KeyError:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
    while True:
        try:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            break
        except ValueError:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
    while True:
        try:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            break
        except KeyError:
            direction = orientation[input("Entrez une direction (haut, droite, bas, gauche): ")]
            porteavionsUser.setPlace(x, y, direction)
    print("Les coordonées que vous avez entré ne fonctionnent pas, veuillez recommencer.")

print(tab(l))


#Phase d'attaque:
    

print("Entrée en combat !","\n")

while isAliveBot() != True and isAliveUser() != True:
    print("Tableau de visée")
    print(tabBotForUser(p))
    print("Tableau de l'utilisateur")
    print(tab(l))
    while True:
        try:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
            break
        except KeyError:
            x = ligne[input("Entrez une ligne (entre A et J): ")]
    while True:
        try:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            break
        except ValueError:
            y = int(input("Entrez une colonne (Entre 1 et 10): "))
            attaqueUser(x, y)
    x = randint(1,10)
    y = randint(1,10)
    attaqueBot(x, y)
    
    
#Fin de partie:
    #if isAliveBot() == False:
        #print("Vous avez gagné !)
    #elif isAliveUser() == False:
        #print("Vous Avez perdu !)
    

    


