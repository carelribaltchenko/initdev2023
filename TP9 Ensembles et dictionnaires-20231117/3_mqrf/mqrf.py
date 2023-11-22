
# ==========================
# La maison qui rend fou
# ==========================

#3.1 : on obtiens le formulaire A-38 par Astus si on part par Abribus


def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    depart = guichet
    while mqrf[depart] != None:
        arrivee=mqrf[depart]
        depart=arrivee
    return depart



def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    depart = guichet
    guichet_traverse=1
    while mqrf[depart] != None:
        arrivee=mqrf[depart]
        depart=arrivee
        guichet_traverse+=1
    return depart, guichet_traverse


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    depart = guichet
    guichet_traverse=1
    while mqrf[depart] != None:
        arrivee=mqrf[depart]
        depart=arrivee
        guichet_traverse+=1
        if guichet_traverse==len(mqrf):
            return None
    return (depart, guichet_traverse)


