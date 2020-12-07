from coords import *
# Feuille des fonctions qui permettront d'afficher ou non les tableaux
# Le tableau m ne sera jamais affiché à l'utilisateur

# Tableau de l'utilisateur, sur lequel il va placer ses bateaux 
def tab(l):
    for i in range(len(l)):
        print("\n", l[i], )
    return ""

# Tableau du bot, où ses bateaux seront placés aléatoirement, et qui permettra d'utiliser la fonction attaqueUser
def tabBot(m):
    for i in range(len(m)):
        print("\n", m[i], )
    return ""

# Tableau de "shoot", qui sera affiché à l'utilisateur, où celui-ci verra quelles cases il a joué et ce qu'elles contenaient
def tabBotForUser(p):
    for i in range(len(p)):
        print("\n", p[i], )
    return ""
