import troupeaux


def test_total_animaux():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {'chevache':3, 'le poulet':8, 'troll':19}
    assert troupeaux.total_animaux(troupeau_de_perrette) == 63
    assert troupeaux.total_animaux(troupeau_de_jean) == 32
    assert troupeaux.total_animaux(troupeau_vide) == 0
    assert troupeaux.total_animaux(mon_troupeau) == 30

test_total_animaux()


def test_tous_les_animaux():
    jean = {'vache':12, 'cochon':17, 'veau':3}
    vide = dict()
    perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {'chevache':3, 'le poulet':8, 'troll':19}    
    assert troupeaux.tous_les_animaux(perrette) == {'veau', 'vache', 'poule'}
    assert troupeaux.tous_les_animaux(jean) == {'veau', 'vache', 'cochon'}
    assert troupeaux.tous_les_animaux(vide) == set()
    assert troupeaux.tous_les_animaux(mon_troupeau) == {'chevache', 'le poulet', 'troll'}

test_tous_les_animaux()

def test_specialise():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {'chevache':3, 'le poulet':8, 'troll':19}    
    assert troupeaux.specialise(troupeau_de_perrette)
    assert not troupeaux.specialise(troupeau_de_jean)
    assert not troupeaux.specialise(troupeau_vide)
    assert not troupeaux.specialise(mon_troupeau)

test_specialise()

def test_quantite_suffisante():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {'chevache':3, 'le poulet':8, 'troll':19}    
    assert troupeaux.quantite_suffisante(troupeau_de_perrette)
    assert not troupeaux.quantite_suffisante(troupeau_de_jean)
    assert troupeaux.quantite_suffisante(troupeau_vide)
    assert not troupeaux.quantite_suffisante(mon_troupeau)

test_quantite_suffisante()

def test_le_plus_represente():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_vide = dict()
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    mon_troupeau = {'chevache':3, 'le poulet':8, 'troll':19}    
    assert troupeaux.le_plus_represente(troupeau_de_perrette) == 'poule'
    assert troupeaux.le_plus_represente(troupeau_de_jean) == "cochon"
    assert troupeaux.le_plus_represente(troupeau_vide) is None
    assert troupeaux.le_plus_represente(mon_troupeau) == 'troll'

test_le_plus_represente()

def test_reunion_troupeaux():
    troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
    troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
    troupeau_vide = dict()    
    mon_troupeau = {'chevache':3, 'le poulet':8, 'troll':19}
    assert troupeaux.reunion_troupeaux(troupeau_de_perrette, troupeau_vide) == troupeau_de_perrette
    assert troupeaux.reunion_troupeaux(troupeau_vide, troupeau_de_jean) == troupeau_de_jean
    assert troupeaux.reunion_troupeaux(troupeau_de_perrette, troupeau_de_jean) == {'vache':12+7, 'cochon':17, 'veau':3+14, 'poule':42}
    assert troupeau_de_jean == {'vache':12, 'cochon':17, 'veau':3}
    assert troupeau_de_perrette == {'veau':14, 'vache':7, 'poule':42}
    assert troupeaux.reunion_troupeaux(troupeau_de_perrette, mon_troupeau) == {'veau':14, 'vache':7, 'poule':42, 'chevache':3, 'le poulet':8, 'troll':19}
    assert troupeaux.reunion_troupeaux(mon_troupeau, troupeau_de_jean) == {'chevache':3, 'le poulet':8, 'troll':19, 'vache':12, 'cochon':17, 'veau':3}
    assert troupeau_de_jean == {'vache':12, 'cochon':17, 'veau':3}
    assert troupeau_de_perrette == {'veau':14, 'vache':7, 'poule':42}

test_reunion_troupeaux()




