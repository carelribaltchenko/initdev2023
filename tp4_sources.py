def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel
    for i in range(1,len(chaine)):
        if chaine[i] == chaine[i-1]:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else:  # si la lettre actuelle est différente de la précédente
            if lg_actuelle > lg_max:
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    return lg_max

print(plus_long_plateau("aazerrrtyyyyyy"))

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]

def ville_plus_peuplee():
    for i in range(1,len(population)):
        if population[i]>population[i-1]:
            c=population[i]
            a=i
    return "la ville la plus peuplée est", liste_villes[a]

print(ville_plus_peuplee())

def chaine_nombre(chaine):
    """transforme un str en int

    Args:
        chaine (str): un nombre entre guillemet

    Returns:
        int: le nombre qui etait entre crochet
    """
    a=0
    for i in range(len(chaine)):
        a=a+int(chaine[i])*(10**(len(chaine)-i-1))
    return a

print(chaine_nombre("123456789"))