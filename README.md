# MONKEY GENERATOR IN PYTHON

Ce qu'il faut faire:
* package pour pip install
* ajouter des fonctionnalitées cool dans le pacakge (par exemple comme dans https://pypi.org/project/python-avatars/)
* stocker les paramètres dans un fichier c mieux ou bien? Ca demande de lire à cahque fois le fichier... Mais est-ce qu'on pourrait pas stocker ces variables d'une manière plus propre? Peut-être en les mettant dans un fichier python qu'on pourrait importer

## Fonctionnalitées
* créer un singe précis
* créer un singe random
* ajouter du texte sur le singe?

## Quickstart
`python setup.py sdist bdist_wheel` \
`pip install .` \
et après dans un script de ton choix \
``` python
import monkey_gerator
monkey_generator.m_generator("test.svg")