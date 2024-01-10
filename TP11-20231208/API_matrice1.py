""" Matrices : API n 1 """


def creer_matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    res = []
    for _ in range(nb_lignes*nb_colonnes):
        res.append(valeur_par_defaut)
    return (nb_lignes, nb_colonnes, res)


def get_nb_lignes(la_matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return la_matrice[0]


def get_nb_colonnes(la_matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        la_matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return la_matrice[1]


def get_val(la_matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    nb_cl = get_nb_colonnes(la_matrice)
    return la_matrice[2][(ligne)*nb_cl+colonne]


def set_val(la_matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur.

    Args:
        la_matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    val = get_val(la_matrice, ligne, colonne)
    nb_cl = get_nb_colonnes(la_matrice)
    for indice in range((ligne)*nb_cl+colonne+1):
        if la_matrice[2][indice] == val :
            la_matrice[2][indice] = nouvelle_valeur

# Fonctions pour l'affichage

def affiche_ligne_separatrice(la_matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(la_matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(la_matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        la_matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(la_matrice)
    nb_lignes = get_nb_lignes(la_matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(la_matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(la_matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(la_matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

# =====================================================
# Exercice 5 :
# =====================================================

def get_ligne(matrice, ligne):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    ligne_demande = []
    if 0 <= ligne < nb_lignes :
        for i in range(nb_colonnes):
            valeur = get_val(matrice, ligne, i)
            ligne_demande.append(valeur)
    return ligne_demande

def get_colonne(matrice, colonne):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    colonne_demande = []
    if 0 <= colonne < nb_colonnes :
        for i in range(nb_lignes):
            valeur = get_val(matrice, i, colonne)
            colonne_demande.append(valeur)
    return colonne_demande

def get_diagonale_principale(matrice):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    valeur_demande = []
    if nb_lignes == nb_colonnes :
        for i in range(nb_lignes):
            valeur = get_val(matrice, i, i)
            valeur_demande.append(valeur)
    return valeur_demande

def get_diagonale_secondaire(matrice):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    valeur_demande = []
    if nb_lignes == nb_colonnes :
        for i in range(nb_lignes):
            valeur = get_val(matrice, i, nb_colonnes-1-i)
            valeur_demande.append(valeur)
    return valeur_demande

def transpose(matrice):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    transpo = creer_matrice(nb_colonnes, nb_lignes, None)
    for i in range(nb_lignes):
        ligne_i = get_ligne(matrice,i)
        for j in range(nb_colonnes):
            set_val(transpo, j, i, ligne_i[j])
    return transpo

def is_triangulaire_inf(matrice):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    if nb_colonnes != nb_lignes:
        return False
    else :
        for i in range(nb_lignes):
            for j in range(i+1, nb_colonnes):
                if get_val(matrice, i, j) != 0:
                    return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    nb_lignes = get_nb_lignes(matrice)
    nb_colonnes = get_nb_colonnes(matrice)
    sous_matrice = creer_matrice(hauteur, largeur, 0)
    if (0 < hauteur <= nb_lignes - ligne) or (0 < largeur <= nb_colonnes - colonne) and (0 <= ligne < nb_lignes) or (0 <= colonne < nb_colonnes):
        for i in range(hauteur):
            for j in range(largeur):
                nouvelle_valeur = get_val(matrice, ligne + i, colonne + j)
                set_val(sous_matrice, i, j, nouvelle_valeur)
    return sous_matrice