---
name: python-workbook-architecture
description: Architecture et bonnes pratiques de codage pour les scripts Python de génération de PDF du projet "Marge de manoeuvre".
---

# Compétence : Architecture des Scripts Python de Workbooks

Le projet génère des carnets de travail ("Workbooks") via un ensemble de scripts Python modulaires centralisés dans `00_Gestion_Projet/Scripts/`. 

L'architecture est centralisée autour d'un package Python `workbook_generator` qui rassemble les responsabilités pour garantir une haute maintenabilité.

## 1. L'Architecture Modulaire `workbook_generator`

- **Scripts Principaux (`main_generate_chapX.py`)** : Ce sont les points d'entrée qui instancient le `canvas` principal de ReportLab. Ils importent et appellent successivement les méthodes de génération de pages.
- **Les Chapitres (`workbook_generator/chapters/`)** : Chaque chapitre dispose de son fichier spécifique (ex. `chap3.py`) qui rassemble la logique *spécifique* à ce chapitre (texte psycho-éducatif et appel des composants).
- **Les Composants Réutilisables (`workbook_generator/components.py`)** : Regroupe les fonctions de dessin réutilisables (en-têtes, encadrés, bannières, exercices standards, pages de couverture ou de conclusion) qui s'appliquent potentiellement à plusieurs chapitres.
- **Configuration Globale (`workbook_generator/config.py`)** : Remplace les variables globales ou les constantes éparpillées. Ce fichier définit systématiquement les propriétés de marge (`PDFStyle.MARGIN_LEFT`), les couleurs (`PDFStyle.COLORS.PRIMARY`), et les tailles de polices (`PDFStyle.FONTS.H1_SIZE`).
- **Formulaires (`workbook_generator/forms.py`)** : Centralise la définition des champs textes (multilignes) ou autres éléments AcroForm interactifs.
- **Utilitaires (`workbook_generator/utils.py`)** : Héberge les utilitaires globaux comme le `register_fonts()`.

## 2. Principes Directeurs de Conception (Design Guidelines)

- **Zéro Magic Numbers** : Tout positionnement Y, toute taille, ou marge doit être déduit de `config.py` ou calculé dynamiquement grâce aux fonctions d'utilitaire texte/dessin (exposées dans `utils` ou `components`).
- **Chaînage de la position Y** : Pratiquez la mise à jour continue d'une variable `current_y` ou le retour d'une position depuis chaque appel de fonction pour éviter les calculs figés.

## Quand utiliser cette compétence

- Lors de la création d'un nouveau chapitre (`main_generate_chapX.py`).
- Lors du déplacement de codes monolithiques vers l'architecture de composants.
- Pour identifier où aller chercher ou placer un réglage visuel (dans `config.py`) ou un nouvel élément graphique (`components.py`).
