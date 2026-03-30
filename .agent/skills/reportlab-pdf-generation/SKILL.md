---
name: reportlab-pdf-generation
description: Lignes directrices pour la génération de PDF avec ReportLab dans le projet "Marge de manoeuvre". Utilisée pour s'assurer de la bonne configuration des formulaires interactifs (AcroForm), gestion du multilingue/multiligne et du style.
---

# Compétence : Génération de PDF avec ReportLab

Ce projet utilise massivement la bibliothèque `reportlab` pour créer des carnets de travail (Workbooks) interactifs avec des formulaires PDF remplissables. Suivez ces étapes et conventions lors de la création ou de la résolution de problèmes sur ces PDF.

## Directives et Modèles de Conception

1. **Champs de Texte de Formulaire (AcroForm Text Fields)** :
   - Pour les champs où un bénéficiaire doit saisir de longues réponses, vous **devez** utiliser le support multiligne.
   - Pour garantir un rendu systématiquement correct (multiline, couleurs, scrollbars), instanciez les champs _exclusivement_ via la fonction `create_form_textfield()` du fichier `workbook_generator/forms.py` plutôt que de manipuler directement l'API ReportLab.

2. **Logo en bas de page** :
   - Chaque WorkBook généré doit intégrer une page de fin.
   - Afin d'éviter la duplication de code, appelez la fonction générique `create_closing_page(c)` présente dans `workbook_generator/components.py`. (Se référer à la compétence `mdm-branding` pour les couleurs/polices globales).

3. **Mise en page** :
   - Évitez les chevauchements entre les en-têtes (headers) et le corps du texte (ex. Arbre de Vie).
   - Toute coordonnée X, Y ou dimension de boîte doit être calculée de façon paramétrique. Référez-vous systématiquement au dictionnaire `PDFStyle` dans `workbook_generator/config.py` (ex. `PDFStyle.MARGIN_LEFT`, `PDFStyle.PAGE_WIDTH`).

## Bonnes pratiques

- Lors de la modification d'un script de module (comme `workbook_generator/chapters/chapX.py`), utilisez le retour des fonctions de composants (qui renvoient généralement la nouvelle coordonnée Y `current_y`) pour chainer vos appels de dessin.
- Si le script rencontre des `TypeError`, lisez les fichiers source de ReportLab (`site-packages/reportlab...`) pour confirmer les signatures de méthodes exactes, car il y a des variations entre les versions.

## Quand utiliser cette compétence

- Lors de la résolution de bugs (ex: `TypeError` sur `textfield`, problèmes d'interface utilisateur comme des chevauchements).
- Lors de l'ajout de nouvelles pages (ex: page de conclusion, page de couverture) aux PDF générés.
- Lors de l'ajustement des styles ou du comportement des PDF (scrollbars, couleur de fond).
