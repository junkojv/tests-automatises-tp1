# Réponses - TP Tests Automatisés

## Préparation de l'environnement

J'ai créé le répertoire `tests-automatises-tp1`, puis j'ai cloné le projet `tests-automatises`. J'ai ensuite créé un environnement virtuel Python et installé les dépendances nécessaires, notamment `pytest`, `pytest-cov`, `pytest-mock`, `flask` et `requests`.

## Découverte du projet

Le projet est une application Flask qui expose une API REST. Elle propose deux grandes fonctionnalités : une calculatrice avec les opérations de base et une gestion simple des utilisateurs via une base SQLite.

## Tests unitaires

J'ai créé des tests unitaires pour la classe `Calculator` afin de vérifier les opérations `add`, `subtract`, `multiply` et `divide`, ainsi que le cas particulier de la division par zéro.

J'ai également créé des tests unitaires pour la classe `Database`. J'ai testé l'ajout, la récupération et la suppression d'utilisateurs, ainsi que les cas limites comme un utilisateur inexistant ou un doublon. J'ai utilisé une fixture `pytest` pour initialiser et nettoyer la base de données entre les tests.

## Tests d'intégration

J'ai écrit des tests d'intégration pour l'API avec le client de test Flask. Ces tests vérifient les endpoints de calculatrice et de gestion des utilisateurs. J'ai contrôlé les codes de retour HTTP ainsi que le contenu JSON renvoyé par l'API.

## Utilisation de mocks

J'ai ajouté un test utilisant `pytest-mock` pour simuler le comportement de la base de données dans un endpoint utilisateur. Cela permet de tester le comportement de l'API de manière isolée, sans dépendre directement de la base réelle.

## Couverture de tests

J'ai exécuté les tests avec `pytest --cov=app` puis avec `pytest --cov=app --cov-report=term-missing` pour identifier les lignes non couvertes. J'ai ensuite complété les tests manquants jusqu'à obtenir une couverture de 100% sur l'ensemble du package `app`.

## Bilan

Tous les tests passent correctement et la couverture de code atteint 100%. Le projet est donc entièrement testé sur les parties principales demandées : logique métier, base de données, API, tests avec mocks et analyse de couverture.
