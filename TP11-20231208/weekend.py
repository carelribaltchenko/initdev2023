#Exercice 1

week_end_mai = { 'Pierre' : [12,70,10], 'Paul' : [100], 'Marie' : [15], 'Anna' : []}

def moyenne(weekend):
    """renvoie la moyenne d'argent qui a été dépensé durant ce weekend

    Args:
        weekend (dico): le dictionnaire du weekend

    Returns:
        float: la moyenne de l'argent dépensé
    """    
    cpt=0
    somm=0
    for listes in weekend.values():
        cpt+=1
        for elt in listes:
            somm+=elt
    return somm/cpt

def affiche_bilan_financier(weekend):
    """affiche le nombre de sous que chacun doit persevoir ou donner à l'issue du sejour

    Args:
        weekend (dico): le dico du weekend
    """    
    moy = moyenne(weekend)
    somme_tot=0
    for prenoms, listes in weekend.items():
        if listes==[]:
            print (prenoms, "devra verser", moy, "€")
        else:
            for elt in weekend[prenoms]:
                somme_tot+=elt
            if somme_tot>moy :
                print(prenoms, "doit recevoir", somme_tot - moy, '€')
                somme_tot=0
            elif somme_tot < moy :
                print(prenoms, "doit donner", moy - somme_tot, '€')
                somme_tot=0
            else:
                print(prenoms, "a paye pile le montant qu'il faut")
                somme_tot=0
                




def soupirants(ATM, personne):
    """renvoie tout ceux qu'il faut buter afin de pécho melanie

    Args:
        ATM (dict): la même qu'avant nique toi
        personne (str): tu le fais expres c'est dans le nom

    Returns:
        ens: la liste de schiendler
    """    
    res=set()
    for nom, amour in ATM.items():
        if amour==personne:
            res.add(nom)
    return res




