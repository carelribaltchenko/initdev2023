import oiseaux
# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_recherche_oiseau():
    assert oiseaux.recherche_oiseau("Merle")=="Turtidé"
    assert oiseaux.recherche_oiseau("Moineau")=="Passereau"
    assert oiseaux.recherche_oiseau("Pie")=="Corvidé"
    assert oiseaux.recherche_oiseau("toto")==None

def test_recherche_par_famille():
    assert oiseaux.recherche_par_famille("Passereau")==["Moineau","Mésange","Pinson","Rouge-gorge"]
    assert oiseaux.recherche_par_famille("Corvidé")==["Pie"]
    assert oiseaux.recherche_par_famille("Turtidé")==["Merle"]
    assert oiseaux.recherche_par_famille("toto")==[]

def test_oiseau_le_plus_observe():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe([])==None

def test_est_liste_observations():
    assert oiseaux.est_liste_observations(oiseaux.observations1)==True
    assert oiseaux.est_liste_observations(oiseaux.observations2)==False
    assert oiseaux.est_liste_observations(oiseaux.observations3)==True
    assert oiseaux.est_liste_observations([])==None

def test_max_observations():
    assert oiseaux.max_observations(...)==...

def test_moyenne_oiseaux_observes():
    assert oiseaux.moyenne_oiseaux_observes(...)==...

def test_total_famille():
    assert oiseaux.total_famille(...)==...


def test_construire_liste_observations():
    assert oiseaux.construire_liste_observations(...)==...

def test_creer_ligne_sup():
    assert oiseaux.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert oiseaux.creer_ligne_noms_oiseaux(...)==...


test_recherche_oiseau()
test_oiseau_le_plus_observe()
test_recherche_par_famille()
test_est_liste_observations()