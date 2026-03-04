# Plan Technique V2 : Le "Workshop Évolutif" (Approche PDF)

Cette version privilégie l'expérience tangible de la création d'un livre personnel. Au lieu d'une interface web, le bénéficiaire construit son "Livre de Profession" chapitre par chapitre.

## 💡 Concept Central : "Construire son Livre"
Le livrable final n'est plus une simple extraction de données, mais un **Workbook PDF complet**, co-écrit par le bénéficiaire (via ses exercices) et le coach (via ses synthèses), assemblé progressivement.

### Flux Logique Type (Intersession)
1.  **Envoi** : Le bénéficiaire reçoit un lien pour le chapitre de la semaine (ex: "Chapitre 1 : Mes Racines").
2.  **Saisie** : Il remplit les exercices via une interface agréable (Formulaire Tally/Typeform) qui guide la réflexion.
3.  **Génération** : L'automation transforme ses réponses en une **page PDF magnifiquement mise en page**.
4.  **Livraison** :
    *   Le PDF est envoyé par email au bénéficiaire ("Voici ton chapitre écrit").
    *   Le PDF est sauvegardé dans son **Dossier Partagé** (Google Drive/Dropbox).
5.  **Analyse** : L'IA lit les réponses brutes et envoie une synthèse au coach.

---

## 🏗️ Architecture "No-Code"
*   **Interface Bénéficiaire** : Emails + Formulaires (Tally.so / Typeform).
*   **Orchestration** : Make (Integromat) ou Zapier.
*   **Génération de Documents** : Documer, PDFMonkey ou Google Docs Templating.
*   **Stockage** : Google Drive (Un dossier par client, partagé avec le coach).

---

## 📅 Détail du Parcours "Workbook"

### Phase 0 : Le Cadrage
*   **Action** : Validation de l'inscription.
*   **Automation** :
    *   Création du dossier Drive `[Nom_Client]_MDM_Programme`.
    *   Génération de la **Page de Garde** personnalisée (Nom, Date).
    *   Envoi du **Chapitre 0 : Mon Engagement** (Contrat + Attentes).

### S1 -> S2 : Le Chapitre "Racines"
*   **Exercice** : Ligne de vie & Héritage.
*   **Formulaire** :
    *   Question : "Racontez un souvenir fort lié au travail de votre père..."
    *   Outil : Timeline interactive dans le formulaire.
*   **Rendu PDF** : Une page avec une frise chronologique dessinée et ses textes mis en exergue.

### S2 -> S3 : Le Chapitre "Identité"
*   **Exercice** : 360° Bienveillant.
*   **Différence Technique** :
    *   Le bénéficiaire donne les emails de ses proches.
    *   Les proches remplissent un formulaire externe.
    *   **Automation** : Compile toutes les réponses des proches dans une page PDF "Le Regard des Autres", ajoutée au dossier *avant* la séance.

### S4 -> S5 : Le Chapitre "Relation à l'Argent"
*   **Exercice** : Lettre à l'Argent.
*   **Formulaire** : Champ texte libre "Cher Argent..."
*   **Analyse IA (Invisible)** :
    *   Le texte est envoyé à GPT-4.
    *   Prompt : "Analyse le ton émotionnel et identifie les croyances limitantes (ex: 'L'argent est sale')."
    *   Résultat : Envoyé *uniquement* au coach par email pour préparer la séance.
*   **Rendu PDF** : La lettre mise en forme comme un courrier officiel, intégrée au Workbook.

### Phase Finale : L'Assemblage
*   **Fin de Parcours (S8)**.
*   **Automation Finale** :
    *   Fusion de tous les PDF du dossier (Garde + Chapitres 1 à 7 + Synthèses Coach).
    *   Ajout d'une Table des Matières.
    *   Envoi du **Grand Livre** final (PDF HD prêt à imprimer).

---

## 📊 Comparatif Rapide V1 vs V2

| Critère | V1 (App Web) | V2 (Workbook PDF) |
| :--- | :--- | :--- |
| **Expérience Client** | Moderne, Dashboard, Digital. | "Livre d'Or", Tangible, Progressif. |
| **Complexité Tech** | Élevée (Dev Custom, Auth, DB). | Moyenne (Liaison d'outils No-Code). |
| **Coût Maintenance** | Abonnement App + Hébergement. | Abonnements SaaS (Make, Tally, Drive). |
| **Flexibilité** | Rigide (Changer un écran demande du code). | Souple (Changer une question = Changer le formulaire). |
| **Livrable** | Accès à une plateforme (éphémère ?). | Un fichier PDF définitif (pérenne). |

Cette approche V2 permet de garder la puissance de l'IA (analyse des formulaires) tout en offrant un rendu "Old School / Premium" (le livre) que le client conserve précieusement.
