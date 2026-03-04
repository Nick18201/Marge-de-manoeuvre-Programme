---
name: reportlab-pdf-generation
description: Lignes directrices pour la génération de PDF avec ReportLab dans le projet "Marge de manoeuvre". Utilisée pour s'assurer de la bonne configuration des formulaires interactifs (AcroForm), gestion du multilingue/multiligne et du style.
---

# Compétence : Génération de PDF avec ReportLab

Ce projet utilise massivement la bibliothèque `reportlab` pour créer des carnets de travail (Workbooks) interactifs avec des formulaires PDF remplissables. Suivez ces étapes et conventions lors de la création ou de la résolution de problèmes sur ces PDF.

## Directives et Modèles de Conception

1. **Champs de Texte de Formulaire (AcroForm Text Fields)** :
   - Pour les champs où un bénéficiaire doit saisir de longues réponses, vous **devez** utiliser le support multiligne.
   - Si les champs standards `textfield` ne supportent pas `multiline=True` par défaut dans votre version ReportLab, privilégiez d'autres moyens de le configurer (voir la documentation source de `reportlab.pdfgen.canvas.acroForm` pour la version installée). 
   - Vous devez vous assurer que les barres de défilement (scrollbars) sont gérées proprement. 
   - Renseignez une couleur de fond claire pour les champs visés, afin de d'indiquer clairement les espaces à remplir (ex: `#f8f9fa` ou la couleur spécifiée par l'utilisateur).

2. **Logo en bas de page** :
   - Chaque WorkBook généré doit intégrer une page de fin.
   - Cette page finale comporte le logo "marge de manoeuvre" (se référer à la compétence mdm-branding pour la police Montserrat Black, souligné, texte rouge) et un message d'encouragement.

3. **Mise en page** :
   - Évitez les chevauchements entre les en-têtes (headers) et le corps du texte (ex. Arbre de Vie).
   - Ajustez minutieusement les coordonnées X, Y pour les boîtes de texte pour une harmonie visuelle.

## Bonnes pratiques

- Lors de la modification de `generate_workbook_chap0_final.py` ou de tout autre script de génération, utilisez un nommage de variable clair pour le placement des éléments.
- Si le script rencontre des `TypeError`, lisez les fichiers source de ReportLab (`site-packages/reportlab...`) pour confirmer les signatures de méthodes exactes, car il y a des variations entre les versions.

## Quand utiliser cette compétence

- Lors de la résolution de bugs (ex: `TypeError` sur `textfield`, problèmes d'interface utilisateur comme des chevauchements).
- Lors de l'ajout de nouvelles pages (ex: page de conclusion, page de couverture) aux PDF générés.
- Lors de l'ajustement des styles ou du comportement des PDF (scrollbars, couleur de fond).
