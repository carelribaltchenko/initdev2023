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

