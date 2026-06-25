# Suivi des Issues & Branches de Maintenance

Ce document répertorie les tickets (Issues) et les branches Git associés pour chaque type de maintenance du projet **Mini-Convertisseur de devises Streamlit**.

---

## 🛠️ 1. Maintenance Corrective
* **Description** : Résolution des bugs existants et validation des entrées utilisateurs.
* **Branche Git** : `bugfix/issue-1-corrective`
* **Issue associée** : **#1 - Sécurisation des entrées et validations**
  * **Tâche 1** : Ajouter une vérification pour empêcher les conversions avec des montants nuls ou négatifs ($Amount \le 0$).
  * **Tâche 2** : Vérifier que la devise source et la devise cible ne sont pas identiques.
  * **Tâche 3** : Afficher des messages d'erreur clairs et conviviaux en cas de non-respect de ces règles.

---

## 🚀 2. Maintenance Évolutive
* **Description** : Ajout de nouvelles fonctionnalités et amélioration de l'expérience utilisateur.
* **Branche Git** : `feature/issue-2-evolutive`
* **Issue associée** : **#2 - Nouvelles fonctionnalités UX & Devises**
  * **Tâche 1** : Ajouter un bouton permettant d'inverser rapidement les devises sélectionnées (source ⇄ cible).
  * **Tâche 2** : Ajouter de nouvelles devises à la liste (ex: `GBP` ou `CAD`).
  * **Tâche 3** : Implémenter un historique des conversions au cours de la session en utilisant `st.session_state`.

---

## 🔌 3. Maintenance Adaptative
* **Description** : Adaptation de l'application à des sources de données externes et dynamiques.
* **Branche Git** : `feature/issue-3-adaptative`
* **Issue associée** : **#3 - Intégration d'une API externe pour les taux de change**
  * **Tâche 1** : Remplacer les taux de change statiques (codés en dur) par un appel à une API externe (ex: [exchangerate-api.com](https://www.exchangerate-api.com/)).
  * **Tâche 2** : Gérer la récupération asynchrone des taux et implémenter un mécanisme de secours (fallback) en cas de panne de l'API.

---

## 💎 4. Maintenance Perfective
* **Description** : Refactorisation du code, tests unitaires, assurance qualité et automatisation CI/CD.
* **Branche Git** : `refactor/issue-4-perfective`
* **Issue associée** : **#4 - Refactoring, Tests unitaires et Intégration Continue (CI)**
  * **Tâche 1** : Extraire et refactoriser la logique métier de conversion dans un fichier séparé `app_functions.py`.
  * **Tâche 2** : Écrire des tests unitaires complets dans `test_app.py`.
  * **Tâche 3** : Assurer la conformité du code avec les standards `flake8` et `black`.
  * **Tâche 4** : Mettre en place un workflow GitHub Actions (`.github/workflows/python-tests.yml`) pour exécuter automatiquement les tests à chaque Pull Request.
