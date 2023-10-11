#exercice 4

# ---------------------------------------
# Exemple de table_scores
# ---------------------------------------
table_scores = [352100, 325410, 312785, 220199, 127853]
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
            if table_scores[i]>scor:
                scor=table_scores[i]
    return scor

    


def score_decroissant(liste):
    """teste si la liste des score est dabns l'ordre decroissant 
    Args:
        list: la liste des table_scores

    Returns:
        bool: True si c'est trié et False sinon
    """    
    res=True
    for i in range (1,len(liste)):
        if liste[i]>liste[i-1]:
            res=False
    return res




def nb_joueur(nom_joueur):
    """compte le nombre de fois dont un joueur apparait dans le tableau des table_scores

    Args:
        nom_joueur (str): le nom d'un joueur

    Returns:
        int: le nombre de fois ou le joueur apparait dans le tableau
    """    
    cpt=0
    if nom_joueur not in joueurs:
        return None
    for i in range(len(joueurs)):
        if joueurs[i]==nom_joueur:
            cpt+=1
    return cpt




def best_scor(nom_joueur):
    """renvoie la place du meilleur joueur

    Args:
        nom_joueur (str): le nom 

    Returns:
        int: la meilleur place du joueur
    """    
    if nom_joueur not in joueurs :
        return None
    res=len(joueurs)+1
    for i in range(len(joueurs)):
        if joueurs[i]==nom_joueur and res>i:
            res=i
    return res+1



def place_score(score):
    """renvoie la place du score mis en paametre

    Args:
        score (int): le score du joueur

    Returns:
        int: la place du score
    """    
    place = 0
    for i in range(len(table_scores)):
        if table_scores[i]>score:
            place+=1
    return place



def insere_score(score, nom_joueur,table_scores, joueurs):
    """insere le score dans la lisete de score 
       et le joueur dans la liste de joueur au m

    Args:
        score (int): le score du joueur
        nom_joueur (str): le nom du joueur
        table_scores (list): la liste des scores
        joueurs (list): la liste des joueur
    """    
    table_scores.insert(place_score(score),score)
    joueurs.insert(place_score(score), nom_joueur)






    


def test_meilleur_score():
    assert meilleur_score('Batman')== 352100
    assert meilleur_score('Robin')== 325410
    assert meilleur_score('Joker')== 220199
    assert meilleur_score('Eliott')==None


def test_score_decroissant():
    assert score_decroissant(table_scores)==True
    assert score_decroissant([5,1,47,8,7,5])==False
    assert score_decroissant([-1,-5,-8])==True
    assert score_decroissant([0,0,0,0,0,0])==True


def test_nb_joueur():
    assert nb_joueur('Batman')==3
    assert nb_joueur('Robin')==1
    assert nb_joueur('Joker')==1
    assert nb_joueur('Richard')==None


def test_best_scor():
    assert best_scor('Batman')==352100
    assert best_scor('Robin')== 325410
    assert best_scor('Joker')== 220199
    assert best_scor('Kyllian')==None

def test_place_score():
    assert place_score(0)==4
    assert place_score(314570)==2
    assert place_score(999999999)==0
    assert place_score(2)==4

def test_insere_score():
    insere_score(314570,'Joker',table_scores,joueurs)
    assert table_scores==[352100, 325410, 314570, 312785, 220199, 127853]
    assert joueurs == ['Batman', 'Robin', 'Joker', 'Batman', 'Joker', 'Batman']
    table_scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
    insere_score(0,"Baptiste",table_scores)
    assert table_scores==[352100, 325410, 312785, 220199, 127853,0]
    assert joueurs == ['Batman', 'Robin', 'Batman', 'Joker', 'Batman','Baptiste']
    table_scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
    insere_score(999999999,"yoann_P",table_scores)
    assert table_scores==[999999999,352100, 325410, 312785, 220199, 127853]
    assert joueurs == ['yoan_P','Batman', 'Robin', 'Batman', 'Joker', 'Batman']  
    table_scores = [352100, 325410, 312785, 220199, 127853]
    joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
    insere_score(-9,"M.Lechoppier",table_scores)
    assert table_scores==[352100, 325410, 312785, 220199, 127853,-9]
    assert joueurs == ['Batman', 'Robin', 'Batman', 'Joker', 'Batman','M.Lechoppier']