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

- **Scripts de génération de Workbooks** : Ils doivent être nommés selon la convention `generate_workbook_chapX_final.py` (où `X` est le numéro du chapitre).
- **Emplacement** : Ces scripts doivent être documentés et positionnés logiquement, généralement près des dossiers de conception (`02_Phase_Investigation_Introspection` pour le Chapitre 2, etc.) ou à la racine du projet si le contexte l'exige.
- **Ressources (Images/Logos)** : Les ressources visuelles nécessaires à la génération (ex. le logo) doivent être appelées de manière robuste via des chemins relatifs ou absolus fiables.

## Quand utiliser cette compétence

- Lorsqu'on vous demande de créer un nouveau script Python, un nouveau document de contenu ou un PDF, référez-vous à cette structure pour déterminer où l'enregistrer.
- Pour identifier rapidement dans quel sous-dossier chercher des ressources existantes si elles manquent à la racine.
