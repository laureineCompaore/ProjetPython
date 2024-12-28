# Projet Python pour la data science : PREDICTION DE LA TEMPERATURE 
 

## Introduction


Dans un contexte de changements climatiques rapides et de défis environnementaux croissants, la compréhension et la prévision des variations de température moyenne jouent un rôle crucial. Ces informations permettent d'anticiper les impacts sur l'agriculture, la santé publique, les écosystèmes et l'économie mondiale.

La modélisation de la température moyenne est un domaine clé où le machine learning offre des outils puissants pour analyser de grandes quantités de données et identifier des tendances complexes. En exploitant les données climatiques historiques, ces modèles permettent de capturer les variations saisonnières, les anomalies météorologiques et d'autres facteurs influençant la température.

Ce projet a pour objectif de construire un modèle de machine learning capable de prédire la température moyenne en fonction de diverses variables telles que l'humidité, les caractéristiques météorologiques et d'autres indicateurs climatiques. Python, en tant que langage polyvalent, est utilisé ici pour son riche écosystème de bibliothèques dédiées au traitement de données (pandas, numpy), à la visualisation (matplotlib, seaborn) et à l'apprentissage automatique (scikit-learn, tensorflow, etc.).


## Revue de littérature : 

**Prédiction de la température :** 

Pour mener à bien ce projet, nous nous sommes inspirés des travaux suivants : 

- [1](https://pythonds.linogaliana.fr) Lino Galiana (2024). Compréhension du travail attendu et apprentissage du travail sur Github

- [2](https://public-api.meteofrance.fr/public/DPObs/v1/liste-stations) API, Météo France. L'extraction des données climatiques.

- [3](https://www.kaggle.com/code/adrianograms/climate-prediction) Adriano Grams (2022). Prédiction du climat.

## Objectifs

En adoptant une approche structurée, ce projet explore les étapes suivantes :

1. Collecte et exploration des données : Analyse des données climatiques historiques.
2. Prétraitement des données : Nettoyage, normalisation et transformation des données.
3. Modélisation : Construction et évaluation de modèles de machine learning adaptés.
4. Interprétation et visualisation : Analyse des résultats et présentation des performances du modèle.

L’objectif final est de fournir un modèle prédictif performant, fiable et explicable, capable d’être utilisé dans des systèmes d’aide à la décision pour relever les défis liés aux variations de température.


## Bases de données

Les données utilisées dans ce projet proviennent de  :

**Les données sur le climat :** [API Météo France](https://public-api.meteofrance.fr/public/DPObs/v1/liste-stations)

## Fonctionnalités utilisées

- Jupyter Notebook pour la création de notebook simplifiée et légère.
- nbformat, nbconvert et graphviz pour la création du fichier main.
- Requests, json, logging, dotenv, StringIO pour la récupération de la base par API. 
- Fonctionnalités offertes par Pandas pour la manipulation des données.
- Matplotlib et Seaborn pour la visualisation.
- Numpy pour le calcul scientifique en Python. 
- Geopandas pour faciliter l'utilisation des données géospatiales.
- Statsmodels, tensorflow et scikit-learn pour la modélisation.

<u> La liste ci-dessus n'est pas exhaustive. <u>

## Brainstorm

- [Jupyter Notebook](https://docs.jupyter.org/en/latest/) est un environnement interactif de développement et d'exécution de code qui permet de créer et de partager des documents contenant du code, des visualisations et du texte explicatif.
- [Pandas](https://pandas.pydata.org/docs/index.html) est une bibliothèque open source fournissant des structures de données et des outils d'analyse de données hautes performances. Elle offre des structures de données flexibles et performantes, notamment le **DataFrame**, l'objet le plus utilisé de Pandas et qui permet de stocker et de manipuler des données tabulaires de manière efficace. 
- [Matplotlib](https://matplotlib.org/stable/index.html) est une bibliothèque complète permettant de créer des visualisations statiques, animées et interactives.
- [Seaborn](https://seaborn.pydata.org/) est une bibliothèque de visualisation de données Python basée sur matplotlib . Il fournit une interface de haut niveau pour dessiner des graphiques statistiques attrayants et informatifs. Elle facilite la création de graphiques basés sur des données DataFrame de pandas.
- [NumPy](https://numpy.org/doc/) est un package pour le calcul scientifique en Python. 
- [Geopandas](https://geopandas.org/en/stable/) permet des opérations spatiales sur les types géométriques.
- [Statsmodels](https://www.statsmodels.org/stable/index.html) est une bibliothèque qui permet l'estimation de différents modèles statistiques, la réalisation de tests statistiques et l'exploration de données statistiques. 


## [Structure du Projet](https://pythonds.linogaliana.fr)

- `ProjetPython/` : Contient les notebooks Jupyter utilisés, ainsi que :

   -`ProjetPython/Données`: Emplacement pour stocker les données collectées.

- `LICENSE/` pour protéger la propriété intellectuelle
- `README.md/` pour mieux comprendre la vocation du projet,
- `fonction.py/` contient toutes les bibliothèques utilisées pour l'analyse.

Le projet est composé de trois notebooks jupyter, soit trois grandes parties : 

1. `Main` : permet d'exécuter en même temps tous les NoteBooks(Temps d'exécution relativement long : environ 10 minutes).
2. `Récupération des données` : qui constitue le coeur du projet, l'objectif est de construire le jeu de données qu'on souhaite manipuler dans les autres parties.
3. `Analyse_Exploratoire&Statistiques_descriptives` : il s'agit de la visualisation et de la description des données.
4. `Modélisation_finale` : pour tester empiriquement les differents modèles utilisés pour prédire la température.
5. `Rapport_final` : Contient une description globale du projet et des différentes variables de la base.
6. `Requirements` : pour créer le tableau des packages dans LICENSE.

## Comment exécuter le projet ?

1. Clonez ce dépôt sur votre machine locale.

   ```bash
   git clone https://github.com/laureineCompaore/ProjetPython.git

&hearts;