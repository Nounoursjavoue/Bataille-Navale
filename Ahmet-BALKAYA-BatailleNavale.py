from random import * #utile pour l'ia

def creer_grille(taille):
    """
    Crée une grille carrée de taille donnée remplie de ".".

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

def placer_navire(grille, ligne_depart, colonne_depart, longueur, orientation):
    """
    Place un navire sur la grille.

    :param grille: La grille de jeu (liste de listes).
    :param ligne_depart: Ligne de départ (1-based).
    :param colonne_depart: Colonne de départ (lettre, A-based).
    :param longueur: Longueur du navire.
    :param orientation: 'H' pour horizontal, 'V' pour vertical.
    :return: True si le placement est réussi, False sinon.
    """
    taille = len(grille)

    # Validation de colonne_depart
    if isinstance(colonne_depart, str) and len(colonne_depart) == 1 and colonne_depart.isalpha():
        colonne_index = ord(colonne_depart.upper()) - 65  # Convertir lettre en index (A=0)
        # Vérifier si la colonne est dans les limites de la grille
        if 0 <= colonne_index < taille:
            colonne_valide = True
        else:
            colonne_valide = False
    else:
        colonne_valide = False

    if not colonne_valide:
        print(f"Colonne invalide. Veuillez entrer une lettre entre A et {chr(64 + taille)}.")
        return False

    # Validation de ligne_depart
    if isinstance(ligne_depart, int) and 1 <= ligne_depart <= taille:
        ligne_index = ligne_depart - 1  # Convertir en index 0-based
        ligne_valide = True
    else:
        ligne_valide = False

    if not ligne_valide:
        print(f"Ligne invalide. Veuillez entrer un nombre entre 1 et {taille}.")
        return False

    # Validation de l'orientation
    if orientation.upper() not in ['H', 'V']:
        print("Orientation invalide. Utilisez 'H' pour horizontal ou 'V' pour vertical.")
        return False

    # Vérifier les limites et les collisions pour le placement horizontal
    if orientation.upper() == 'H':
        if colonne_index + longueur > taille:
            print("Placement hors des limites de la grille.")
            return False
        # Vérifier les collisions horizontales
        for i in range(longueur):
            if grille[ligne_index][colonne_index + i] != ".":
                print("Collision avec un autre navire.")
                return False
        # Placer le navire horizontalement
        for i in range(longueur):
            grille[ligne_index][colonne_index + i] = "$"

    # Vérifier les limites et les collisions pour le placement vertical
    elif orientation.upper() == 'V':
        if ligne_index + longueur > taille:
            print("Placement hors des limites de la grille.")
            return False
        # Vérifier les collisions verticales
        for i in range(longueur):
            if grille[ligne_index + i][colonne_index] != ".":
                print("Collision avec un autre navire.")
                return False
        # Placer le navire verticalement
        for i in range(longueur):
            grille[ligne_index + i][colonne_index] = "$"

    return True
