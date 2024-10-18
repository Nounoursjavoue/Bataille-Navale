import random

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

def afficher_grille(grille, afficher_navires=False):
    """
    Affiche la grille avec les coordonnées.

    :param grille: La grille à afficher (liste de listes).
    :param afficher_navires: Booléen indiquant si les navires doivent être affichés.
    """
    taille = len(grille)
    # Afficher les en-têtes de colonnes
    en_tetes = "  "
    for i in range(taille):
        en_tetes += chr(65 + i) + " " # Utilisation de la table ascii pour facilitez l'affichage
    print(en_tetes)

    # Afficher chaque ligne avec son numéro
    for indice, ligne in enumerate(grille, start=1):
        if indice < 10:
            numero = f"{indice} "
        else:
            numero = f"{indice}"
        ligne_a_afficher = numero
        for cellule in ligne:
            if cellule == "$" and not afficher_navires:
                ligne_a_afficher += ". "
            else:
                ligne_a_afficher += cellule + " "
        print(ligne_a_afficher.strip())

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
    if cellule == "$":
        grille[ligne_index][colonne_index] = "T"  # 'T' pour Touché
        # Vérification si le navire est coulé
        navire_coule = True
        for ligne_grille in grille:
            if "$" in ligne_grille:
                navire_coule = False
                break
        if navire_coule:
            return "Touché et Coulé!"
        else:
            return "Touché!"
    elif cellule == ".":
        grille[ligne_index][colonne_index] = "M"  # 'O' pour Manqué
        return "Manqué."
    elif cellule == "T" or cellule == "M":
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
        {"nom": "Porte-avions", "longueur": 5, "quantité": 0},
        {"nom": "Cuirassé", "longueur": 4, "quantité": 0},
        {"nom": "Croiseur", "longueur": 3, "quantité": 0},
        {"nom": "Sous-marin", "longueur": 3, "quantité": 0},
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
                grille_attaque_actuel[ligne_index][colonne_index] = "T" if resultat.startswith("Touché") else "M"
                print(f"Tir à {cible}: {resultat}")
                # Afficher les grilles
                print("\nVotre grille d'attaque après le tir :")
                afficher_grille(grille_attaque_actuel)
                print("\nGrille de défense adverse :")
                afficher_grille(grille_defense_adverse, afficher_navires=False)
                # Vérifier la fin du jeu
                if resultat.startswith("Touché et Coulé!") or all(cell != "$" for ligne in grille_defense_adverse for cell in ligne):
                    print(f"\nFélicitations {nom_actuel}! Vous avez coulé tous les navires de l'adversaire.")
                    jeu_en_cours = False
        # Changer de joueur
        joueur_actuel = 2 if joueur_actuel == 1 else 1
        if jeu_en_cours:
            input("Passons au prochain joueur. Appuyez sur Entrée pour continuer.")
            

    print("Fin du jeu. Merci d'avoir joué à la Bataille Navale!")

# rendre dans la partie IA basic 

# Dictionnaire pour conversion lettre -> index
lettre_a_index = {chr(65 + i): i for i in range(26)}  # {'A': 0, 'B': 1, ...}

# Dictionnaire pour conversion index -> lettre
index_a_lettre = {i: chr(65 + i) for i in range(26)}  # {0: 'A', 1: 'B', ...}

def convertir_coord_en_index(coord):
    """
    Convertit une coordonnée de type "B5" en indices (ligne, colonne).

    :param coord: Coordonnée sous forme de chaîne (ex: "B5").
    :return: Tuple (ligne, colonne) sous forme d'indices.
    """
    colonne = lettre_a_index[coord[0]]
    ligne = int(coord[1:]) - 1
    return (ligne, colonne)

def convertir_index_en_coord(ligne, colonne):
    """
    Convertit des indices (ligne, colonne) en une coordonnée de type "B5".

    :param ligne: Indice de la ligne.
    :param colonne: Indice de la colonne.
    :return: Coordonnée sous forme de chaîne (ex: "B5").
    """
    return f"{index_a_lettre[colonne]}{ligne + 1}"

