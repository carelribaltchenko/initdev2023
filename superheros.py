def intelligence_moyenne(dictionnaire):
    """renvoie la valeur moyenne de l'intelligence de tous les personnages

    Args:
        dictionnaire (dict): dictionnaire avec une clé str

    Returns:
        _type_: _description_
    """    
    cpt = 0
    tot = 0
    for elem in dictionnaire.values():
        tot+=elem[1]
        cpt+=1
    if cpt != 0:
        return tot/cpt
    else:
        return None
    
def kikelplusfort(dictionnaire):
    cpt = 0
    max = None
    for (nom, tuple) in troupeau.items():
        if tuple[0] > cpt:
            max = nom
            cpt = tuple[0]
    return max

def combienDeCretins(dictionnaire):
    moy = intelligence_moyenne(dictionnaire)
    cpt = 0
    for elem in dictionnaire.values():
        if elem[1] < moy:
            cpt+=1
    return cpt