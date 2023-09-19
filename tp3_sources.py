# exercice 1
# def pair_supp_impair(entree):
#     """[revoie si il y a plus de nombre pair que de nombre impair dans une liste donnée]

#     Args:
#         entree ([list]): [liste d'entier]

#     Returns:
#         [bool]: [true si il y a plus de nombres pairs et false si plus de nombres impairs]
#     """
#     pair = 0
#     nb_impair = 0
#     # au début de chaque tour de boucle
#     #  A COMPLETER
#     for nbr in entree:
#         if nbr % 2 == 0:
#             pair += 1
#         else:
#             nb_impair += 1
#     return pair >= nb_impair

# def test_pair_sup_impair():
# print(pair_supp_impair([1,4,6,-2,-5,3,10]) == True
# print(pair_supp_impair([-4,5,-11,-56,5,-11]) == False 

# exercice 2
# def min_sup(liste_nombres, valeur):
#     """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

#     Args:
#         liste_nombres (list): la liste de nombres
#         valeur (int ou float): la valeur limite du minimum recherché

#     Returns:
#         int ou float: le plus petit nombre de la liste supérieur à valeur
#     """

#     if liste_nombres==[]:
#         return None
#     else :
#         res = float("inf")
#         for elem in liste_nombres:
#             if valeur < elem and elem < res:
#                 res = elem
#         if res == float("inf"):
#             res = None
#     return res



# print(min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5))
# print(min_sup([-2, -5, 2, 9.8, -8.1, 7], 0))
# print(min_sup([5, 7, 6, 5, 7, 3], 10))
# print(min_sup([], 5))


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


def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus


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

print(last_voy("buongiorno"))
print(last_voy("bonjour"))


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
def test_somme_pre_ent():
    assert sommme_pre_ent(4)==10
    assert sommme_pre_ent(100)==5050


test_somme_pre_ent()

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


def test_test_syracuse():
    assert test_syracuse(8,14) == 4.0
    assert test_syracuse(7,250)==2.0

test_test_syracuse()

