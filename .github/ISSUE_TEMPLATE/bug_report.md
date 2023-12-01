---
name: Bug report
about: 'Absence d''affichage de tout les fichiers  '
title: ''
labels: ''
assignees: ''

---

Le programme ne fonctionne pas correctement lorsqu'il est exécuté dans un répertoire contenant des fichiers cachés. Plutôt que d'afficher la liste complète des fichiers, il ne montre que les fichiers non cachés.

Étapes pour Reproduire le Bug :

1/ Placez vous dans un répertoire contenant des fichiers cachés :

2/ Exécutez le programme .

Comportement Attendu :
Le programme devrait afficher la liste complète des fichiers, y compris les fichiers cachés, dans le répertoire spécifié.

Comportement Actuel :
Le programme ne liste que les fichiers non cachés du répertoire, ignorant les fichiers cachés.
