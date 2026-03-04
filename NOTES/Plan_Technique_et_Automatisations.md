# Plan Technique & Automatisations du Parcours MDM

Ce document détaille le parcours utilisateur (Coach & Bénéficiaire) pour identifier les besoins en automatisation, communication (emails), analyse IA, et développement (Front/Back) à chaque étape.

## 🏗️ Architecture Globale
*   **Frontend (App Web)** :
    *   **Espace Bénéficiaire** : Tableau de bord, accès aux exercices, progression, Livret de Compétences évolutif.
    *   **Espace Coach** : CRM, vue d'ensemble des bénéficiaires, accès aux résultats d'exercices, rapports d'analyse IA.
*   **Backend** : Base de données (Utilisateurs, Progression, Réponses exercices), API.
*   **Moteur IA** : Analyse des réponses textuelles (Croyances, Biographie, Enquêtes) pour fournir des synthèses au coach.
*   **Automation** : Envoi d'emails transactionnels, déblocage de contenus programmés.

---

## 📅 Phase 0 : Onboarding & Cadrage

### 1. Prise de Contact & RDV Découverte
*   **Actions** : Bénéficiaire réserve un créneau (ex: Calendly/Cal.com).
*   **Automatisations** :
    *   (Mail) Confirmation de RDV + Lien Visio.
    *   (Mail - J-24h) Rappel RDV.
    *   (Mail - Immédiat) Envoi du **Formulaire de Cadrage**.
*   **Tech / Outils** :
    *   Intégration Calendrier.
    *   **Formulaire Cadrage (Typeform/Tally ou Intégré)** : Questions sur la situation actuelle.
*   **Analyse IA** :
    *   Résumé de la situation du prospect à partir du formulaire pour préparer le coach avant l'appel.

### 2. Validation & Contrat
*   **Trigger** : Le Coach valide le démarrage après le RDV gratuit.
*   **Automatisations** :
    *   (Mail) Envoi Contract/Convention + Lien de paiement (Stripe).
    *   (Admin) Création du compte utilisateur "Espace Bénéficiaire".
*   **Tech** :
    *   Signature électronique (DocuSign/Yousign API).
    *   Paiement en ligne.

### 3. Démarrage (Onboarding)
*   **Trigger** : Contrat signé + Paiement acompte.
*   **Automatisations** :
    *   (Mail) Bienvenue + Identifiants de connexion.
    *   (App) Déblocage du module "Bienvenue" & "Session 1".

---

## 📅 Phase 1 : Préliminaire & Exploration (S1-S3)

### Session 1 : Analyse & Alliance
*   **Pré-séance** :
    *   (App) Accès au "Jeu des Émotions" (Outil interactif de sélection).
*   **Pendant la séance** :
    *   Saisie en direct (par le coach ou bénéficiaire) des "Objectifs Boussole".
*   **Tech** :
    *   **Livret de Compétences (P4)** : Initialisation de la brique "Objectif".

### Intersession 1 (Vers S2)
*   **Actions Bénéficiaire** :
    *   Remplir "Analyse du Parcours" (Chronologie interactive).
    *   Remplir "Enquête Familiale" (Héritage).
*   **Automatisations** :
    *   (Mail) Récapitulatif S1 + Lien vers exercices S2.
    *   (App) Formulaire structuré pour l'héritage (Arbre simplifié ?).
*   **Analyse IA** :
    *   **Analyse Héritage** : Détection des schémas répétitifs ou mots-clés émotionnels dans les réponses sur la famille.

### Session 2 : Rétroviseur
*   **Pendant la séance** :
    *   Visualisation de la "Ligne de vie" générée.
    *   Validation des compétences extraites -> **Livret (P2 Parcours)**.

### Intersession 2 (Vers S3)
*   **Actions Bénéficiaire** :
    *   Passer Test MBTI (Lien externe ou intégré).
    *   Lancer le **360° Bienveillant**.
*   **Automatisations** :
    *   (Mail) Vers le bénéficiaire : Instructions MBTI.
    *   **Système 360°** : Le bénéficiaire entre les emails de 4-6 proches -> La plateforme envoie les formulaires -> La plateforme agrège les réponses anonymisées.
*   **Analyse IA** :
    *   **Synthèse 360°** : Résumé des points forts récurrents cités par les proches.

### Session 3 : Personnalité & Moteurs
*   **Pendant la séance** :
    *   Review des résultats MBTI & 360°.
    *   Saisie des "Moteurs" -> **Livret (P1 Profil)**.

---

## 📅 Phase 2 : Investigation & Alignement (S4-S6)

### Intersession 3 (Vers S4)
*   **Actions Bénéficiaire** :
    *   Tri des Valeurs (Drag & Drop interface).
    *   Test Intérêts (Hexa3D/RIASEC).
*   **Tech** :
    *   Outil interactif de hiérarchisation des valeurs.

### Session 4 : Croyances & Argent
*   **Pendant la séance** :
    *   Quiz "Money Script" (Résultat immédiat).
    *   Saisie "Biographie Financière".
*   **Analyse IA** :
    *   **Profiling Financier** : Corrélation entre le Money Script et la Biographie pour suggérer des pistes de déblocage au coach.

### Intersession 4 (Vers S5)
*   **Actions Bénéficiaire** :
    *   "Lettre à l'Argent" (Éditeur de texte riche).
    *   Action "Générosité Stratégique" (Journal de bord).
*   **Automatisations** :
    *   (Mail) Encouragement & Rappel "Mindset d'Abondance".

---

## 📅 Phase 3 : Projection & Concrétisation (S5-S8)

### Intersession 5 (Vers S6) - Enquêtes
*   **Actions Bénéficiaire** :
    *   Organisation des "Enquêtes Métier".
*   **Tech** :
    *   **CRM Candidat** : Outil simple pour lister les contacts, dates de RDV, et notes de débriefing.

### Session 6 : Faisabilité
*   **Pendant la séance** :
    *   Validation du "Plan A".
    *   Matrice de faisabilité (Formulaire interactif avec scoring ?).
    *   Mise à jour **Livret (P3 Preuves)** avec les validations terrain.

### Intersession 6 + (Vers S7)
*   **Actions Bénéficiaire** :
    *   Consultation modules autonomie (Job Crafting, LinkedIn...).
    *   Rédaction "Plan d'Action".

### Session 7 : Synthèse & Livret
*   **Tech** :
    *   **Génération du Livret de Compétences** : PDF dynamique généré à partir de toutes les données accumulées (P1, P2, P3, P4).
    *   Validation finale du Plan d'Action (Timeline interactive).

## 📊 Résumé des Besoins Clés

| Type | Besoin | Exemple Concret |
| :--- | :--- | :--- |
| **Backend** | Stockage structuré | Sauvegarder "Valeurs", "Compétences", "Parcours" séparément pour générer le Livret. |
| **Frontend** | UX/UI Interactive | "Tri de cartes" pour les valeurs, "Timeline" pour le parcours, "Arbre" pour l'héritage. |
| **Automation** | Gestionnaires de tâches | Envoi automatique des formulaires 360° aux proches. |
| **A.I.** | Assistant Analyse | Synthétiser 6 réponses de 360° en 1 paragraphe de points forts. |
| **Admin** | Dashboard Coach | Voir la progression de *tous* les bénéficiaires en un coup d'œil. |
