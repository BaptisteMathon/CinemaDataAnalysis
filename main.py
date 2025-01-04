import pandas as pd

# Exercice 1: Nettoyage et exploration des données :
# 1.1 Nettoyage :

df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")

# Recherche des valeurs manquantes ou incohérentes : 
# print("Valeurs manquantes ou incohérentes selon les différents champs de cinemas.csv:")
# print(df_cinemas.isnull().sum())

# Affichage des colonnes ayant des valeurs manquantes ou incohérentes : (après avoir executé la commande df_cinemas.isnull().sum())
colonnes_en_defaut = [
    'label Art et Essai',
    'programmateur', 
    'évolution entrées', 
    'entrées 2021'
]

# print("Avant traitement des colonnes en défaut:")
# print(df_cinemas[colonnes_en_defaut])


# Traitement des colonnes en défaut :
df_cinemas = df_cinemas.fillna({
    'label Art et Essai': 'Non renseigné',
    'programmateur': 'Non renseigné',
    'évolution entrées': 0,
    'entrées 2021': 0
})

# Affichage des colonnes ayant des valeurs manquantes ou incohérentes après traitement :
# print("Après traitement des colonnes en défaut:")
# print(df_cinemas[colonnes_en_defaut])


# 1.2 Exploration :

# Affichage des premières lignes du dataset :
print("Premières lignes du fichier cinemas.csv:")
print(df_cinemas.head())

#Affichage des statistiques descriptives des colonnes numériques principales (fauteuils, écrans, entrées 2022, entrées 2021) :
cinemas_filter = [
    'fauteuils',
    'écrans',
    'entrées 2022',
    'entrées 2021'
]

print("Colonnes principales du fichier cinemas.csv:")
print(df_cinemas[cinemas_filter])
