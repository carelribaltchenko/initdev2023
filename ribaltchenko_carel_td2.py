def add_liste(list):
    """additionne tous les termes d'une liste

    Args:
        list (list): une liste de nombres

    Returns:
        float: l'addition de tous les termes
    """    
    res=0
    for i in list:
        res+=i
    return res

def max_liste(list):
    """renvoi le plus grand teme d'une lite

    Args:
        list (list): une liste de nombres

    Returns:
        int: le plus grand terme de la suite
    """    
    res = list[0]
    for i in list:
        if i>res:
            res=i
    return res

def nb_occ(mot, char):
    """le nombre d'occurence d'un terme dans un mot

    Args:
        mot (str): un mot 
        char (str): une letre

    Returns:
        int: le nombre d'occurence de char dans mot
    """    
    c=0
    for i in mot:
        if i==char:
            c+=1
    return c
