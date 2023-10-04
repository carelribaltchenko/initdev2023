def mystere(liste, valeur):
    """calcule le nombre de valeur egalea valeur dans une liste si ce nombre est superieur a trois

    Args:
        liste (list): une liste
        valeur (int): un nombre

    Returns:
        int: [le nombre de valeur egale a valeur si >3 sinon None]
    """
    xxx = 0
    yyy = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            yyy += 1
            if yyy > 3:
                return xxx
        xxx += 1
    return None


print(mystere([12, 5, 8, 20, 12, 418, 20, 17, 5, 87], 20))



def recherche_ind_nombre(phrase):
    """renvoie l'indice du premier nombre d'une phrase

    Args:
        phrase (str): une phrase

    Returns:
        int: l'indice du premier chiffre de la phrase
    """    
    chiffre="1234567890"
    for i in range(len(phrase)):
        if phrase[i] in chiffre:
            return i
    return None

print (recherche_ind_nombre("onhfhfjibfbfhrebjhzefbfhj")) 
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

def pop_ville(ville):
    """renvoie le nombre d'habitants d'une ville donnée en argument 

    Args:
        ville (str): le nom d'une ville qui se trouve dans la ville

    Returns:
        int: le nombre d'habitants de la ville
    """    
    lv=liste_villes
    pop=population
    for i in range(len(lv)):
        if lv[i]==ville:
            return pop[i]
    return None

print(pop_ville("Châteauroux"))


#exercice3:
def est_triee(liste):
    """renvoie true si la liste est triee dans l'ordre croissant et false sinon

    Args:
        liste (list): une liste 

    Returns:
        bool: true si triée dans l'ordre
    """    
    t1=liste[0]
    for i in range(1,len(liste)):
        t2=liste[i]
        if t2<t1:
            return False
        t1=t2
    return True

print(est_triee([1,2,3,4,5,8]))

def somme_supp_seuil(liste,seuil):
    """renvoie true si la somme des terme de la liste dépasse un seuil

    Args:
        liste (_type_): _description_
        seuil (_type_): _description_

    Returns:
        _type_: _description_
    """    
    som=0
    for i in range (len(liste)):
        som+=liste[i]
    return som>seuil

def est_mail(adresse):
    """verifie si l'adresse mail est valide

    Args:
        adresse (_type_): _description_

    Returns:
        _type_: _description_
    """    
    cpt_at=0
    cpt_spc=0
    for i in range(len(adresse)):
        if adresse[i]=="@":
            cpt_at+=1
        if adresse[i]==" ":
            cpt_spc+=1
    return cpt_at==1 and cpt_spc==0 and adresse[0]!="@" and adresse[-1]!="." and point_apres_at(adresse)

def point_apres_at(adresse):
    """verifie si il y a un point apres le symbole @

    Args:
        adresse (str): l'adresse mail

    Returns:
        bool: true si il y a bien un point apres l'arobase
    """    
    for i in range(len(adresse)):
        if adresse[i]=="@":
            for j in range(i,len(adresse)):
                if adresse[j]==".":
                    return True
    return False

print(est_mail("deznjzenjiz@jkdsdsgqg"))

#exercice 4

# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
#4.1
def meilleur_score(nom_joueur):
    """renvoie le meilleur score du joueur donné en argument

    Args:
        nom_joueur (str): le nom d'u joueur

    Returns:
        int: le score du joueur
    """    
    scor=0
    if nom_joueur not in joueurs:
        return None
    for i in range(len(joueurs)):
        if joueurs[i]==nom_joueur:
            if scores[i]>scor:
                scor=scores[i]
    return f"le meilleur score de {nom_joueur} est de {scor}"

print(meilleur_score('Robin'))

def score_decroissant(liste):
    """teste si la liste des score est dabns l'ordre decroissant 
    Args:
        list: la liste des scores

    Returns:
        bool: True si c'est trié et False sinon
    """    
    res=True
    for i in range (len(liste)):
        if liste[i]>liste[i-1]:
            res=False
    return res

def nb_joueur(nom_joueur):
    cpt=0
    if nom_joueur not in joueurs:
        return None
    for i in range(len(joueurs)):
        if joueurs[i]==nom_joueur:
            cpt+=1
    return cpt

