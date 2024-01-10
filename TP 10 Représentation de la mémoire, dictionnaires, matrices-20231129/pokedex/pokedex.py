"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke, types in pokedex:
        if pokemon==poke:
            return True


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    type_stab=set()
    for poke, types in pokedex:
        if poke==pokemon:
            type_stab.add(types)
    return type_stab


def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt=0
    for poke, types in pokedex:
        if types==attaque:
            cpt+=1
    return cpt


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dico={}
    for poke, types in pokedex:
        if types not in dico.keys():
            dico[types]=1
        else:
            a=dico[types]
            a+=1
            dico[types]=a
    print(dico)
    nb_res=0
    for types, nb in dico.items():
        if nb>nb_res:
            res=types
            nb_res=nb
    print(res, nb_res)
    return res



# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    return pokemon in pokedex.keys()


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    return pokedex[pokemon] if appartient_v2 else None


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt=0
    for type in pokedex.values():
        if attaque in type:
            cpt+=1
    return cpt


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dico={}
    for type in pokedex.values():
        for elt in type:
            if elt not in dico:
                dico[elt]=1
            else:
                val=dico[elt]
                val+=1
                dico[elt]=val
    max=0

    for elt,val in dico.items():
        if max<val:
            max=val
            res=elt
    return res
# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke in pokedex.values():
        if pokemon in poke:
            return True
    return False


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt=0
    for type,poke in pokedex.items():
        if type==attaque:
            cpt=len(poke)
    return cpt

def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    res=set()
    for type,poke in pokedex.items():
        if pokemon in poke:
            res.add(type)
    return res

def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dico={}
    for type in pokedex.keys():
        dico[type]=nombre_de_v3(type,pokedex)
    max=0

    for elt,val in dico.items():
        if max<val:
            max=val
            res=elt
    return res

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    dico={}
    for poke,type in pokedex_v1:
        if poke not in dico:
            ens=set()
            ens.add(type)
            dico[poke]=ens
        else:
            ens=set(dico[poke])
            ens.add(type)
            dico[poke]=ens
    return dico


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    dico=dict()
    for poke, types in pokedex_v2.items():
        for types_val in types:
            if types_val not in dico.keys():
                dico[types_val]=set()
            dico[types_val].add(poke)
    return dico

