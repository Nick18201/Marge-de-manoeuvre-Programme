# Workbook - Chapitre 0 : Le Prélude 🕯️
*Ce document sert de spécification pour le contenu textuel, le formulaire de collecte et le rendu PDF.*

---

## 1. Concept & Objectif
*   **Moment** : Envoyé immédiatement après la signature du contrat et le paiement.
*   **Objectif** : Accueillir, rassurer, engager solennellement ("Onboarding rituel").
*   **Ton** : Chaleureux, solennel, professionnel, encourageant.

## 2. Structure du PDF (Rendu Final)

### Page 1 : La Couverture
*   **Visuel** : Fond épuré, typographie élégante.
*   **Textes** :
    *   Titre : "MON LIVRE DE TRANSITION"
    *   Sous-titre : "Bilan de Compétences & Alignement Professionnel"
    *   Variable : `[Prénom] [Nom]`
    *   Variable : `[Date de Démarrage]`

### Page 2 : Bienvenue (Édito)
*   **Titre** : "Bienvenue [Prénom],"
*   **Corps** :
    > "Si vous lisez ceci, c’est que vous avez choisi de vous mettre en mouvement. Bravo.
    > Ce livre n'est pas un simple rapport. C'est le réceptacle de votre histoire, de vos découvertes et de vos ambitions.
    > Il va s'écrire page après page, au rythme de notre travail.
    > Aujourd'hui, nous posons la première pierre."

### Page 3 : Le Cadre de Confiance (Le Pacte)
*   **Concept** : Une version "noble" des règles du jeu.
*   **Les 3 Piliers** :
    1.  **Confidentialité** : "Tout ce qui se dit ici, reste ici."
    2.  **Authenticité** : "Pas de masque. C'est votre vérité qui compte."
    3.  **Action** : "La clarté vient du mouvement, pas seulement de la pensée."

### Page 4 : Mon Intention (Interactive)
*   **Titre** : "Mon Engagement Envers Moi-même"
*   **Contenu généré** :
    *   "Moi, `[Prénom]`, décide aujourd'hui d'investir `[Heures par semaine]` heures par semaine pour mon avenir."
    *   "Mon objectif principal est de : `[Objectif Principal saisi]`."
    *   "Pour réussir, je m'autorise à : `[Autorisation saisie]` (ex: être imparfait, demander de l'aide)."
*   **Signature** : Espace pour signer (ou signature numérique générée).

---

## 3. Formulaire de Collecte (Source de données)

Le bénéficiaire reçoit un lien Tally/Typeform "Initialisez votre Livre".

**Question 1 : Identité**
*   "Comment souhaitez-vous être nommé(e) dans ce livre ?" (Prénom / Surnom)

**Question 2 : La Motivation (Objectif Boussole V0)**
*   "Si nous avons une baguette magique, quelle serait votre situation idéale à la fin de ce bilan, dans 3 mois ?" (Texte libre)
*   *Usage : Sera synthétisé pour la Page 4.*

**Question 3 : L'Engagement**
*   "Combien de temps pouvez-vous *réalistement* consacrer à votre travail personnel chaque semaine ?" (Choix unique : 1h, 2h, 3h+)

**Question 4 : L'Autorisation**
*   "Quelle permission avez-vous besoin de vous donner pour vivre ce processus pleinement ?"
    *   Exemples : "Me tromper", "Prendre mon temps", "Changer d'avis".
*   *Usage : Page 4.*

---

## 4. Instructions Techniques (Automation)

1.  **Trigger** : Nouveau formulaire soumis (Tally).
2.  **Action 1** : Formater la date actuelle (ex: "Janvier 2026").
3.  **Action 2 (Génération PDF)** :
    *   Remplir le template `Workbook_Cover.docx` avec `[Nom]`.
    *   Remplir le template `Workbook_Chap0.docx` avec les réponses.
4.  **Action 3 (Merge)** : Fusionner les 2 fichiers en `[Nom]_Livre_Chap0.pdf`.
5.  **Action 4 (Envoi)** : Email avec pièce jointe + Sauvegarde Drive.