def convertir_coord_inverse(ligne, colonne): # on aurait aussi pu faire un dictionnaire
    """
    Convertit des coordonnées numériques en coordonnées de jeu (ex: (0,1) -> "B1").

    :param ligne: Indice de ligne.
    :param colonne: Indice de colonne.
    :return: La coordonnée du jeu (ex: "B1").
    """
    lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return f"{lettres[colonne]}{ligne + 1}"

def placer_navire_aleatoire(grille, longueur):
    """
    Place un navire de manière aléatoire sur la grille.

    :param grille: Grille où placer le navire.
    :param longueur: Longueur du navire.
    :return: True si le placement a réussi, False sinon.
    """
    taille = len(grille)
    orientation = random.choice(['H', 'V'])
    
    if orientation == 'H':
        ligne = random.randint(0, taille - 1)
        colonne = random.randint(0, taille - longueur)
        # Vérifier les collisions
        for i in range(longueur):
            if grille[ligne][colonne + i] != ".":
                return False
        # Placer le navire
        for i in range(longueur):
            grille[ligne][colonne + i] = "$"
    else:  # orientation == 'V'
        ligne = random.randint(0, taille - longueur)
        colonne = random.randint(0, taille - 1)
        # Vérifier les collisions
        for i in range(longueur):
            if grille[ligne + i][colonne] != ".":
                return False
        # Placer le navire
        for i in range(longueur):
            grille[ligne + i][colonne] = "$"
    
    return True

def placer_flotte_aleatoire(grille):
    """
    Place aléatoirement une flotte de navires sur la grille pour l'IA.

    :param grille: Grille de défense de l'IA (liste de listes).
    """
    navires = [5, 4, 3, 3, 2]  # Longueurs des navires

    for longueur in navires:
        place = False
        while not place:
            place = placer_navire_aleatoire(grille, longueur)

def tir_aleatoire_ia(grille_attaque, taille_grille):
    """
    Génère un tir aléatoire sur une grille pour l'IA.

    :param grille_attaque: Grille d'attaque de l'IA (liste de listes).
    :param taille_grille: Taille de la grille (int).
    :return: Coordonnées du tir sous forme de tuple (ligne, colonne).
    """
    tir_valide = False
    while not tir_valide:
        ligne = random.randint(0, taille_grille - 1)
        colonne = random.randint(0, taille_grille - 1)
        if grille_attaque[ligne][colonne] == ".":  # Vérifie si l'IA n'a pas déjà tiré ici
            tir_valide = True
    return (ligne, colonne)

def effectuer_tir_IA(grille_defense, grille_attaque, cible):
    """
    Effectue un tir sur la grille de défense et met à jour la grille d'attaque.

    :param grille_defense: Grille de défense de l'adversaire.
    :param grille_attaque: Grille d'attaque du joueur (ou de l'IA).
    :param cible: La case visée par le tir (ex: "B5").
    :return: Un message indiquant si c'est touché, raté ou déjà tiré.
    """
    ligne, colonne = convertir_coord_en_index(cible)

    if grille_attaque[ligne][colonne] in ["X", "M"]:
        return "Vous avez déjà tiré à cet endroit."

    if grille_defense[ligne][colonne] == "$":
        grille_defense[ligne][colonne] = "X"  # Met à jour la grille de défense
        grille_attaque[ligne][colonne] = "X"  # Met à jour la grille d'attaque
        return "Touché!"
    else:
        grille_attaque[ligne][colonne] = "M"  # Tir manqué
        return "Manqué!"


