#Utile pour l'IA
from random import randint


#affichage de la grille pour bataille navale

def afficher_grille(grille):
    taille = 10
    # Afficher les en-têtes de colonnes
    en_tetes = " " + " ".join([chr(65 + i) for i in range(taille)])
    print(en_tetes)
    
    # Afficher chaque ligne avec son numéro
    for idx, ligne in enumerate(grille, start=1):
        # Ajouter un espace pour les numéros à un chiffre
        numero = f"{idx} " if idx < 10 else f"{idx}"
        print(numero + " " + " ".join(ligne))

# Créer une grille 10x10 pour la bataille navale
tailleGrille = 10
grille = [["." for _ in range(tailleGrille)] for _ in range(tailleGrille)]

# Afficher la grille avec coordonnées
afficher_grille(grille)