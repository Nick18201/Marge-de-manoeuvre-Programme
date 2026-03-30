---
name: mdm-project-structure
description: Architecture et conventions de nommage des dossiers et fichiers du projet "Marge de manoeuvre". À utiliser pour savoir où placer ou modifier des scripts Python, des documents PDF générés ou des ressources.
---

# Compétence : Structure et Nommage du Projet "Marge de manoeuvre"

Ce projet suit une arborescence très spécifique selon les différentes phases de l'accompagnement des bénéficiaires.

## 1. Arborescence Principale

Les fichiers et dossiers doivent être organisés rigoureusement dans les dossiers suivants :

- `00_Gestion_Projet` : Pour les documents de suivi, de planification et d'organisation globale du projet.
- `01_Phase_Preliminaire` : Pour les fichiers du premier module (Chapitre 0 / Chapitre 1).
- `02_Phase_Investigation_Introspection` : Pour les documents traitant d'exercices d'introspection (ex. Arbre de Vie, Mes Racines, Genogramme).
- `03_Phase_Exploration_Projection` : Pour les fichiers concernant les environnements professionnels et les projections.
- `04_Phase_Conclusion` : Pour les bilans finaux.
- `05_Suivi` : Pour les documents post-programme.

## 2. Emplacement et Nommage des Scripts Python

- **Emplacement Centralisé** : Tous les scripts Python liés à la génération des Workbooks sont centralisés dans le dossier `00_Gestion_Projet/Scripts/`. 
- **Point d'Entrée (Entry Points)** : Les scripts principaux d'exécution doivent être nommés selon la convention `main_generate_chapX.py` (où `X` est le numéro du chapitre).
- **Package `workbook_generator`** : Toute la logique de conception PDF, les composants graphiques et les configurations doivent se trouver dans le package central `00_Gestion_Projet/Scripts/workbook_generator/`.
- **Ressources (Images/Logos)** : Les ressources visuelles nécessaires à la génération (ex. le logo) doivent être appelées de manière robuste via des chemins définis dans la configuration du générateur.

## Quand utiliser cette compétence

- Lorsqu'on vous demande de créer un nouveau script Python, un nouveau document de contenu ou un PDF, référez-vous à cette structure pour déterminer où l'enregistrer.
- Pour identifier rapidement dans quel sous-dossier chercher des ressources existantes si elles manquent à la racine.
