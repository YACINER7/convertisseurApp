# Pull Request : Maintenance Corrective (Issue #1)

Cette Pull Request introduit les corrections nécessaires pour résoudre les anomalies identifiées dans la version initiale de l'application de conversion de devises.

## 🛠️ Bugs Corrigés

1. **Validation du montant saisi** :
   * **Problème** : L'utilisateur pouvait lancer une conversion avec un montant nul ou négatif, ce qui n'a pas de sens économique.
   * **Correction** : Ajout d'une condition bloquante vérifiant si le montant est inférieur ou égal à `0.0`. Si c'est le cas, un message d'erreur s'affiche (`st.error("Le montant doit être supérieur à zéro.")`) et le calcul de conversion n'est pas exécuté.

2. **Validation des devises identiques** :
   * **Problème** : L'application permettait de sélectionner la même devise en entrée et en sortie (ex. EUR vers EUR), générant une conversion inutile.
   * **Correction** : Ajout d'une condition d'erreur si la devise source et la devise cible sont identiques. Un message clair s'affiche (`st.error("La devise source et la devise cible ne doivent pas être identiques.")`) pour inviter l'utilisateur à modifier sa sélection.

## 🔍 Impact sur le code
* Fichier modifié : `app.py`
