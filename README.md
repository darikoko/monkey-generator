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
### Install
`python setup.py sdist bdist_wheel` \
`pip install .`

### Usage
``` python
import monkey_gerator
# créer un nouvel avatar
monkey_generator.MonkeyGenerator()
# créer un nouvel avatar aver des traits précis
monkey_generator.MonkeyGenerator(hat="Crown.xml",glasses="SunglassesAviatorCyan.xml",mouth="SmileBigTeeth.xml")
# créer un nouvel avatar avec un trait aléatoire (ici le chapeau)
monkey_generator.MonkeyGenerator(hat=monkey_generator.random_hat(),glasses="SunglassesAviatorCyan.xml",mouth="SmileBigTeeth.xml")
