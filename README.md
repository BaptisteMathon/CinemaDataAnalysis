# CinemaDataAnalysis


# dépendances à installer :

- pandas
- numpy
- matplotlib
- scikit-learn


## Question exercice 3: Selon vous, quelle est la variable ayant le plus d'impact sur les entrées annuelles ? Justifiez votre réponse avec les visualisations. 

### Corrélation entre le nombre d'écrans et les entrées de 2022: 0.20610167847673563
### Corrélation entre le nombre de fauteuils et les entrées de 2022: 0.0009999530364899361

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
