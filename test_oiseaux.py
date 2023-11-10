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
    assert oiseaux.est_liste_observations(oiseaux.observations3)==True
    assert oiseaux.est_liste_observations([])==None

def test_max_observations():
    assert oiseaux.max_observations(oiseaux.observations1)==5
    assert oiseaux.max_observations(oiseaux.observations2)==5
    assert oiseaux.max_observations(oiseaux.observations3)==4
    assert oiseaux.max_observations([])==None

def test_moyenne_oiseaux_observes():
    assert oiseaux.moyenne_oiseaux_observes(oiseaux.observations1)==3.0
    assert oiseaux.moyenne_oiseaux_observes(oiseaux.observations2)==2.5
    assert oiseaux.moyenne_oiseaux_observes(oiseaux.observations3)==8/3
    assert oiseaux.moyenne_oiseaux_observes([])==None

def test_total_famille():
    assert oiseaux.total_famille("Corvidé", oiseaux.observations1)==2
    assert oiseaux.total_famille("Passereau", oiseaux.observations2)== 8
    assert oiseaux.total_famille("Passereau", oiseaux.observations3)== 6


def test_construire_liste_observations():
    assert oiseaux.construire_liste_observations(oiseaux.oiseaux, oiseaux.comptage1)== [("Merle", 2), ("Moineau", 5), ("Mésange", 0),("Pic vert", 1), ("Pie", 2), ("Pinson", 0),("Rouge-gorge", 3), ("Tourterelle", 5)]
    assert oiseaux.construire_liste_observations(oiseaux.oiseaux, oiseaux.comptage2)== [("Merle", 2), ("Moineau", 1), ("Mésange", 3),("Pic vert", 0), ("Pie", 0), ("Pinson", 3),("Rouge-gorge", 5), ("Tourterelle", 1)] 
    assert oiseaux.construire_liste_observations(oiseaux.oiseaux, oiseaux.comptage3)== [("Merle", 0), ("Moineau", 0), ("Mésange", 4),("Pic vert", 3), ("Pie", 2), ("Pinson", 1),("Rouge-gorge", 2), ("Tourterelle", 4)]
    

def test_caracteres():
    assert oiseaux.caracteres(oiseaux.observations1, 3)== '    **          **  **  '
    assert oiseaux.caracteres(oiseaux.observations1, 5)== '    **              **  '
    assert oiseaux.caracteres(oiseaux.observations1, 2)== '**  **      **  **  **  '


test_recherche_oiseau()
test_oiseau_le_plus_observe()
test_recherche_par_famille()
test_est_liste_observations()
test_max_observations()
test_moyenne_oiseaux_observes()