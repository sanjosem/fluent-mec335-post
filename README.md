# fluent-mec335-post

Scripts et module pour le post-traitement des fichiers d'export de Fluent du projet Numérique MEC335

## Prérequis

Le programme nécessite d'installer les package python suivants : 
* numpy
* matplotlib

# Module

Le module `mod_IO_fluent_export` permet de lire les fichiers texte exportés sur des lignes du calcul Fluent d'écoulement en conduite. 
Le nom des fichiers d'entrées peut être modifié. Les mêmes noms devront être utilisés pour tous les calculs. 
La fonction Lecture_fichiers_config lit les différentes variables d'un même calcul dont les données sont regroupées dans un dossier et stocke les données dans un dictionnaire. Le dictionnaire est exporté au format `pickle`.

## Utilisation

0. Les fichiers d'export doivent être déposés dans un dossier. Leurs noms doivent être consistant avec les définitions dans le module `mod_IO_fluent_export`
1. Conversion des fichiers  
    Le script `posttraitement.py` permet de lire les fichiers par lots et de sauvegarder un fichier pickle pour chaque configuration.
    Il faut adapter le nom du répertoire et le nom de la configuration. Plusieurs calculs (configurations) peuvent être traitées en dupliquant le code.
2. Analyse des résultats
    Le script `analyse.py` montre un exemple d'analyse (ici la vitesse au centre de la conduite). Il sert d'exemple pour illustrer comment charger les données avec le module.
    Ce fichier peut-être personnalisé pour les besoins de l'utilisateur. 






