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
    # Créer une grille 10x10
    taille_grille = 10
    grille = [["." for _ in range(taille_grille)] for _ in range(taille_grille)]
    return grille


grille = creer_grille()
# Afficher la grille avec coordonnées
afficher_grille(grille)
