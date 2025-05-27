# Introduction
Ce repo sert de démo de Playwright pour la communauté testing de Sogeti.  Le site utilisé pour les différents test est celui d'[AutomateNow](https://practice-automation.com/).


# Installation

```
pip install --upgrade pip
pip install playwright
playwright install
```
Playwright automatise les interactions web, mais on a besoin de *pytest* pour créer des instances de tests.

# Composition du repo

Le dossier **demo** possède les différents fichiers de tests. 

```premiere_instance.py``` montre la structure classique d'un automate Playwright. 

```test_premier.py``` montre la structure classique d'un test Playwright avec pytest. On y trouve également les stratégies de locator.

```test_benchmark_pw.py``` est un fichier de test pour 3 fonctionalités disponibles sur le site d'AutomateNow: Le formulaire, les évenements aux clics et les "modals". Il est utile pour comparer les performances de Playwright avec celles de Selenium. 

```test_misc.py``` est quant à lui présent pour tester les autres fonctionalités disponibles sur AutomateNow.



Le dossier **pages** contient les différentes pages de fonctionalité d'AutomateNow, puisque les fichiers de test suivent le design pattern de Page Object Model.
