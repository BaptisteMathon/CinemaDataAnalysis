import pandas as pd
import matplotlib.pyplot as plt

# Exercice 1: Nettoyage et exploration des données :
# Nettoyage :

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


# Exploration :

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


# Exercice 2: Analyse des données :

#  Calcule des entrées moyennes par fauteuil pour chaque région en 2022:

somme_entrees = df_cinemas.groupby('commune')[['entrées 2022', 'fauteuils']].sum()
moyenne_entrees = somme_entrees['entrées 2022'] / somme_entrees['fauteuils']

print("Entrées moyennes par fauteuil pour chaque région en 2022:")
print(moyenne_entrees)

# Les 3 communes avec le plus d'entrées moyenne par fauteuil en 2022:

best_3_communes = moyenne_entrees.sort_values(ascending=False).head(3)

print("Les 3 communes avec le plus d'entrées moyenne par fauteuil en 2022:")
print(best_3_communes)

# Les 3 communes avec le moins d'entrées moyenne par fauteuil en 2022:

worst_3_communes = moyenne_entrees.sort_values().head(3)

print("Les 3 communes avec le moins d'entrées moyenne par fauteuil en 2022:")
print(worst_3_communes)

# Graphique représentant les entrées moyennes par fauteuil pour les 10 communes avec le plus d'entrées en 2022:

# diagram_best_3_communes = moyenne_entrees.sort_values(ascending=False).head(10).reset_index()

# diagram_best_3_communes.columns = ['commune', 'entrées moyennes par fauteuil']

# diagram_best_3_communes.set_index('commune')['entrées moyennes par fauteuil'].plot(kind='bar', figsize=(14, 6))
# plt.title("Entrées moyennes par fauteuil pour les 10 communes avec le plus d'entrée en 2022")
# plt.ylabel('Entrées moyennes par fauteuil')
# plt.xlabel('Communes')
# plt.xticks(rotation=30)
# plt.grid(axis='y')
# plt.legend(title='')
# plt.show()

# Graphique représentant les entrées moyennes par fauteuil pour les 10 communes avec le moins d'entrées en 2022:

# diagram_worst_3_communes = moyenne_entrees.sort_values().head(10).reset_index()

# diagram_worst_3_communes.columns = ['commune', 'entrées moyennes par fauteuil']

# diagram_worst_3_communes.set_index('commune')['entrées moyennes par fauteuil'].plot(kind='bar', figsize=(14, 6))
# plt.title("Entrées moyennes par fauteuil pour les 10 communes avec le moins d'entrée en 2022")
# plt.ylabel('Entrées moyennes par fauteuil')
# plt.xlabel('Communes')
# plt.xticks(rotation=30)
# plt.grid(axis='y')
# plt.legend(title='')
# plt.show()