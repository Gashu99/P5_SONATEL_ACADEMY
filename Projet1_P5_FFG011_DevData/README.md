# Projet1_P5_FFG011
# PROJET PYTHON | Dev Data P5<br>
## PROGRESSION:         ![](https://geps.dev/progress/85)


## 1. Récupérer le fichier contenant les données ()
Faites un traitement de ce fichier ensuite mettez les données dans une structure de votre choix
(liste, tuple, dictionnaire ou une combinaison de ses derniers)
 Vous devez séparer les données valides et celles non valide (Une ligne est invalide si une
des informations qu’il contient n’est pas valide) ; pour les ligne invalides vous devez
garder les informations qui l’on rendu invalide
### Les différentes données sont :
### Numéro
Composé de lettre majuscule et de chiffre
Sa taille est 7
## Exemple : H5G32YR ou 54YTG5T
#### Prénom
Commence par une lettre
Contient au moins 3 lettre
#### Nom
Commence par une lettre
Contient au moins 2 lettre
#### Date de naissance
Doit être une date valide
Vous devez choisir un format de date et transformer toutes les dates sous ce format
#### Classe
6em à 3em plus les lettres A & B
Vous devez choisir un format de classe et transformer toutes les classes sous ce format
#### Note
Voici ce que contient la chaine note<br>
👉  Les différentes matières sont séparer par dièse #<br>
👉  Les notes des matières sont dans des crochets []<br>
👉  Les notes de devoir sont séparées par la note d'examen par deux point :<br>
👉  Les notes de devoir sont séparées entre eux par une barre verticale |<br>
### Exemple
Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]
Francais[4|11:13]#Anglais[13,5:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]#Math[12|14,5|11:13]Vous devez garder pour chaque matière<br>
🫴  Les notes de devoir<br>
🫴  La note d’examen<br>
🫴  La moyenne [moyenne = (moyenne(note)+2*note_examen)/3]
## 2. Créer un menu permettant<br>
🫴  D’afficher les informations (Valide ou invalide ; au choix)<br>
🫴  D’afficher une information (par son numéro)<br>
🫴  D’afficher les cinq premiers<br>
🫴  D’ajouter une information en vérifiant la validité des informations données.<br>
🫴  De modifier une information invalide ensuite le transférer dans la structure où se
trouve les informations valides<br>
## 3. Dans cette partie l’affichage se fera par pagination.<br>
🫴  Dans le premier cas vous paginez par 5 lignes<br>
🫴  Dans le second cas vous demandez à l’utilisateur de choisir par combien de ligne il
veut paginer<br>