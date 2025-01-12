import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Exercice 1: Nettoyage et exploration des données :
# Nettoyage :

def exercice1():  
# Recherche des valeurs manquantes ou incohérentes : 
    df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")

    print("Valeurs manquantes ou incohérentes selon les différents champs de cinemas.csv:")
    print(df_cinemas.isnull().sum())

# Affichage des colonnes ayant des valeurs manquantes ou incohérentes : (après avoir executé la commande df_cinemas.isnull().sum())
    colonnes_en_defaut = [
        'label Art et Essai',
        'programmateur', 
        'évolution entrées', 
        'entrées 2021'
    ]

    print("Avant traitement des colonnes en défaut:")
    print(df_cinemas[colonnes_en_defaut])


# Traitement des colonnes en défaut :
    df_cinemas = df_cinemas.fillna({
        'label Art et Essai': 'Non renseigné',
        'programmateur': 'Non renseigné',
        'évolution entrées': 0,
        'entrées 2021': 0
    })

# Affichage des colonnes ayant des valeurs manquantes ou incohérentes après traitement :
    print("Après traitement des colonnes en défaut:")
    print(df_cinemas[colonnes_en_defaut])


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

def exercice2():
    df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")

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

    diagram_best_3_communes = moyenne_entrees.sort_values(ascending=False).head(10).reset_index()

    diagram_best_3_communes.columns = ['commune', 'entrées moyennes par fauteuil']

    diagram_best_3_communes.set_index('commune')['entrées moyennes par fauteuil'].plot(kind='bar', figsize=(14, 6))
    plt.title("Entrées moyennes par fauteuil pour les 10 communes avec le plus d'entrée en 2022")
    plt.ylabel('Entrées moyennes par fauteuil')
    plt.xlabel('Communes')
    plt.xticks(rotation=30)
    plt.grid(axis='y')
    plt.legend(title='')
    plt.show()

# Graphique représentant les entrées moyennes par fauteuil pour les 10 communes avec le moins d'entrées en 2022:

    diagram_worst_3_communes = moyenne_entrees.sort_values().head(10).reset_index()

    diagram_worst_3_communes.columns = ['commune', 'entrées moyennes par fauteuil']

    diagram_worst_3_communes.set_index('commune')['entrées moyennes par fauteuil'].plot(kind='bar', figsize=(14, 6))
    plt.title("Entrées moyennes par fauteuil pour les 10 communes avec le moins d'entrée en 2022")
    plt.ylabel('Entrées moyennes par fauteuil')
    plt.xlabel('Communes')
    plt.xticks(rotation=30)
    plt.grid(axis='y')
    plt.legend(title='')
    plt.show()

# Exercice 3: Corrélation entre infrastrucutres et fréquentation :

# Corrélation entre le nombre d'écrans et les entrées de 2022:
def exercice3():
    df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")

    screen = df_cinemas['écrans'].tolist()
    entrees_2022 = df_cinemas['entrées 2022'].tolist()
    total_value_screen = len(screen)

    sum_screen = sum(screen)
    sum_entrees_2022 = sum(entrees_2022)
    sum_products = sum(x * y for x, y in zip(screen, entrees_2022))
    sum_squares_screen = sum(x ** 2 for x in screen)

    numerator = (total_value_screen * sum_products) - (sum_screen * sum_entrees_2022)
    denominator = ((total_value_screen * sum_squares_screen - (sum_squares_screen ** 2)) * (total_value_screen * sum_entrees_2022 - (sum_entrees_2022 ** 2))) ** 0.5

    if denominator != 0:
        correlation_screen_entrees_2022 = numerator / denominator
    else:
        correlation_screen_entrees_2022 = 0

    print("Corrélation entre le nombre d'écrans et les entrées de 2022:")
    print(correlation_screen_entrees_2022)

# Corrélation entre le nombre de fauteuils et les entrées de 2022:

    fauteuils = df_cinemas['fauteuils'].tolist()
    entrees_2022 = df_cinemas['entrées 2022'].tolist()
    total_value_fauteuils = len(fauteuils)

    sum_fauteuils = sum(fauteuils)
    sum_entrees_2022 = sum(entrees_2022)
    sum_products = sum(x * y for x, y in zip(fauteuils, entrees_2022))
    sum_squares_fauteuils = sum(x ** 2 for x in fauteuils)

    numerator = (total_value_fauteuils * sum_products) - (sum_fauteuils * sum_entrees_2022)
    denominator = ((total_value_fauteuils * sum_squares_fauteuils - (sum_squares_fauteuils ** 2)) * (total_value_fauteuils * sum_entrees_2022 - (sum_entrees_2022 ** 2))) ** 0.5

    if denominator != 0:
        correlation_fauteuils_entrees_2022 = numerator / denominator
    else:
        correlation_fauteuils_entrees_2022 = 0

    print("Corrélation entre le nombre de fauteuils et les entrées de 2022:")
    print(correlation_fauteuils_entrees_2022)

