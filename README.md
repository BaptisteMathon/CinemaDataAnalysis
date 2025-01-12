# CinemaDataAnalysis


# Lancement du projet :

Avant d'éxecuter le code présent dans le main.py, il va falloir suivre les étapes suivantes:

1. clone le répo avec la commande suivante : 
  *git clone https://github.com/BaptisteMathon/CinemaDataAnalysis.git*
2. Ce rendre dans le répertoire du fichier main.py depuis le terminal.
3. installer les différentes dépendance avec la commande suivante:
  *pip install pandas numpy matplotlib scikit-learn*
4. Exécuter le code avec la commande suivante:
  *py main.py*

4.1. Si jamais il est nécessaire de créer un environnement pour éxecuter le code, faire les commandes suivantes:
  
  *python3 -m ven venv*

  Windows: *venv\Scripts\Activate.ps1*
  
  Mac / Linux: *source ./venv/bin/activate*

5. Maintenant il ne reste plus qu'à choisir l'exercice souhaité :) 


# Réponse au différentes questions du projet: 

## Question exercice 3: Selon vous, quelle est la variable ayant le plus d'impact sur les entrées annuelles ? Justifiez votre réponse avec les visualisations. 

### Corrélation entre le nombre d'écrans et les entrées de 2022: 
### 0.20610167847673563
### Corrélation entre le nombre de fauteuils et les entrées de 2022: 
### 0.0009999530364899361

### Nuage de points entre le nombre d'écrans et les entrées de 2022:
![image](https://github.com/user-attachments/assets/ec4e0ce8-e373-4d55-87d5-cd26c000b801)

### Nuage de points entre le nombre de fauteuils et les entrées de 2022:
![image](https://github.com/user-attachments/assets/60b2338f-cbdc-4bdd-83c4-365728e92555)

Selon moi, la variable ayant le plus d'impact sur les entrées annuelles est le nombre d'écrans.
Les deux graphiques se ressemble énormément: 
  - Au plus il y a de fauteuil, au plus le nombre d'entrées est élevé
  - Au plus il y a d'écrans, au plus le nombre d'entrées est élevé

Cependant, la régression linéaire du nombre d'écrans est légèrement plus importante que le nombre de fauteuil (comme vu dans les captures ci-dessus)



## Question exercice 4: Selon les performances du modèle, le nombre d'écrans ou de fauteuils est-il un bon prédicteur des entrées ? Expliquez

Le nombre d'écrans serait un bon prédicteur des entrées, car son coefficient (41482.68) est plus élevé que celui du nombre de fauteuil (30.83)
Ce qui veut dire, que pour chaque écran suplémentaire, le nombre d'entrées annuelles augmenterai d'environ 41'483. 
Alors que pour chaque nouveau fauteuil, le nombre d'entrées annuelles augmenterai d'environ 31.

Cependant, on ne peut pas se fier à 100% à se model prédictif, car son Model Score est d'environ 0.54. Ce qui veut dire que certains autres paramètres non inclus dans la prédiction peuvent jouer sur le nombre d'entrées annuelles.


## Question exercice 5: Recommandations statégiques:

* Les calculs sont présent dans le fichier main.py (partie Exercice 5):  *

Comme expliqué dans les exercices ci-dessus, ajouter un nouvel écran permettrait d'augmenter les entrées du cinéma.
Le prix moyen d'un écran de cinéma est de 10'000€, et le prix moyen d'un fauteuil de cinéma est de 200€.
Acheter 50 nouveaux fauteuils reviendrai à achter un nouvel écran de cinéma.

Si l'on calcul le nombre d'entrée potentiel de la commune de 20'000 habitants, avec 2 écrans et 120 fauteuils. On aurait une estimation d'un nombre d'entrées de : 35'541
Si maintenant l'on calcul le nombre d'entrée potentiel mais avec 3 écrans et 120 fauteuils, on obtient une estimation du nombre d'entrée à : 77'024. Soit une augmentation d'environ 40'000 entrées.
Et maintenant le nombre d'entrée potentiel pour un cinéma avec 2 écrans et 170 fauteuils et de : 37'083. Soit une légère augmentation d'environ 2'000 entrées.

Il est donc plus intéressant d'augmenter le nombre d'écrans au nombre de fauteuils pour cette commune de 20'000 habitants.