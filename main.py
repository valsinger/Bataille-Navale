# Programme de Bataille Navale créé par Valentin Singer et Aurélien Dumay

#import de tous les scripts ----------------------------------------------------
from tab import *
from coords import *
from boats import *
from bot import *
from attaque import *


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