def tour_ia(grille_joueur_defense, grille_ia_attaque, taille_grille):
    """
    L'IA tire aléatoirement sur la grille du joueur.
    Met à jour la grille de l'IA et affiche le résultat du tir.
    
    :param grille_joueur_defense: Grille de défense du joueur.
    :param grille_ia_attaque: Grille d'attaque de l'IA.
    :param taille_grille: Taille de la grille.
    :return: Un message indiquant le résultat du tir de l'IA.
    """
    ligne = random.randint(0, taille_grille - 1)
    colonne = random.randint(0, taille_grille - 1)

    while grille_ia_attaque[ligne][colonne] in ["X","M"]:
        ligne = random.randint(0, taille_grille - 1)
        colonne = random.randint(0, taille_grille - 1)

    if grille_joueur_defense[ligne][colonne] == "$":
        grille_joueur_defense[ligne][colonne] = "X"  # Met à jour la grille de défense du joueur
        grille_ia_attaque[ligne][colonne] = "X"  # Met à jour la grille d'attaque de l'IA
        print(f"L'IA a tiré sur {convertir_coord_inverse(ligne, colonne)}: Touché!")
        return "Touché!"
    else:
        grille_ia_attaque[ligne][colonne] = "M"  # Tir manquéb
        print(f"L'IA a tiré sur {convertir_coord_inverse(ligne, colonne)}: Manqué!")
        return "Manqué!"


def jouer_bataille_navale_avec_ia():
    """
    Fonction principale pour jouer à la Bataille Navale contre une IA qui tire aléatoirement.
    """
    taille_grille = 10
    # Création des grilles pour le joueur et l'IA
    grille_joueur_defense = creer_grille(taille_grille)
    grille_joueur_attaque = creer_grille(taille_grille)
    grille_ia_defense = creer_grille(taille_grille)
    grille_ia_attaque = creer_grille(taille_grille)

    # Nom du joueur
    nom_joueur = input("Entrez votre nom: ")

    # Placement des navires pour le joueur
    placer_flotte(grille_joueur_defense, nom_joueur)

    # Placement des navires pour l'IA (aléatoire)
    placer_flotte_aleatoire(grille_ia_defense)

    # Début du jeu
    jeu_en_cours = True
    joueur_actuel = "Joueur"  # Alternance entre "Joueur" et "IA"

    while jeu_en_cours:
        if joueur_actuel == "Joueur":
            # Tour du joueur
            print(f"{nom_joueur}, c'est votre tour d'attaquer.")
            afficher_grille(grille_joueur_attaque)
            cible = input("Entrez la coordonnée du tir (ex: B5): ").upper()
            resultat = effectuer_tir_IA(grille_ia_defense, grille_joueur_attaque, cible)
            print(f"Tir à {cible}: {resultat}")
            afficher_grille(grille_joueur_attaque)
            
            # Vérification de la victoire
            if all(cell != "$" for row in grille_ia_defense for cell in row):
                print(f"Félicitations {nom_joueur}, vous avez coulé tous les navires de l'IA!")
                jeu_en_cours = False
            else:
                joueur_actuel = "IA"
        else:
            # Tour de l'IA
            resultat = tour_ia(grille_joueur_defense, grille_ia_attaque, taille_grille)
            afficher_grille(grille_joueur_defense)  # Montrer où l'IA a tiré
            
            # Vérification de la victoire
            if all(cell != "$" for row in grille_joueur_defense for cell in row):
                print("L'IA a coulé tous vos navires. Vous avez perdu.")
                jeu_en_cours = False
            else:
                joueur_actuel = "Joueur"

    print("Fin du jeu. Merci d'avoir joué à la Bataille Navale!")

# commencer du jeu  

if __name__ == "__main__":
    modeDeJeu = ""
    
    #le joueur choisi son mode de jeu 
    
    while modeDeJeu.upper() not in ["IA", "AMI"]:
        modeDeJeu = input("Voulez-vous jouer contre une IA ou un ami? (IA/AMI) ").upper()
        if modeDeJeu == "IA":
            jouer_bataille_navale_avec_ia()
        elif modeDeJeu == "AMI":
            jouer_bataille_navale()