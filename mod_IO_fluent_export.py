import os
import numpy as np
import pickle


# Noms des fichiers attendus (peut-etre modifie)
noms_fichiers = {}
noms_fichiers['Vc'] = 'vcentre.xy'
noms_fichiers['tau_w'] = 'tau_wall.xy'
noms_fichiers['dPdX'] = 'grad_p_axe.xy'
noms_fichiers['pression'] = 'pression_axe.xy'

# Fonction pour trouver les lignes avec parentheses
def trouver_lignes_avec_parentheses(nom_fichier):
    lignes_avec_parentheses = []
    with open(nom_fichier, 'r') as f:
        for num_ligne, ligne in enumerate(f, start=1):
            if '(' in ligne or ')' in ligne:
                lignes_avec_parentheses.append((num_ligne, ligne.strip()))
    return lignes_avec_parentheses

# Fonction pour lire les donnees dans un tableau numpy
def lire_fichier_xy(nom_fichier,debut,fin):
    data = np.loadtxt(nom_fichier, delimiter='\t',
            skiprows=debut, max_rows=fin)
    return data

def Lecture_fichiers_config(repertoire,nom_config,save=True):
    # Nombre de points
    filename = os.path.join(repertoire,noms_fichiers['Vc'])
    lines = trouver_lignes_avec_parentheses(filename)
    # Numero de ligne (en comptant a partir de 0)
    ligne_debut = lines[-2][0]
    ligne_fin = lines[-1][0]-2
    Nx = ligne_fin - ligne_debut + 1 
    print(f"Nombre de points sur l'axe: {Nx}")
    # NB: nb pts = nb cell + 1

    # Lecture des donnees
    donnees = {}
    for item in noms_fichiers.keys():
        filename = os.path.join(repertoire,noms_fichiers[item])
        data = lire_fichier_xy(filename,ligne_debut,Nx)
        if not 'X' in donnees.keys():
            donnees['X'] = data[:,0]
        donnees[item] = data[:,1]
        print(f'Variable lue: {item}')

    if save:
        with open(f'{nom_config}_Axe.pkl', 'wb') as fih:
            pickle.dump(donnees, fih, protocol=pickle.HIGHEST_PROTOCOL)
        print(f'Fichier sauvegarde: {nom_config}_Axe.pkl')
    else:
        return donnees

def Charge_Resultats(nom_fichier_pkl):
    with open(nom_fichier_pkl, 'rb') as fih:
        data = pickle.load(fih)
    return data