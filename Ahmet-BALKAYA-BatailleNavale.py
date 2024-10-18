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

def effectuer_tir(grille, cible):
    """
    Effectue un tir sur la grille.

    :param grille: La grille de défense (liste de listes).
    :param cible: Coordonnée du tir (ex: 'B5').
    :return: Résultat du tir ('Manqué', 'Touché', 'Coulé').
    """
    longueur_cible = len(cible)
    if longueur_cible < 2:
        return "Coordonnée invalide."

    colonne = cible[0].upper()
    ligne_str = cible[1:]

    # Validation de la colonne
    if colonne.isalpha() and len(colonne) == 1:
        colonne_index = ord(colonne) - 65
        colonne_dans_limites = 0 <= colonne_index < len(grille)
    else:
        colonne_dans_limites = False

    if colonne_dans_limites:
        pass
    else:
        return "Coordonnée invalide."

    # Validation de la ligne
    if ligne_str.isdigit():
        ligne = int(ligne_str)
        ligne_index = ligne - 1
        ligne_dans_limites = 0 <= ligne_index < len(grille)
    else:
        ligne_dans_limites = False

    if ligne_dans_limites:
        pass
    else:
        return "Coordonnée invalide."

    # Vérification de la cellule ciblée
    cellule = grille[ligne_index][colonne_index]
    if cellule == "N":
        grille[ligne_index][colonne_index] = "T"  # 'T' pour Touché
        # Vérification si le navire est coulé
        navire_coule = True
        for ligne_grille in grille:
            if "N" in ligne_grille:
                navire_coule = False
                break
        if navire_coule:
            return "Touché et Coulé!"
        else:
            return "Touché!"
    elif cellule == ".":
        grille[ligne_index][colonne_index] = "O"  # 'O' pour Manqué
        return "Manqué."
    elif cellule == "T" or cellule == "O":
        return "Déjà tiré ici."
    else:
        return "État de cellule inconnu."

def placer_flotte(grille, nom_joueur):
    """
    Permet à un joueur de placer sa flotte de navires sur sa grille.

    :param grille: La grille de défense du joueur (liste de listes).
    :param nom_joueur: Nom du joueur (str).
    """
    print(f"{nom_joueur}, placez vos navires sur la grille.")
    afficher_grille(grille, afficher_navires=True) 
    navires = [
        {"nom": "Porte-avions", "longueur": 5, "quantité": 1},
        {"nom": "Cuirassé", "longueur": 4, "quantité": 1},
        {"nom": "Croiseur", "longueur": 3, "quantité": 1},
        {"nom": "Sous-marin", "longueur": 3, "quantité": 1},
        {"nom": "Torpilleur", "longueur": 2, "quantité": 1}
    ]

    for navire in navires:
        for _ in range(navire["quantité"]):
            placement_reussi = False
            while not placement_reussi:
                print(f"Placer un {navire['nom']} (Longueur: {navire['longueur']})")
                entree = input("Entrez la position et l'orientation (ex: C3 H): ").upper().split()
                if len(entree) != 2:
                    print("Entrée invalide. Veuillez entrer la position et l'orientation séparées par un espace.")
                    continue
                position, orientation = entree
                if len(position) < 2:
                    print("Position invalide. Exemple valide: C3")
                    continue
                colonne_depart = position[0]
                ligne_depart_str = position[1:]
                if not ligne_depart_str.isdigit():
                    print("Ligne invalide. Exemple valide: C3")
                    continue
                ligne_depart = int(ligne_depart_str)
                if orientation not in ['H', 'V']:
                    print("Orientation invalide. Utilisez 'H' pour horizontal ou 'V' pour vertical.")
                    continue
                placement_reussi = placer_navire(grille, ligne_depart, colonne_depart, navire["longueur"], orientation)
                if placement_reussi:
                    afficher_grille(grille, afficher_navires=True)
                else:
                    print("Réessayez de placer ce navire.")
    input("Tous les navires ont été placés. Passons au prochain joueur. Appuyez sur Entrée pour continuer.")
    
def jouer_bataille_navale():
    """
    Fonction principale pour jouer à la Bataille Navale à deux joueurs.
    """
    taille_grille = 10
    # Création des grilles pour les deux joueurs
    grille_joueur1_defense = creer_grille(taille_grille)
    grille_joueur1_attaque = creer_grille(taille_grille)
    grille_joueur2_defense = creer_grille(taille_grille)
    grille_joueur2_attaque = creer_grille(taille_grille)

    # Noms des joueurs
    nom_joueur1 = input("Entrez le nom du Joueur 1: ")
    nom_joueur2 = input("Entrez le nom du Joueur 2: ")

    # Placement des navires pour le Joueur 1
  
    placer_flotte(grille_joueur1_defense, nom_joueur1)

    # Placement des navires pour le Joueur 2

    placer_flotte(grille_joueur2_defense, nom_joueur2)

    # Début du jeu
    jeu_en_cours = True
    joueur_actuel = 1  # 1 ou 2

    while jeu_en_cours:
        if joueur_actuel == 1:
            nom_actuel = nom_joueur1
            grille_defense_adverse = grille_joueur2_defense
            grille_attaque_actuel = grille_joueur1_attaque
        else:
            nom_actuel = nom_joueur2
            grille_defense_adverse = grille_joueur1_defense
            grille_attaque_actuel = grille_joueur2_attaque

        print(f"{nom_actuel}, c'est votre tour d'attaquer.")
        print("Votre grille d'attaque :")
        afficher_grille(grille_attaque_actuel)
        print("Entrez votre tir.")
        tir_valide = False
        while not tir_valide:
            cible = input("Entrez la coordonnée du tir (ex: B5): ").upper()
            resultat = effectuer_tir(grille_defense_adverse, cible)
            if resultat == "Coordonnée invalide.":
                print(resultat)
                continue
            elif resultat == "Déjà tiré ici.":
                print(resultat)
                continue
            else:
                tir_valide = True
                # Mettre à jour la grille d'attaque
                colonne = cible[0]
                ligne = int(cible[1:])
                colonne_index = ord(colonne) - 65
                ligne_index = ligne - 1
                grille_attaque_actuel[ligne_index][colonne_index] = "T" if resultat.startswith("Touché") else "O"
                print(f"Tir à {cible}: {resultat}")
                # Afficher les grilles
                print("\nVotre grille d'attaque après le tir :")
                afficher_grille(grille_attaque_actuel)
                print("\nGrille de défense adverse :")
                afficher_grille(grille_defense_adverse, afficher_navires=False)
                # Vérifier la fin du jeu
                if resultat.startswith("Touché et Coulé!") or all(cell != "N" for ligne in grille_defense_adverse for cell in ligne):
                    print(f"\nFélicitations {nom_actuel}! Vous avez coulé tous les navires de l'adversaire.")
                    jeu_en_cours = False
        # Changer de joueur
        joueur_actuel = 2 if joueur_actuel == 1 else 1
        if jeu_en_cours:
            input("Passons au prochain joueur. Appuyez sur Entrée pour continuer.")
            

    print("Fin du jeu. Merci d'avoir joué à la Bataille Navale!")
    
    
if __name__ == "__main__":
    jouer_bataille_navale()