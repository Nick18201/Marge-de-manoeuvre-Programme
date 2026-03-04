---
name: python-workbook-architecture
description: Architecture et bonnes pratiques de codage pour les scripts Python de génération de PDF du projet "Marge de manoeuvre".
---

# Compétence : Architecture des Scripts Python de Workbooks

Le projet génère des carnets de travail ("Workbooks") via un ensemble de scripts Python (généralement nommés `generate_workbook_chapX_final.py`). Pour s'assurer de la maintenabilité du code, respectez cette architecture.

## 1. Séparation des Préoccupations (Separation of Concerns)

- **Le Contenu (Data / Text)** : Séparez au maximum les textes liés à la "psycho-éducation" (consignes, textes explicatifs, titres) de la logique de rendu PDF. Stockez les textes dans des dictionnaires ou de grands blocs constants au début du script ou dans un fichier de configuration/module séparé.
- **La Logique de Rendu (Rendering Logic)** : Concentrez le dessin du PDF dans des fonctions dédiées (ex. `draw_header()`, `draw_exercise_arbre_de_vie()`). Ces fonctions doivent accepter les données/textes en tant paramètres.

## 2. Gestion de la Mise en Page et Variables Globales

- Évitez les "nombres magiques" (magic numbers) éparpillés dans le code pour positionner visuellement les éléments avec Draw ou ReportLab.
- Groupez les marges, l'espacement entre chapitres, les hauteurs et largeurs de cadre dans un dictionnaire de style ou un bloc de constantes (ex. `MARGIN_LEFT = 50`, `HEADER_Y_POS = 750`).
- Mettez à profit les méthodes qui calculent automatiquement la hauteur des blocs de texte pour ajuster la position Y des éléments subséquents au lieu de la "deviner".

## 3. Gestion des Erreurs et Robustesse

- Prévoyez des `try...except` pertinents en encapsulant les méthodes à risques (gestion d’imports de fonts ou le chargement d'images de police/logos).
- Assurez-vous que les imports de `reportlab.pdfgen.canvas`, `reportlab.lib.colors`, et la gestion des formulaires AcroForm sont toujours appelés correctement selon la version de la bibliothèque installée.

## Quand utiliser cette compétence

- Lors de la création d'un nouveau script `generate_workbook_chapX_final.py`.
- Lors de la refactorisation d'un script long, monolithique ou causant des décalages dans le dessin de la page PDF.
