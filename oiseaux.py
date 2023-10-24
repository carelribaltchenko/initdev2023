# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if liste_observations==[]:
        return None
    oiseau_max = liste_observations[0]
    for observation in liste_observations:
        if observation[1] > oiseau_max[1]:
            oiseau_max = observation
    return oiseau_max[0]

def oiseau_le_plus_observe_indice(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    if liste_observations==[]:
        return None
    oiseau_max = liste_observations[0]
    for i in range (len(liste_observations)):
        if liste_observations[i][1] > oiseau_max[1]:
            oiseau_max = liste_observations[i]
    return oiseau_max[0]


#exercice 2
def recherche_oiseau(oiseau):
    """renvoie les caractéristiques d'un oiseau

    Args:
        oiseau (int): le nom d'un oiseau

    Returns:
        int: sa famille
    """    
    for piaf in oiseaux:
        if piaf[0]==oiseau:
            return piaf[1]
    return None 

def recherche_par_famille(famille):
    """renvoie la liste des oiseaux qui appartiennent à la même famille

    Args:
        famille (int): une famille d'oiseau

    Returns:
        list: la liste des oiseaux
    """    
    res=[]
    for i in range(len(oiseaux)):
        if oiseaux[i][1] == famille:
            res.append(oiseaux[i][0])
    return res


#exercice 3 ------------------------------
def est_trié(liste_observations):
    for i in range(1,len(liste_observations)):
        if liste_observations[i-1][0]>liste_observations[i][0]:
            return False
    return True

def est_liste_observations(liste_observations):
    """verifie si c'est une liste d'observation

    Args:
        liste_observations (list): une liste de tuples

    Returns:
        bool: True si 'est une liste d'observation et false sinon
    """    
    if liste_observations==[]:
        return None
    if not est_trié(liste_observations):
        return False
    for i in range(len(liste_observations)):
        if liste_observations[i][1]==0:
            return False
    return True 

def max_observations(liste_observations):

    if liste_observations==[]:
        return None
    max=0
    for oiseau in liste_observations:
        if oiseau[1]>max:
            max = oiseau[1]
    return max 

def moyenne_oiseaux_observes(liste_observations):
    if liste_observations == []:
        return None
    tot=0
    nbr=0
    for i in range(len(liste_observations)):
        nbr+=liste_observations[i][1]
        tot+=1
    return nbr/tot

def total_famille(nom_famille, liste_observations):
    if liste_observations == []:
        return None
    for i in range(len(oiseaux)):
        if oiseau[1]==nom_famille:
            liste_piaf.append(oiseaux[0])
    somme=0
    for oiseaux in liste_observations:
        if oiseaux[1] in liste_piaf:
            somme += oiseaux[0]
    return somme

            


#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)

