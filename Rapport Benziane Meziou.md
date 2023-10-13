
## 1. Qu'est ce que lE GIl

Le GIL est un sytème qui empèche plusieurs threads python de s'éxecuter en même temps. Il a été ajouté dans les premiers jours de python pour permettre aux bibliothèques de mieux fonctionner. 

En effet à l'époque les OS géraient mal le multithreading et ça causait problème avec un grand nombre de bibliothèque en particulier celles écrit en C. 

## 2. Temps pris avec et sans le gil 

Pour ces tests on utilise un programme qui countdown de d'un trés grand nombre à 0. c'est un programme simple et peu complexe  qui nous permet de tester de manière pure. 

### 1 sans aucune variables partagées

Avec le gil l'exercice prends 27.273619174957275 s

Sans le gil l'exercice prends 21.000165700912476 s

### 2 avec une variable partagée en lecture

Avec le gil l'exercice prends 3.201810598373413 s

Sans le gil l'exercice prends 2.146207809448242 s


### 3 avec une variable partagée en lecture et en écriture 

Avec le gil l'exercice prends 0.08295106887817383 s

Sans le gil l'exercice prends 3.2432758808135986 s

### 4 comparaison des différents scénarii

L'exécution est plus rapide sans le GIL sauf dans le cas de la variable partagée. 

## 3. applications dans la vie réelle avec accès à une même variable

Dans la vraie vie deux threads peuvent avoir besoin d'accèder à la même variable par exemple dans un word, il y a un thread qui s'occupe de vérifier l'orthographe et un thread qui s'occupe de l'affichage sur l'écran. 