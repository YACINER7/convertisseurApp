# Pull Request : Maintenance Évolutive (Issue #2)

Cette Pull Request ajoute de nouvelles fonctionnalités destinées à enrichir l'expérience utilisateur (UX) et à étendre les capacités de l'application de conversion de devises.

## 🚀 Fonctionnalités Ajoutées

1. **Bouton d'inversion des devises (Permutation)** :
   * **Description** : Ajout d'un bouton `Inverser les devises ⇄` qui permet à l'utilisateur de permuter instantanément la devise source ("De :") et la devise cible ("Vers :").
   * **Technique** : Utilisation de `st.session_state` et d'une fonction de callback (`swap_currencies`) pour modifier l'état de l'application de façon réactive.

2. **Ajout de nouvelles devises** :
   * **Description** : Extension des devises prises en charge avec l'intégration du **GBP** (Livre Sterling) et du **CAD** (Dollar Canadien) dans le dictionnaire des taux de change.

3. **Historique des conversions de la session** :
   * **Description** : Stockage de toutes les conversions réussies effectuées au cours de la session active de l'utilisateur.
   * **Affichage** : Affichage d'une section `📜 Historique des conversions` en bas de page (par ordre chronologique inverse) avec un bouton interactif `Effacer l'historique` pour réinitialiser la liste si souhaité.

## 🔍 Impact sur le code
* Fichier modifié : `app.py`
