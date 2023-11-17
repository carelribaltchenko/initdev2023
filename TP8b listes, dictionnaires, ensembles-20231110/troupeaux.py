# TP8 B - Manipuler des listes, ensembles et dictionnaires


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    anim_tot=0
    for valeurs in troupeau.values():
        anim_tot+= valeurs
    return anim_tot


def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    les_animaux=set()
    for animal in troupeau.keys():
        les_animaux.add(animal)
    return les_animaux


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    res=False
    for nbr in troupeau.values():
        if nbr>=30:
            res=True
    return res


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    if troupeau=={}:
        return None
    troupeau["a"]=0
    res="a"
    for animal in troupeau.keys():
        if troupeau[animal]>troupeau[res]:
            res=animal
    return res

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    res=True
    for nbr in troupeau.values():
        if nbr<5:
            res=False
    return res


def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    val={}
    res=0
    if troupeau1=={}:
        return troupeau2
    if troupeau2=={}:
        return troupeau1
    for (nom, nb) in troupeau1.items():
        val[nom]=nb
    for (nom, nb) in troupeau2.items():
        if nom not in val:
            val[nom]=nb
        else:
            res=val[nom]
            val[nom]=res+nb
    return val