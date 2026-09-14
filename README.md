# prix-Goncourt-2026
Evaluation python 

# Objectif
Ce projet a été réalisé afin de mettre en pratique les notions suivantes :

 démonstration ; 
• diagrammes UML (cas d’utilisation, classes, en option séquence) ; 
• spécifications fonctionnelles ; 
• base de données : MCD, script SQL de création, droit restreint sur celle-ci ; 
• couche modèle conforme au diagramme de classes ; 
• couche DAO ; 
• couche métier, puis couche application ; 
• utilisation de Git et de toutes les bonnes pratiques vues depuis le début (POO, typage 
statique, exceptions, journalisation éventuellement, anglais, lisibilité, docstrings, tests 
éventuellement).

# Enoncé de l' exercice :
Le prix Goncourt 2026 sera attribué mardi 3 novembre, au restaurant Drouant à Paris, à l'issue 
de trois sélections successives :

• mercredi 2/9 : première sélection comportant une liste de 16 romans ; 
• mardi 6/10 : deuxième sélection, réduite à 8 romans ; 
• mardi 27/10 : troisième sélection, révélant les 4 romans finalistes.

Chaque livre1 porte un titre, est décrit par un résumé, est écrit par un auteur, est publié par un 
éditeur et comporte un ou plusieurs personnages principaux2. Il est également caractérisé par 
une date de parution, un nombre de pages, un ISBN et un prix éditeur. En outre, chaque 
auteur peut être décrit – de façon optionnelle – par une biographie.

Le jury est constitué des membres de l'académie Goncourt, qui est composée d'un ensemble 
de personnalités de l'écriture et présidée par l'une d'elles. Celui-ci établit trois sélections 
successives et attribue le prix Goncourt à l'auteur du roman primé à l'issue d'un dernier tour 
de scrutin lors duquel il obtient un certain nombre de voix, suivi par d'autres romans ayant 
obtenu moins de voix.

Il est demandé d'écrire une application en mode console permettant : 

• à tout utilisateur d’afficher les livres composant chaque sélection, avec toutes les 
informations figurant ci-dessus ; 
• au président du jury d’indiquer les livres faisant partie de la deuxième et troisième 
sélection ; 
• au président du jury d’indiquer le nombre de votes obtenus par chaque livre présent au 
dernier tour de scrutin ; 
• dans le futur, d’ajouter une authentification pour chaque membre du jury, leur permettant 
de voter pour les deuxième et troisième sélections, ainsi que pour le lauréat (l’ensemble 
étant alors calculé automatiquement) ;

L’ensemble des données de départ pourra être entré en dur (par ex. avec PHPMyAdmin) dans 
la base de données MariaDB utilisée, en se limitant à la description détaillée des huit titres des 
huit premiers auteurs dans l'ordre alphabétique de leur nom, et en ne renseignant pour les 
autres que le titre, l'auteur et l'éditeur. 

On veillera à limiter au maximum la redondance dans le modèle de données choisi et à 
permettre facilement l'extension de ce modèle à un ensemble de livres plus large (dans lequel 
notamment, un même auteur pourrait apparaître pour plusieurs livres3), par exemple 
l'ensemble des livres sélectionnés pour le prix Goncourt depuis sa création, ou celui des livres 
sélectionnés pour tous les prix littéraires en France en 2026. 
Webographie : 
• Prix Goncourt 2026 : permet d'obtenir toutes les données demandées 
• http://academie-goncourt.fr > Prix Goncourt 2026, Le Prix GONCOURT:  Sélections et 
Lauréats par année 
• Prix Goncourt — Wikipédia 

Contrainte technique : Votre application doit respecter – ou s’inspirer de – l’architecture 
multicouches vue lors du module Python avancé (application Ecole). 

# Technologies utilisées

- Python 3.14
- Git / GitHub
- Php My admin
- looping
- drawio

# Améliorations possibles