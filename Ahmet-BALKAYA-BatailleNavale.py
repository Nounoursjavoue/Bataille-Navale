def afficher_grille(grille):
    taille = len(grille)
    # Afficher les en-têtes de colonnes
    en_tetes = "  " + " ".join([chr(65 + i) for i in range(taille)])
    print(en_tetes)
    
    # Afficher chaque ligne avec son numéro
    for index, ligne in enumerate(grille, start=1):
        # Ajouter un espace pour les numéros à un chiffre
        numero = f"{index} " if index < 10 else f"{index}"
        print(numero + " " + " ".join(ligne))

def creer_grille():
    """
    Crée une grille carrée de taille donnée remplie de ".".
    :return: Grille créée (liste de listes).
    """
    taille_grille = 10 # taille de la grille 
    grille = [["." for _ in range(taille_grille)] for _ in range(taille_grille)]
    return grille


grille = creer_grille()
# Afficher la grille
afficher_grille(grille)