# Nuage de points entre le nombre d'écrans et les entrées de 2022:

    X_screens = df_cinemas['écrans']
    Y_entries = df_cinemas['entrées 2022']

    m_screens = ((X_screens * Y_entries).mean() - X_screens.mean() * Y_entries.mean()) / ((X_screens ** 2).mean() - (X_screens.mean() ** 2))
    b_screens = Y_entries.mean() - m_screens * X_screens.mean()

    plt.scatter(X_screens, Y_entries, color='blue', label='Données')
    plt.plot(X_screens, m_screens * X_screens + b_screens, color='red', label='Régression linéaire')
    plt.title("Relation entre le nombre d'écrans et les entrées annuelles (2022)")
    plt.xlabel("Nombre d'écrans")
    plt.ylabel('Entrées annuelles')
    plt.legend()
    plt.grid()
    plt.show()

# Nuage de points entre le nombre de fauteuils et les entrées de 2022:

    X_fauteuil = df_cinemas['fauteuils']
    Y_entries = df_cinemas['entrées 2022']

    m_screens = ((X_fauteuil * Y_entries).mean() - X_fauteuil.mean() * Y_entries.mean()) / ((X_fauteuil ** 2).mean() - (X_fauteuil.mean() ** 2))
    b_screens = Y_entries.mean() - m_screens * X_fauteuil.mean()

    plt.scatter(X_fauteuil, Y_entries, color='blue', label='Données')
    plt.plot(X_fauteuil, m_screens * X_fauteuil + b_screens, color='red', label='Régression linéaire')
    plt.title("Relation entre le nombre de fauteuils et les entrées annuelles (2022)")
    plt.xlabel('Nombre de fauteuils')
    plt.ylabel('Entrées annuelles')
    plt.legend()
    plt.grid()
    plt.show()


# Exercice 4: Modèle prédictif des entrées annuelles:

# Division des données de 2021 et 2022 en deux sous-ensembles:

def exercice4():
    df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")

    variables_explicatives_2021 = df_cinemas[['écrans', 'fauteuils', 'population de la commune']]
    variables_cible_2021 = df_cinemas['entrées 2021']
    print('Variables explicatives 2021 : \n', variables_explicatives_2021.head())
    print('Variable cible 2021 : \n', variables_cible_2021.head())

    variables_explicatives_2022 = df_cinemas[['écrans', 'fauteuils', 'population de la commune']]
    variables_cible_2022 = df_cinemas['entrées 2022']
    print('Variables explicatives 2022 : \n', variables_explicatives_2022.head())
    print('Variable cible 2022 : \n', variables_cible_2022.head())


#---------

    X = variables_explicatives_2022.values
    Y = variables_cible_2022.values

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=1)

    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)

    print('Coefficient des variables explicatives [écrans, fauteuils, population de la commune] : ', regressor.coef_)
    print('Intercept : ', regressor.intercept_)

    Y_pred = regressor.predict(X_test)

    comparison_df = pd.DataFrame({'Réel': Y_test, 'Prédit': Y_pred})
    print('Données réelles VS données prédites : \n', comparison_df)

    print('MAE : ', mean_absolute_error(Y_test, Y_pred))
    print('MSE : ', mean_squared_error(Y_test, Y_pred))
    print('RMSE : ', np.sqrt(mean_squared_error(Y_test, Y_pred)))
    r2 = r2_score(Y_test, Y_pred)
    print('Model Score : ', r2)


# Exercice 5 : Recommandations stratégiques:

#Coefficient écrans : 41482.68
#Coefficient fauteuils : 30.83
#Coefficient population commune : -0.19
#intercept = -47323.89
# Equation de prédiction des entrées annuelles de la commune de 20'000 habitants pour 2 écrans et 120 fauteuils :

# (coefficient écran * écran) + (coefficient fauteuil * fauteuil) + (coefficient population commune * habitant commune) + intercept

def exercice5():

    def entrees_commune_20000(ecran, fauteuil):
        result = (41482.68 * ecran) + (30.83 * fauteuil) + (-0.19 * 20000) + (-47323.89)
        return result

    print("Entrée attendu pour la commune de 20'000 habitants avec 2 écrans et 120 fauteuil : ", entrees_commune_20000(2, 120))
    print("Entrée attendu pour la commune de 20'000 habitants avec 3 écrans et 120 fauteuil : ", entrees_commune_20000(3, 120))
    print("Entrée attendu pour la commune de 20'000 habitants avec 2 écrans et 170 fauteuil : ", entrees_commune_20000(2, 170))



print("Bienvenue dans mon projet CINEMA DATA ANALYSIS")
print("Veuillez choisir le numéro de l'exercice de votre choix")
print("""
    Exercice 1: Nettoyage et exploration des données
    Exercice 2: Analyse des données
    Exercice 3: Corrélation entre infrastructures et fréquentation
    Exercice 4: Modèle prédictif des entrées annuelles
    Exercice 5: Recommandations stratégiques
""")
user_choice = int(input("Entrez le numéro de l'exercice souhaité (1, 2, 3, 4, 5):"))
df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")
if user_choice == 1:
    exercice1()
elif user_choice == 2:
    exercice2()
elif user_choice == 3:
    exercice3()
elif user_choice == 4:
    exercice4()
elif user_choice == 5:
    exercice5()
else:
    print("Numéro d'exercice inconnue !")