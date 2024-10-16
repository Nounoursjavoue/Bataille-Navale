#Utile pour l'IA
from random import randint


#affichage de la grille pour bataille navale


# Définir la taille de la grille
taille_grille = 10

# Créer une grille 10x10 remplie de "~" pour représenter l'eau
grille = []
for _ in range(taille_grille):
    ligne = []
    for _ in range(taille_grille):
        ligne.append(".")
    grille.append(ligne)

# Fonction pour afficher la grille
def afficher_grille(grille):
    taille = len(grille)
    # Afficher les en-têtes de colonnes
    en_tetes = "  "
    for i in range(taille):
        en_tetes += chr(65 + i) + " "
    print(en_tetes)
    
    # Afficher chaque ligne avec son numéro
    for index, ligne in enumerate(grille, start=1):
        # Ajouter un espace pour les numéros à un chiffre
        if index < 10:
            numero = f"{index} "
        else:
            numero = f"{index}"
        ligne_a_afficher = numero
        for cellule in ligne:
            ligne_a_afficher += cellule + " "
        print(ligne_a_afficher.strip())

# Afficher la grille vide avec coordonnées
afficher_grille(grille)
