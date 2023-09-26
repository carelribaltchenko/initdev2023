phrase = "Cela fait déjà 28 jours! 28 jours à l’IUT’O! Cool!!"

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


# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,
              25725]

def ville_plus_peuplee():
    """
        renvoie le nom de la ville la plus peuplée
    """    
    for i in range(1,len(population)):
        if population[i]>population[i-1]:
            c=population[i]
            a=i
    return "la ville la plus peuplée est", liste_villes[a]


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


def recherche_mot(liste, lettre):
    """renvoie une liste avec tous les mots commencant par une lettre donnée

    Args:
        liste (list): une liste de str
        lettre (str): une lettre

    Returns:
        list: la liste des mots commencant par la lettre donnée
    """    
    L1=[]
    for i in range(len(liste)):
        if liste[i][0] == lettre:
            L1.append(liste[i])
    return L1


def liste_mot_texte(texte):
    """renvoie la liste des mots d'un texte

    Args:
        texte (str): un texte 

    Returns:
        list: la liste des mots du texte
    """    
    L=[]
    mot = ''
    for i in range(len(texte)):
        if texte[i].isalpha():
            mot = mot + texte[i]
        else:
            if mot != '':
                L.append(mot)
                mot = ''
    return L 


def liste_mot_lettre_texte(texte, lettre):
    """renvoie les mots qui commencent par une lettre donnée dans une phrase

    Args:
        texte (str): une phrase
        lettre (str): une lettre

    Returns:
        list: une liste avec les mots qui commencent par la lettre donnée
    """    
    L=[]
    Liste=liste_mot_texte(texte)
    L.append(recherche_mot(Liste, lettre))
    return L


def true_sauf_premier(N):
    """initialise une liste de N+ booléens tous a True sauf les 2 premiers

    Args:
        N (int): un nombre

    Returns:
        liste: la liste des booleens
    """
    liste = []
    for i in range(N+1):
        if i == 1 or i == 0:
            liste.append(False)
        else:
            liste.append(True)
    return liste


def false_multiple(x,N):
    """renvoie une liste avec true tous les nombres qui ne sont pas multiple de N

    Args:
        x (int): le multiple du nombre
        true_sauf_premier (list): le resultt du premier

    Returns:
        list: true si c'est pas un multiple ou lui même 
    """    
    Liste= true_sauf_premier(N)
    for i in range(len(Liste)):
        Liste[i]=not (i%x == 0 and i!=x)
    return Liste



def crible_eratostene(N):
    """renvoie la liste des nombres premiers jusqu'au terme N

    Args:
        N (int): un entier

    Returns:
        list: les nombres premiers grace au crible
    """    
    crible_bool=true_sauf_premier(N)
    crible=[]
    for i in range(2,len(crible_bool)):
        liste_false=false_multiple(i,N)
        for j in range(len(liste_false)):
            if not liste_false[j]:
                crible_bool[j]=False
        if crible_bool[i]:
            crible.append(i)
    return crible


def all_print():
    print(plus_long_plateau("aazerrrtyyyyyy"))
    print(ville_plus_peuplee())
    print(chaine_nombre("123456789"))
    print(recherche_mot(["salut","hello","hallo","ciao","hola"],"a"))
    print(liste_mot_texte(phrase))
    print(liste_mot_lettre_texte(phrase, 'C'))
    print(true_sauf_premier(5))
    print(false_multiple(2,6))
    print(crible_eratostene(5))

print(all_print())
