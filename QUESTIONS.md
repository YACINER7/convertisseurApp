# Questions de réflexion

## 1. Gestion de version

**Comment organiser le travail en groupe avec des branches ?**

On crée une branche par tâche ou par type de maintenance : `bugfix/issue-1-corrective`, `feature/issue-2-evolutive`, etc. Chaque membre travaille sur sa branche sans toucher au code des autres. Une fois la tâche finie, on merge sur `main`.

**Quels avantages apportent les Pull Requests par rapport à un push direct sur `main` ?**

Les PR permettent de relire le code avant qu'il soit intégré. On peut repérer des erreurs, poser des questions et valider que les tests passent. Un push direct sur `main` c'est risqué car personne ne vérifie et on peut casser le projet pour tout le monde.

---

## 2. Qualité et tests

**Qu'est-ce qu'un test unitaire et pourquoi est-il important ?**

Un test unitaire vérifie qu'une fonction précise renvoie le bon résultat pour des entrées données. C'est important parce que si on modifie le code plus tard, les tests nous alertent si on a cassé quelque chose sans s'en rendre compte.

**Pourquoi automatiser les tests dans GitHub Actions avant d'accepter une PR ?**

Pour ne pas avoir à les lancer à la main à chaque fois. Si une PR fait échouer un test, GitHub Actions le signale directement et on refuse le merge. Ça évite d'introduire des bugs dans `main`.

---

## 3. Refactoring

**Quelles dettes techniques observez-vous dans le code initial ?**

- Les taux de change sont codés en dur, donc jamais à jour.
- Toute la logique (calcul, interface, validation) est mélangée dans un seul fichier.
- Aucune gestion d'erreur si le montant est nul ou si les devises sont identiques.
- Pas de tests, impossible de vérifier que le calcul est correct.

**Quelles modifications ont amélioré la maintenabilité et la lisibilité ?**

Extraire la logique dans `app_functions.py` sépare clairement ce qui est interface de ce qui est calcul. La fonction `convert()` est simple à lire et à tester indépendamment. Le code est aussi plus facile à faire évoluer sans tout casser.

---

## 4. Maintenance

**Classez vos modifications selon les quatre types de maintenance.**

| Type | Modifications |
|---|---|
| Corrective | Vérification montant nul/négatif, devises identiques, messages d'erreur |
| Évolutive | Bouton inverser les devises, ajout GBP/CAD, historique des conversions |
| Adaptative | Remplacement des taux codés en dur par l'API exchangerate-api.com |
| Perfective | Refactoring dans `app_functions.py`, tests unitaires, CI GitHub Actions, flake8/black |

**Quelle partie vous semble la plus fréquente dans un projet réel ?**

La maintenance corrective et évolutive sont les plus fréquentes. Il y a toujours des bugs à corriger et des fonctionnalités à ajouter selon les retours des utilisateurs. La perfective est souvent mise de côté par manque de temps même si elle est importante sur le long terme.
