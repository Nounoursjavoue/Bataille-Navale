from random import * #utile pour l'ia

def creer_grille(taille):
    """
    Crée une grille carrée de taille donnée remplie de "~".

    :param taille: Taille de la grille (int).
    :return: Grille créée (liste de listes).
    """
    grille = []
    for _ in range(taille):
        ligne = []
        for _ in range(taille):
            ligne.append(".")
        grille.append(ligne)
    return grille


def afficher_grille(grille):
    """
    Affiche la grille avec les coordonnées.

    :param grille: La grille à afficher (liste de listes).
    :param afficher_navires: Booléen indiquant si les navires doivent être affichés.
    """
    taille = len(grille)
    # Afficher les en-têtes de colonnes
    en_tetes = "   " + " ".join([chr(65 + i) for i in range(taille)])
    print(en_tetes)
    
    # Afficher chaque ligne avec son numéro
    for index, ligne in enumerate(grille, start=1):
        # Ajouter un espace pour les numéros à un chiffre
        numero = f"{index} " if index < 10 else f"{index}"
        print(numero + " " + " ".join(ligne))



grille = creer_grille(10)
# Afficher la grille
afficher_grille(grille)
