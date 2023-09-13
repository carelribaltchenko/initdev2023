print("bienvenue à l'IUT'O")

def exemple_debug(x,y):
    nb=15
    ch="cou"
    nb=x+y
    return ch*2


def fonction1(x):
    a=12
    a=3+x
    return a


def fonction2(x):
    a = 12
    a = 3+x
    A = a/2
    b = a
    a = 5
    b = b+1
    return a


#exercice 5
def algo_1(a,b,c,d):
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_
        c (int): _description_
        d (int): _description_

    Returns:
        int: _description_
    """    
    res = 0
    if a<b:
        res = a
    else : 
        res = b
    if c<res:
        res = c
    if d<res:
        res = d
    return res

def algo2(m):
    """_summary_

    Args:
        m (str): un mot en minuscule

    Returns:
        bool: retourne si le mot contien plus de voyelles ou non

    """
    res = 0
    for i in m:
        if i in 'aeiuoy':
            res+=1
        else:
            res-=1
    return res>0

#exercice 6

"""6.1: record au 100m+3victoires OU être champion du monde
6.2 : qualifiée : record de 10.5s et 5 victoires mais pas champion du monde
      qualifiée : record de 13 second et 2 victoire mais champion du monde
      non qualifié : record de 13 secondes et 4 victoires"""


def qualifiquations_aux_JO(sexe, record, nb_victoires, champion_de_monde):
    """permet de dire si une personne est qualifiée aux JO

    Args:
        sexe (str): indique si la personne est un homme ou une femme
        record (float): le record au 100m de la personne en secondes
        nb_victoires (int): le nombre de victoires
        champion_de_monde (bool): si la personne est championne du monde

    Returns:
        bool: _description_
    """
    assert sexe == 'm' or sexe == 'M' or sexe =='f' or sexe == 'F', "le sexe doit etre indiqué par 'm', 'M', 'f' ou 'F'"

    
    
    if sexe == 'm' or sexe =='M':
        if record<=12:
            res = True
        else : 
            res = False
    elif sexe == 'f' or sexe == 'F' :
        if record <= 15:
            res = True
        else:
            res = False
    if nb_victoires<3:
        res = False
    if champion_de_monde == True:
        res = True
    return res 


print(qualifiquations_aux_JO('G', 15.0, 2, True ))


#exercice 7 : 
    """7.1 : les parametres d'entrée sont le depassement de vitesse, la vitesse programée et si le client à récidivé
        7.2 : depassement de vitesse : 15, vitesse programée : 30, recidive, True : il aura une amande de 135€ et -1 point

    """

def amende(depassement_de_vitesse, vitesse_programee, recidive):
    """_summary_

    Args:
        depassement_de_vitesse (int): _description_
        vitesse_programee (int): _description_
        recidive (bool): _description_

    Returns:
        p_uplet: _description_
    """    
    if depassement_de_vitesse<=20:
        if vitesse_programee<=50:
            res = (135, 1, 0)
        else :
            res = (68,1,0)
    elif 20<depassement_de_vitesse<=30:
        res = (135,2,0)
    elif 30<depassement_de_vitesse<=40:
        res = (135,3,3)
    elif 40<depassement_de_vitesse<=50:
        res = (135,4,3)
    elif 50<depassement_de_vitesse:
        if recidive:
            res = (1500,6,3)
        else:
            res = (3750,6,3)
    return res



def sante(taille, poids):
    """permet de detecter un probleme de santé en fonction
    de l'IMC

    Args:
        taille (float): entrez la taille en metre
        poid (int): entrer le poid en kg

    Returns:
        str: retourne le probleme eventuelement rencontré
    """

    imc = poids/(taille*taille)
    if imc < 16.5:
        res = "famine"
    elif imc < 18.5:
        res = "maigreur"
    elif imc < 25:
        res = "normal"
    elif imc < 30:
        res = "surpoids"
    else:
        res = "obésité"
    return res 


def test_sante():
    assert sante(1.8, 80) == "normal" #sante(1.8, 80) doit retourner normal
    assert sante(1.6, 67) == "surpoid" #sante(1.6, 67) doit retourner surpoid

    
print(sante(1.75, 55))



prog
print(fonction1(23))
print(fonction2(5))
print(algo_1(1,5,7,96))
print(algo2("oiseau"))

