# exercice 1
def pair_supp_impair(entree):
    """[revoie si il y a plus de nombre pair que de nombre impair dans une liste donnée]

    Args:
        entree ([list]): [liste d'entier]

    Returns:
        [bool]: [true si il y a plus de nombres pairs et false si plus de nombres impairs]
    """
    pair = 0
    nb_impair = 0
    # au début de chaque tour de boucle
    #  A COMPLETER
    for nbr in entree:
        if nbr % 2 == 0:
            pair += 1
        else:
            nb_impair += 1
    return pair >= nb_impair



# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """

    if liste_nombres==[]:
        return None
    else :
        res = float("inf")
        for elem in liste_nombres:
            if valeur < elem and elem < res:
                res = elem
        if res == float("inf"):
            res = None
    return res





# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = ''
    if phrase == "":
        return 0
    if phrase[0] == " ":
        resultat+=-1
    # au début de chaque tour de boucle
    # c1 vaut
    # c2 vaut
    # resultat vaut
    for c2 in phrase:
        if c1 == ' ' and c2 != ' ':
            resultat = resultat + 1
        c1 = c2
    return resultat+1





#ex4
def add_pair(liste):
    """renvoie la somme de tous les nombres pairs d'une liste donnée

    Args:
        liste (list): une liste d'entier

    Returns:
        int: le resultat
    """    
    res = 0
    for i in liste:
        if i%2==0:
            res+=i
    return res



def last_voy(mot):
    """renvoie la dernierre voyelle d'un mot

    Args:
        mot (str): un mot ou chaine de caractere

    Returns:
        str: la derniere voyelle
    """    
    last = ""
    voy='aeiouy'
    for i in mot:
        if i in voy:
            last = i
    return last



def prop_neg(list):
    """renvoie la proportion de ngatifs

    Args:
        list (list): une liste d'entier 

    Returns:
        str: proportion de negatif
    """    
    c=0
    if list==[]:
        return None
    for i in list :
        if i<0:
            c+=1
    return c/len(list)

#exercice 5 

def sommme_pre_ent(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res
"""res contiens la somme de tous les entiers jusqu'a i"""


def test_syracuse(val_init, n):
    """renvoie le terme Un d'une suite de syracuse

    Args:
        val_init (int): strictement positif
        n (int): strictement positif

    Returns:
        float: resultat de la suite de syracus
    """    
    U=val_init
    for i in range(n-1):
        if U%2==0:
            U=U/2
        elif U%2==1:
            U=3*U+1
    return U




#exercice 6

def mini_liste(liste):
    """renvoie le plus petit terme de la liste

    Args:
        liste (list): une liste d'entier

    Returns:
        int: le plus petit nombre dans la liste
    """    
    res = liste[0]
    for elt in liste:
        if elt < res :
            res = elt
    return res




def ecart_mini_maxi(liste):
    """renvoie l'ecart entre le plus grand terme et le plus petit terme d'une liste

    Args:
        liste (list): une liste d'entier

    Returns:
        int: un entier positif
    """    
    max=liste[0]
    min=liste[0]
    for elt in liste:
        if elt<min:
            min = elt
        elif elt > max :
            max = elt
    return max - min



def sup_10(liste):
    """renvoie le nombre de termes superieur a 10

    Args:
        liste (list): une liste d'entier

    Returns:
        int : le nombre de terme sup a 10
    """    
    c=0
    for i in range(len(liste)):
        if liste[i]>10:
            c+=1
    return c



def moy_neg(liste):
    """renvoie la moyenne des nombres negatifs d'une liste

    Args:
        liste (list): liste d'entier

    Returns:
        None: none
        int: list d'entier
    """    
    som=0
    c=0
    for elt in liste:
        if elt<0:
            som+=elt
            c+=1
    if c==0:
        return None
    return som/c



def compt_sylabe(mot):
    """renvoie le nombre de sylabe dans le mot

    Args:
        mot (str): un mot

    Returns:
        int: nombre de sylabes dans le mot
    """    
    voy = "aeiouy"
    c1=""
    nb = 0
    if mot[0]in voy:
        nb+=1
    for c2 in mot:
        if c1 not in voy and c2 in voy:
            nb+=1
        c1=c2
    return nb

#tous les asserts


def test_moy_neg():
    assert moy_neg([1,2,5,7,8,9,6,4,5,7,8,4]) == None
    assert moy_neg([1,4,8,7,-9,4,5,8,-7]) == -8


def test_compt_sylabe():
    assert compt_sylabe("bonbon") ==2
    assert compt_sylabe("ami") == 2


def test_sup_10():
    assert sup_10([1,4,84,6,25,10,14,1,25,4]) == 4
    assert sup_10([1,4,84,5,4,7,4,2,54,1,10]) == 2

def test_ecart_mini_maxi():
    assert ecart_mini_maxi([5,4,8,9,3,5,7,2,0,4]) == 9
    assert ecart_mini_maxi([1,8,-1,5,4,-9,7,8]) == 17

def test_mini_liste():
    assert mini_liste([5,4,8,9,3,5,7,2,0,4]) == 0
    assert mini_liste([1,8,-1,5,4,-9,7,8]) == -9

def test_test_syracuse():
    assert test_syracuse(8,14) == 4.0
    assert test_syracuse(7,250)==2.0

def test_somme_pre_ent():
    assert sommme_pre_ent(4)==10
    assert sommme_pre_ent(100)==5050

def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

def test_pair_sup_impair():
    assert pair_supp_impair([1,4,6,-2,-5,3,10]) == True
    assert pair_supp_impair([-4,5,-11,-56,5,-11]) == False 

def test_min_sup():
    assert(min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5)) == 7
    assert(min_sup([-2, -5, 2, 9.8, -8.1, 7], 0)) == 2
    assert(min_sup([5, 7, 6, 5, 7, 3], 10)) == None
    assert(min_sup([], 5)) == None

test_min_sup()
test_pair_sup_impair()
test_nb_mots()
test_somme_pre_ent()
test_test_syracuse()
test_mini_liste()
test_ecart_mini_maxi()
test_moy_neg()
test_sup_10()